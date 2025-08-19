# distributed_task_processor.py
import asyncio
import time
import random
import multiprocessing
from typing import Callable, Awaitable, Optional, Tuple, TypeVar, List, Union, Dict, Any
from tortoise.models import Q
from database.connection import init_db, close_db
from database.models import Account
from loguru import logger
import inspect

from src.core.api import API

TaskCoroutine = Callable[..., Awaitable[None]]

class AsyncDBContext:
    """Asynchronous context manager for per-process database initialization and shutdown."""
    async def __aenter__(self):
        process_name = multiprocessing.current_process().name
        logger.debug(f"[{process_name}] Initializing database connection.")
        await init_db()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        process_name = multiprocessing.current_process().name
        if exc_type:
            logger.error(f"[{process_name}] Exiting DBContext due to an exception: {exc_val}")
        logger.debug(f"[{process_name}] Closing database connection.")
        await close_db()
        return False

async def fetch_accounts_for_segment(
    total_segments: int,
    current_segment_index: int,
    filter_condition: Optional[Q] = None
) -> List[Account]:
    """
    Fetches a specific segment of accounts from the database.
    This logic ensures all accounts are covered even with uneven distribution.
    """
    base_query = Account.all()
    if filter_condition:
        base_query = base_query.filter(filter_condition)
    
    total_accounts = await base_query.count()
    if total_accounts == 0:
        return []

    base_size = total_accounts // total_segments
    remainder = total_accounts % total_segments

    if current_segment_index < remainder:
        limit = base_size + 1
        offset = current_segment_index * (base_size + 1)
    else:
        limit = base_size
        offset = (remainder * (base_size + 1)) + ((current_segment_index - remainder) * base_size)

    logger.info(
        f"Segment {current_segment_index}/{total_segments-1}: Fetching {limit} accounts from offset {offset} (Total: {total_accounts})"
    )
    return await base_query.offset(offset).limit(limit)

async def process_segment_tasks(
    task_coroutine: TaskCoroutine,
    total_segments: int,
    current_segment_index: int,
    # <<< MODIFIED >>> Renamed for generality
    action_concurrency: int,
    filter_condition: Optional[Q] = None,
    task_kwargs: Dict[str, Any] = None
):
    """
    Manages the task execution for all accounts within a single segment
    using a name-based dependency injection system.
    """
    accounts = await fetch_accounts_for_segment(total_segments, current_segment_index, filter_condition)
    if not accounts:
        logger.warning(f"Segment {current_segment_index}: No accounts found to process for the given filter.")
        return

    process_name = multiprocessing.current_process().name
    logger.info(f"[{process_name}] Segment {current_segment_index}: Starting processing for {len(accounts)} accounts.")

    # --- Framework-Managed Resources ---
    # <<< MODIFIED >>> Renamed for generality
    action_semaphore: Optional[asyncio.Semaphore] = None
    if action_concurrency and action_concurrency > 0:
        # <<< MODIFIED >>> Use the new generalized variable
        action_semaphore = asyncio.Semaphore(action_concurrency)
        logger.info(f"[{process_name}] Action concurrency limit per process set to {action_concurrency}.")
    else:
        logger.info(f"[{process_name}] No action concurrency limit set.")
        
    sig = inspect.signature(task_coroutine)
    task_param_names = sig.parameters.keys()

    async def _account_task_worker(account: Account):
        """A worker that prepares context and intelligently calls the user's task."""
        process_name = multiprocessing.current_process().name
        # logger.debug(f"[{process_name}] Worker starting for Account ID: {account.id}")

        try:
            # --- Assemble the context of all available arguments ---
            context_args = {
                "account": account,
                "bot": API(account),
                **(task_kwargs or {})
            }
            # <<< MODIFIED >>> Use the new semaphore name for injection
            if action_semaphore:
                context_args["action_semaphore"] = action_semaphore
            
            # --- Dependency Injection Logic ---
            final_args = {
                name: context_args[name] 
                for name in task_param_names 
                if name in context_args
            }

            await task_coroutine(**final_args)

        except asyncio.CancelledError:
            pass
            # logger.info(f"[{process_name}] Worker for Account ID {account.id} was cancelled.")
        except TypeError as e:
            logger.error(
                f"[{process_name}] TypeError calling task for Account {account.id}. "
                f"This likely means the task requires an argument that was not provided "
                f"in execute_distributed_tasks's kwargs. Error: {e}", exc_info=True
            )
        except Exception as e:
            logger.critical(f"[{process_name}] Worker for Account {account.id} crashed with unhandled exception: {e}", exc_info=True)
        # finally:
        #     logger.warning(f"[{process_name}] Worker for Account {account.id} has exited its task loop.")

    tasks = [asyncio.create_task(_account_task_worker(acc)) for acc in accounts]
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

async def _segment_process_entrypoint(
    segment_index: int,
    total_segments: int,
    task_coroutine: TaskCoroutine,
    # <<< MODIFIED >>> Renamed for generality
    action_concurrency: int,
    filter_condition: Optional[Q] = None,
    task_kwargs: Dict[str, Any] = None
):
    """The main asynchronous entry point for a single process."""
    process_name = multiprocessing.current_process().name
    logger.info(f"[{process_name}] Starting segment processing: {segment_index}/{total_segments-1}")
    
    async with AsyncDBContext():
        try:
            await process_segment_tasks(
                task_coroutine=task_coroutine,
                total_segments=total_segments,
                current_segment_index=segment_index,
                # <<< MODIFIED >>> Pass the renamed parameter
                action_concurrency=action_concurrency,
                filter_condition=filter_condition,
                task_kwargs=task_kwargs
            )
        except Exception as e:
            logger.critical(f"[{process_name}] Unhandled critical error in segment {segment_index}: {e}", exc_info=True)
        finally:
            logger.info(f"[{process_name}] Segment {segment_index} processing has finished.")

def _process_target_func(**kwargs):
    """
    The target function for `multiprocessing.Process`.
    Accepts kwargs to avoid argument order issues.
    """
    asyncio.run(_segment_process_entrypoint(**kwargs))

def execute_distributed_tasks(
    task_coroutine: TaskCoroutine,
    total_segments: int,
    # <<< MODIFIED >>> Renamed public-facing parameter for clarity and generality.
    action_concurrency: int,
    filter_condition: Optional[Q] = None,
    startup_delay_range: Tuple[int, int] = (5, 15),
    **task_kwargs: Any
):
    """
    Launches and manages distributed task processing using multiprocessing.

    Args:
        task_coroutine: The async function to be executed for each account. It will be
                        injected with arguments by name. Available arguments are:
                        'api_client', 'account', 'action_semaphore' (if action_concurrency > 0), 
                        and any custom arguments passed via **task_kwargs.
        total_segments: The number of processes to spawn.
        action_concurrency: Max concurrent "actions" per process. An "action" is whatever
                            part of your task you choose to gate with the `action_semaphore`.
                            Set to 0 or None to disable.
        filter_condition: An optional Tortoise-ORM Q object to filter accounts.
        startup_delay_range: A tuple (min, max) for random delay between process launches.
        **task_kwargs: Custom keyword arguments to be passed to every execution of
                       the task_coroutine.
    """
    if total_segments < 1:
        logger.error("`total_segments` must be at least 1.")
        return

    processes: List[multiprocessing.Process] = []
    logger.info(f"Master process initiating {total_segments} worker processes.")
    logger.info(f"User-defined task arguments (task_kwargs): {task_kwargs}")

    for i in range(total_segments):
        process_name = f"WorkerProcess-{i}"
        
        process_kwargs = {
            "segment_index": i,
            "total_segments": total_segments,
            "task_coroutine": task_coroutine,
            # <<< MODIFIED >>> Use the new parameter name
            "action_concurrency": action_concurrency,
            "filter_condition": filter_condition,
            "task_kwargs": task_kwargs
        }
        
        process = multiprocessing.Process(
            target=_process_target_func,
            kwargs=process_kwargs,
            name=process_name
        )
        processes.append(process)
        process.start()
        logger.info(f"Launched process: {process.name} (PID: {process.pid}) for segment {i}.")
        
        if i < total_segments - 1:
            delay = random.randint(*startup_delay_range)
            logger.info(f"Waiting {delay} seconds before launching next process...")
            time.sleep(delay)
    
    logger.info("All worker processes have been launched. Main process is now monitoring.")
    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        logger.warning("Master process received KeyboardInterrupt. Terminating worker processes...")
        for p in processes:
            if p.is_alive():
                p.terminate()
                p.join(timeout=5)
                if p.is_alive():
                    logger.warning(f"Process {p.name} did not terminate gracefully. Forcing kill.")
                    p.kill()
        logger.info("All worker processes have been terminated.")
    finally:
        logger.info("Master process is shutting down.")





# ### Rationale for Changes

# 1.  **Generality and Abstraction**: The primary driver for this change is to make the framework more abstract. `action_concurrency` communicates that the user can control the concurrency of *any* critical section in their task, whether it's API calls, database writes, or CPU-intensive work. This is far more flexible than `login_concurrency`.
# 2.  **Clarity and Intent**: The new name makes the code's intent clearer. A new developer looking at `execute_distributed_tasks` immediately understands that `action_concurrency` is a generic throttle, not a feature tied to a specific business logic like "login".
# 3.  **Consistent Naming**: Pairing `action_concurrency` (the configuration value) with `action_semaphore` (the injected object) creates a clear and consistent mental model for the developer writing the task coroutine. They know that setting the former makes the latter available.

# ### Updated "How to Use" Examples

# Here are updated examples demonstrating how to use the refactored framework, including a new example that explicitly uses the `action_semaphore`.

# **Example 1: Simple task (unaffected by the change)**
# This task does not require throttling, so it doesn't request the `action_semaphore`. It works exactly as before.

# ```python
# # In your main script
# from src.core.api import Api # Assuming this is your API wrapper

# async def simple_task(api_client: Api):
#     """A simple task that just needs the api_client."""
#     print(f"Executing simple task for account {api_client.account.id}")
#     await api_client.get_profile_info() # Example API call

# # Usage:
# # The framework will not inject 'action_semaphore' as it's not in the function signature.
# execute_distributed_tasks(simple_task, total_segments=4)
