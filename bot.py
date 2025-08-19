from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
import asyncio
# import time
from src.core.discord_api import DiscordApi, get_location
from src.core.twitter_api import TwiiterOAuth_1
from distributed_task_processor import execute_distributed_tasks
from src.core.api import API, ResultFormatter
from database.connection import init_db, close_db
from database.models import Account
from loguru import logger
from tortoise.expressions import Q
import random

from itertools import cycle
from loader import config
import multiprocessing
import asyncio
import os

from src.utils.add_accounts_utils import batch_update_account_field_advanced
current_dir = Path(__file__).parent
proxy_urls = config.proxies
user_agents = config.user_agents
  
twitters = config.twitters
discords = config.discords 




temps = []
for twitter in twitters:
    temps.append(twitter.split(':')[5])
twitters = temps
config.twitters = temps
print(config.twitters)





temps = []
#for discord in discords:
#    temps.append(discord.split(':')[2])
discords = config.discords
#config.discords = temps


async def batch_update_twitter_tokens_optimized():
    await init_db()
    try:
        # 一次性获取所有需要的数据
        all_accounts = await Account.all().values('twitter_auth_token')
        existing_tokens = [all_account['twitter_auth_token'] for all_account in all_accounts if all_account['twitter_auth_token']]
        existing_tokens_set = set(existing_tokens)
        need_update_twitters = set(twitters) - existing_tokens_set
        tokens = list(need_update_twitters)
        # 获取需要更新的账户
        need_update_accounts = await Account.filter(twitter_auth_token__isnull=True).all()
        need_update_accounts_list = list(need_update_accounts)
        # 检查token是否足够
        if len(tokens) < len(need_update_accounts_list):
            print(f"警告：可用token数量({len(tokens)})少于需要更新的账户数量({len(need_update_accounts_list)})")
            # 只更新有token可用的账户
            need_update_accounts_list = need_update_accounts_list[:len(tokens)]
        # 直接分配，不使用cycle
        for i, need_update_account in enumerate(need_update_accounts_list):
            need_update_account.twitter_auth_token = tokens[i]
        print(f"准备更新的tokens: {tokens[:len(need_update_accounts_list)]}")
        await Account.bulk_update(need_update_accounts_list, fields=['twitter_auth_token'])
        print(f"成功更新了 {len(need_update_accounts_list)} 个账户的 twitter_auth_token")
        
    except Exception as e:
        logger.error(f"出现错误{str(e)}")
    finally:
        await close_db()





async def batch_add_dc():
    await batch_update_account_field_advanced(field_name='discord_auth_token', new_values=config.discords, filter_condition=(Q(discord_auth_token__isnull=True) and Q(is_twitter_connected=True)))


async def manage_sessions(bot: API):
    """管理会话启动和停止"""
    session_results = []
    
    try:
        # 停止所有会话
        if bot.account.nodes_infos:
            for node in bot.account.nodes_infos:
                pub_key = node.get('pub_key')
                if pub_key:
                    stop_result = await bot.stop_session(pub_key, node)
                    session_results.append(stop_result)
            
            await asyncio.sleep(5)
            
            # 启动所有会话
            for node in bot.account.nodes_infos:
                pub_key = node.get('pub_key')
                if pub_key:
                    start_result = await bot.start_session(pub_key, node)
                    session_results.append(start_result)
        
        # 检查是否所有会话都成功启动
        success_count = sum(1 for result in session_results if "✅" in result and "START SESSION" in result)
        total_nodes = len(bot.account.nodes_infos) if bot.account.nodes_infos else 0
        
        return success_count == total_nodes, session_results
        
    except Exception as e:
        error_result = ResultFormatter.format_error("SESSION MANAGEMENT", f"会话管理异常 - {str(e)}")
        session_results.append(error_result)
        return False, session_results
    


async def start_run_ping(bot: API, action_semaphore: asyncio.Semaphore):
    """
    启动ping任务的包装函数，用于避免惊群效应
    通过随机延迟启动时间来错开任务执行
    """
    # 生成随机延迟时间（0-300秒，即0-5分钟）
    startup_delay = random.uniform(0, 60)
    
    # 输出启动信息
    # print(f"[{bot.account.email}] 将在 {startup_delay:.1f} 秒后启动ping任务")
    
    # 等待随机延迟时间
    await asyncio.sleep(startup_delay)
    
    # 输出实际启动信息
    # print(f"[{bot.account.email}] 正在启动ping任务...")
    
    # 调用实际的ping任务
    await run_ping(bot, action_semaphore)



async def run_ping(bot: API, semaphore: asyncio.Semaphore):
    session_started = False
    while True:
        all_results = []
        session_management_failed = False
        
        try:
            # 使用信号量保护API调用部分
            async with semaphore:
                # 只有在session未启动时才执行manage_sessions
                if not session_started:
                    success, session_results = await manage_sessions(bot)
                    all_results.extend(session_results)
                    
                    if not success:
                        session_management_failed = True
                        all_results.append(ResultFormatter.format_warning("SYSTEM", "会话启动失败，1小时后重试"))
                        # 输出当前结果
                        print(ResultFormatter.format_summary(bot.account.email, all_results))
                        for result in all_results:
                            print(result)
                        # 注意：这里不要continue，而是设置标志位
                    else:
                        session_started = True
                        all_results.append(ResultFormatter.format_info("SYSTEM", "会话启动成功，后续循环将跳过会话启动"))
                
                # 如果会话管理失败，跳过后续的API调用
                if session_management_failed:
                    pass  # 跳过ping等操作
                else:
                    # 执行ping任务
                    if bot.account.nodes_infos:
                        ping_tasks = []
                        for node in bot.account.nodes_infos:
                            pub_key = node.get('pub_key')
                            if pub_key:
                                ping_tasks.append(asyncio.create_task(bot.ping(pub_key, node)))
                        
                        if ping_tasks:
                            ping_results = await asyncio.gather(*ping_tasks, return_exceptions=True)
                            # 处理异常结果
                            for i, result in enumerate(ping_results):
                                if isinstance(result, Exception):
                                    pub_key = bot.account.nodes_infos[i].get('pub_key', 'unknown')
                                    all_results.append(ResultFormatter.format_error("PING", f"{pub_key[-15:]}... 执行异常 - {str(result)}"))
                                else:
                                    all_results.append(result)
                    
                    # 随机执行overview (1/10概率)
                    if random.randint(1, 10) == 1:
                        try:
                            overview_result = await bot.overview()
                            all_results.append(overview_result)
                        except Exception as e:
                            all_results.append(ResultFormatter.format_error("OVERVIEW", f"执行异常 - {str(e)}"))
                    
                    # 执行earnings
                    try:
                        earnings_result = await bot.earnings()
                        all_results.append(earnings_result)
                    except Exception as e:
                        all_results.append(ResultFormatter.format_error("EARNINGS", f"执行异常 - {str(e)}"))
            
            # 信号量已释放，现在可以安全地进行长时间等待
            if session_management_failed:
                await asyncio.sleep(3600)  # 休眠1小时，不占用信号量
                continue
                
        except Exception as e:
            logger.error(f"运行过程中发生严重错误: {str(e)}")
            all_results.append(ResultFormatter.format_error("SYSTEM", f"运行异常 - {str(e)}"))
            # 重置session状态以便下次重试
            session_started = False
        
        # 美化输出所有结果
        try:
            print(ResultFormatter.format_summary(bot.account.email, all_results))
            for result in all_results:
                print(result)
            print(ResultFormatter.create_separator())
        except Exception as e:
            logger.error(f"输出结果时发生错误: {str(e)}")
        
        # 循环间隔
        await asyncio.sleep(9.5 * 60)  # 每9.5分钟执行一次

async def get_socials(bot:API, proxy_url):
    # bot = API(account=Account.get_account("bless@gmail.com"))
    await bot.get_socials(proxy_url)

async def process_get_socials():
    await init_db()
    try:
        proxies = config.proxies
        proxy_urls_cycle = cycle(proxies)
        accounts = await Account.filter(is_delete=False)
        semaphore = asyncio.Semaphore(30)
        async def limited_get_socials(account: Account, proxy_url):
            try:
                async with semaphore:
                    bot = API(account=account)
                    await get_socials(bot, proxy_url)
            except Exception as e:
                logger.error(f"出现错误{str(e)}")
        tasks = [limited_get_socials(account, next(proxy_urls_cycle)) for account in accounts]
        await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        logger.error(f"出现错误{str(e)}")
    finally:
        await close_db()
        
    # proxies = config.proxies
    # proxy_urls_cycle = cycle(proxies)
    # accounts = await Account.filter(is_delete=False)
    # semaphore = asyncio.Semaphore(30)
    # async def limited_get_socials(account: Account, proxy_url):
    #     async with semaphore:
    #         bot = API(account=account)
    #         await get_socials(bot, proxy_url)
    # tasks = [limited_get_socials(account, next(proxy_urls_cycle)) for account in accounts]
    # await asyncio.gather(*tasks)


async def bind_twitter(bot: API, proxy_url=None):
    try:
        if not proxy_url:
            proxy_url= bot.account.proxy_url

        print(bot.account.twitter_auth_token)
        twiiter_oauth = TwiiterOAuth_1(auth_token=bot.account.twitter_auth_token,
                                        user_agent=bot.account.user_agent,
                                        proxy_url=proxy_url)
        await twiiter_oauth.login_1()
        auth_code = await twiiter_oauth.twitter_http_get_auth_code()
        data = await twiiter_oauth.authorize_oauth2(auth_code)
        data = await bot.bind_twitter(auth_code, proxy_url=proxy_url)
        print(data)
    except Exception as e:
        logger.error(f"绑定Twitter失败: {str(e)}")

async def process_bind_twitter():
    await init_db()
    try:
        proxies = config.proxies
        random.shuffle(proxies)
        proxy_urls_cycle = cycle(proxies)
        accounts = await Account.filter(twitter_auth_token__isnull=False, is_delete=False, is_twitter_connected=False)
        print(len(accounts))
        random.shuffle(accounts)
        semaphore = asyncio.Semaphore(10)
        async def limited_bind_twitter(account: Account, proxy_url):
            async with semaphore:
                bot = API(account)
                await bind_twitter(bot, proxy_url)
        tasks = [limited_bind_twitter(account, next(proxy_urls_cycle)) for account in accounts]
        await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        logger.error(f"出现错误{str(e)}")
    finally:
        await close_db()











async def bind_discord_main(bot: API, proxy_url=None):
    location = await get_location(user_agent=bot.account.user_agent, proxy_url=proxy_url, dc_token=bot.account.discord_auth_token)
    logger.success(f"获取到location: {location}")
    response = await bot.bind_discord(proxy_url=proxy_url, code=location.code)
    return response



async def process_bind_discord():
    await init_db()
    try:
        proxies = config.proxies
        random.shuffle(proxies)
        proxy_urls_cycle = cycle(proxies)
        accounts = await Account.filter(discord_auth_token__isnull=False, is_dc_connected=False)
        semaphore = asyncio.Semaphore(10)
        async def limited_bind_discord(account: Account, proxy_url):
            async with semaphore:
                bot = API(account)
                await bind_discord_main(bot, proxy_url)
        tasks = [limited_bind_discord(account, next(proxy_urls_cycle)) for account in accounts]
        await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
        logger.error(f"出现错误{str(e)}")
    finally:
        await close_db()


async def show_menu():
    print("\n" + "="*40)
    print("BlessNetwork 自动化工具菜单".center(40))
    print("="*40)
    print("1. 运行保活任务(pinging)")
    print("3. 运行自定义任务(更新代理/UA)")
    print("4. 正在查询是否连接DC 推特...")
    print("5. 添加推特")
    print("6. 绑定推特")
    print("7. 添加Discord")
    print("8. 绑定Discord")
    print("0. 退出")
    print("="*40)
    return input("请选择要执行的操作 (0-5): ")

async def main():
    while True:
        choice = await show_menu()
        if choice == "1":
            print("正在启动保活任务...")
            execute_distributed_tasks(
                task_coroutine=start_run_ping,
                total_segments=config.FRAMING_PROCESSES,
                action_concurrency=config.FRAMING_CONCURRENCY,
                filter_condition=Q(nodes_len__gt=0),
                startup_delay_range=(5 * 60, 10 * 60), 
            )
        elif choice == "3":
            print("正在运行自定义任务...")
            await main_custom_task()
        elif choice == "4":
            print("正在查询是否连接DC 推特...")
            await process_get_socials()
        elif choice == "5":
            print("正在添加推特...")
            await batch_update_twitter_tokens_optimized()
        elif choice == "6":
            print("正在绑定Twitter...")
            for i in range(1,3):
                await process_bind_twitter()
                time.sleep(30 * 60)
        elif choice == "7":
            print("正在添加Discord...")
            await batch_add_dc()
        elif choice == "8":
            print("正在绑定Discord...")
            await process_bind_discord()
        elif choice == "0":
            print("感谢使用，再见！")
            break
        else:
            print("无效的选择，请重新输入！")


async def update_proxy_urls():
    # proxy_urls = config.proxies
    proxy_urls_cycle = cycle(proxy_urls)
    # username__isnull=False, is_email_verified=True
    accounts = await Account.filter()
    print(accounts)
    # 批量更新代理地址
    for acc in accounts:
        acc.proxy_url = next(proxy_urls_cycle)
        logger.debug(f"为账户 {acc.email} 设置代理: {acc.proxy_url}")
    if len(accounts) > 0:
        await Account.bulk_update(accounts, fields=['proxy_url'])
        logger.success(f"成功批量更新了 {len(accounts)} 个账户的代理地址")

async def update_user_agents():
    if user_agents:
        cycle_user_agents = cycle(user_agents)
        accounts = await Account.filter(user_agent__isnull=True)
        logger.info(f"找到 {len(accounts)} 个需要更新user_agent的账户")
        # 批量更新
        for acc in accounts:
            acc.user_agent = next(cycle_user_agents)
            logger.debug(f"为账户 {acc.email} 设置user_agent: {acc.user_agent}")
        if len(accounts) > 0:
            await Account.bulk_update(accounts, fields=['user_agent'])
            logger.success(f"成功更新了 {len(accounts)} 个账户的user_agent")



# 自定义任务
async def main_custom_task():
    await init_db()
    try:
        await update_proxy_urls()
        await update_user_agents()
    except Exception as e:
        logger.error(f"出现错误{str(e)}")
    finally:
        await close_db()



if __name__ == "__main__":
    asyncio.run(main())







# async def process_run_ping(interval_seconds: int = 120, total_segments: int = 1, current_segment: int = 0):
#     query_condition = Q(nodes_len__gt=0)
#     total_count = await Account.filter(query_condition).count()
#     per_segment = total_count // total_segments
#     offset = current_segment * per_segment
#     offset = 0
#     accounts = await Account.filter(query_condition).offset(offset).limit(per_segment)
#     async def worker(bot: API):
#         while True:
#             try:
#                 await run_ping(bot)
#             except Exception as e:
#                 logger.error(f"处理账户 {account.email} 时出错: {e}")
#             finally:
#                 await asyncio.sleep(interval_seconds)

#     tasks = []
#     for i, account in enumerate(accounts):
#         bot = API(account=account)
#         task = asyncio.create_task(worker(bot))
#         tasks.append(task)
#     await asyncio.gather(*tasks, return_exceptions=True)




# async def process_update_points(limit_numbers: int = 10):
#     accounts = await Account.filter(bless_auth_token__isnull=False)
#     semaphore = asyncio.Semaphore(limit_numbers)
#     async def limited_update_points(account: Account):
#         async with semaphore:
#             bot = API(account)
#             await update_points(bot)
#     tasks = [limited_update_points(account) for account in accounts]
#     await asyncio.gather(*tasks)


# async def _run_process_update_points():
#     await init_db()
#     try:
#         await process_update_points()
#     except Exception as e:
#         logger.error(f"出现错误{str(e)}")
#     finally:
#         await close_db()

# async def schedule_update_points():
#     while True:
#         await _run_process_update_points()  # 直接await协程
#         logger.info("积分更新任务已完成，等待12小时后再次执行...")
#         await asyncio.sleep(24 * 60 * 60)  # 使用asyncio.sleep而不是time.sleep


# async def _run_frameing(segment: int, total_segments: int):
#     await init_db()
#     try:
#         await process_run_ping(interval_seconds=60 * 7, total_segments=total_segments, current_segment=segment)
#     except Exception as e:
#         logger.error(f"出现错误{str(e)}")
#     finally:
#         await close_db()

# def run_frameing_wrapper(segment: int, total_segments: int):
#     asyncio.run(_run_frameing(segment, total_segments))

# def run_frameing(total_segments: int = 3):
#     processes = []
#     for i in range(total_segments):
#         p = multiprocessing.Process(target=run_frameing_wrapper, args=(i, total_segments))
#         p.start()
#         processes.append(p)
#         if i < total_segments - 1:  # 如果不是最后一个进程
#             delay = random.randint(10 * 60, 15 * 60)  # 随机30-60秒间隔
#             time.sleep(delay)  # 等待随机时间
#     for p in processes:
#         p.join()




# async def update_points(bot: API): 
#     all_time_total_reward = await bot.overview()
#     bot.account.points = all_time_total_reward
#     await bot.account.save()
#     logger.success(f"成功更新了 {bot.account.email} 的积分数据")


# async def process_frameing_accounts(interval_seconds: int = 120, total_segments: int = 1, current_segment: int = 0):
#     total_count = await Nodego_Wallet.filter(
#         username__isnull=False, 
#         is_email_verified=True
#     ).count()
#      # 计算每段的数量
#     per_segment = total_count // total_segments
#     # 计算偏移量
#     offset = current_segment * per_segment
#     # 获取当前分段的账户
#     nodego_wallets = await Nodego_Wallet.filter(
#         username__isnull=False, 
#         is_email_verified=True
#     ).offset(offset).limit(per_segment)

#     # proxy_urls_cycle = cycle(proxy_urls)
#     async def worker(nodego_wallet: Nodego_Wallet):
#         while True:
#             try:
#                 await ping(nodego_wallet)
#             except Exception as e:
#                 logger.error(f"处理账户 {nodego_wallet.email} 时出错: {e}")
#             finally:
#                 await asyncio.sleep(interval_seconds)
    
#     tasks = []
#     for i, wallet in enumerate(nodego_wallets):
#         task = asyncio.create_task(worker(wallet))
#         tasks.append(task)

#     await asyncio.gather(*tasks, return_exceptions=True)






    


# async def update_mic_emails():
#     mic_emails = config.mic_emails
#     # 获取数据库会话
#     try:
#         # 获取已存在的邮箱列表
#         existing_emails = {email.email for email in await Nodego_Wallet.filter(email__in=[email.mic_email for email in mic_emails])}
#         # 过滤出不存在的新邮箱
#         new_emails = [email for email in mic_emails if email.mic_email not in existing_emails]
#         # 批量创建新记录
#         await Nodego_Wallet.bulk_create([
#             Nodego_Wallet(
#                 email=email.mic_email,
#                 mic_client_id=email.mic_client_id,
#                 mic_refresh_token=email.mic_refresh_token,
#                 mic_password=email.mic_password,
#                 username=None
#             ) for email in new_emails
#         ])
#         logger.success(f"更新 mic 邮箱成功，新增 {len(new_emails)} 条记录")
#     except Exception as e:
#         logger.error(f"更新 mic 邮箱失败: {str(e)}")


# def generate_password():
#     special_chars = ['#', '@', '$', '%', '!', '*']
#     return (
#         random.choice(special_chars)
#         + ''.join(random.choices(string.ascii_uppercase, k=2))
#         + ''.join(random.choices(string.ascii_lowercase, k=3))
#         + ''.join(random.choices(string.digits, k=10))
#         + ''.join(random.choices(string.ascii_lowercase, k=1))
#     )


# def generate_random_string():
#     length = random.randint(10, 13)
#     chars = string.ascii_letters + string.digits
#     return ''.join(random.choice(chars) for _ in range(length))

# async def reg_account(node_go_wallet: Nodego_Wallet):
#     node_api = NodeApi(account=node_go_wallet)
#     try:
#         mic_account = Mic_Account(
#             email=node_go_wallet.email,
#             client_id=node_go_wallet.mic_client_id,
#             refresh_token=node_go_wallet.mic_refresh_token
#         )
#         email_criteria = EmailCriteria(
#             from_address='no-reply@nodego.ai'
#         )
#         mic_link_extractor = MicLinkExtractor(account=mic_account)
#         await mic_link_extractor.refresh_access_token()
#         await asyncio.to_thread(mic_link_extractor.delete_matching_emails, account=mic_account, email_criteria=email_criteria)
#         pwd = generate_password()
#         username = generate_random_string()
#         nodego_account = Nodego_Account(
#             username=username,
#             email=node_go_wallet.email,
#             password=pwd
#         )
#         captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#         logger.success(f"验证码解决成功！令牌: {captcha_token}")
#         await node_api.register(account=nodego_account, captcha_token=captcha_token)
#         logger.success(f"注册成功！用户名: {username}")
#         # node_go_wallet.username = username
#         # node_go_wallet.password = pwd
#         # node_go_wallet.nodego_access_token = node_api.nodego_access_token
#         # await node_go_wallet.save()
#         await asyncio.sleep(3)
#         await node_api.request_verify_email(email=nodego_account.email)
#         logger.success(f"请求验证邮箱成功！用户名: {username}")

#         # email_content = mic_link_extractor.retrieve_matching_email_content(account=mic_account, email_criteria=email_criteria)
#         email_content = await asyncio.to_thread(
#             mic_link_extractor.retrieve_matching_email_content, 
#             account=mic_account, 
#             email_criteria=email_criteria
#         )
#         verification_link = extract_verification_link(email_content)
#         # https://app.nodego.ai/verify-email?token=fea29dfd-ce9b-4b4f-a271-2fa1597feb4d
#         token = verification_link.split('verify-email?token=')[1]
#         if not token:
#             raise Exception("没有获取token")
#         logger.success(f"成功获取到token:{token}")
#         await node_api.verify_email(verification_token=token)
#         node_go_wallet.is_email_verified = True
#         await node_go_wallet.save()
#     except Exception as e:
#         logger.error(f"{node_go_wallet.email}注册过程中出现错误: {str(e)}")
#     # finally:
#         # await node_api.session.close()





# async def only_verify_email(nodego_wallet: Nodego_Wallet, proxy_url:str = None):
#     mic_account = Mic_Account(
#         email=nodego_wallet.email,
#         client_id=nodego_wallet.mic_client_id,
#         refresh_token=nodego_wallet.mic_refresh_token
#     )
#     email_criteria = EmailCriteria(
#         from_address='no-reply@nodego.ai'
#     )
#     mic_link_extractor = MicLinkExtractor(account=mic_account)
#     await mic_link_extractor.refresh_access_token()
#     await mic_link_extractor.delete_matching_emails(account=mic_account, email_criteria=email_criteria)
#     node_api = NodeApi(
#         proxy_url=proxy_url,
#     )
#     try:
#         if nodego_wallet.nodego_access_token:
#             node_api.access_token = nodego_wallet.nodego_access_token
#         else:
#             await node_api.login(email=nodego_wallet.email, password=nodego_wallet.password)
#             nodego_wallet.nodego_access_token = node_api.access_token
#             await nodego_wallet.save()

#         await asyncio.sleep(0.1)
#         await node_api.request_verify_email(email=nodego_wallet.email)
        
#         email_content = mic_link_extractor.retrieve_matching_email_content(account=mic_account, email_criteria=email_criteria)
#         verification_link = extract_verification_link(email_content)
#         token = verification_link.split('verify-email?token=')[1]
#         if not token:
#             raise Exception("未找到验证链接")
#         await asyncio.sleep(0.1)
#         logger.debug(f"成功获取到token:{token}")
#         await node_api.verify_email(verification_token=token)
#         nodego_wallet.is_email_verified = True
#         await nodego_wallet.save()
#     except Exception as e:
#         logger.error(f"邮箱验证失败: {str(e)}")
#     finally:
#         await node_api.session.close()


# async def check_in(nodego_wallet: Nodego_Wallet):
#     # logger.debug(f"输出当前代理ip:{proxy_url}")
#     node_api = NodeApi(account=nodego_wallet)
#     try:
#         # if nodego_wallet.nodego_access_token:
#         #     node_api.access_token = nodego_wallet.nodego_access_token
#         if not nodego_wallet.nodego_access_token:
#             captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#             await node_api.login(captcha_token=captcha_token)
#             # nodego_wallet.nodego_access_token = node_api.access_token
#             #await nodego_wallet.save()
#          # 新增签到逻辑
    
#         if nodego_wallet.check_in_at is None or (datetime.now() - nodego_wallet.check_in_at.replace(tzinfo=None)) >= timedelta(hours=24):
#             captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#             await node_api.checkin(captcha_token=captcha_token)
#             nodego_wallet.check_in_at = datetime.now()
#             # 更新积分（假设每次签到获得100积分，根据实际情况调整）
#             await nodego_wallet.save()
#             logger.success(f"账户 {nodego_wallet.email} 签到成功")
#     except Exception as e:
#         logger.error(f"签到失败: {str(e)}")
#     finally:
#         await node_api.session.close()



# async def update_points(nodego_wallet: Nodego_Wallet):
#     # logger.debug(f"输出当前代理ip:{proxy_url}")
#     node_api = NodeApi(account=nodego_wallet)
#     try:
#         # last_points
#         if not nodego_wallet.nodego_access_token:
#             captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#             await node_api.login(captcha_token=captcha_token)
#         await node_api.update_points(api_key=config.two_captcha_api_key)
#     except Exception as e:
#         logger.error(f"获取积分失败: {str(e)}")


# async def process_update_points(limit_numbers: int = 50):
#     nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=True)
#     semaphore = asyncio.Semaphore(limit_numbers)
#     async def limited_update_points(nodego_wallet: Nodego_Wallet):
#         async with semaphore:
#             await update_points(nodego_wallet)
#     tasks = [limited_update_points(nodego_wallet) for nodego_wallet in nodego_wallets]
#     await asyncio.gather(*tasks)



# async def process_reg_accounts(limit_numbers: int = 3):
#     nodego_wallets = await Nodego_Wallet.filter(is_email_verified=False, nodego_access_token__isnull=True)
#     semaphore = asyncio.Semaphore(limit_numbers)
#     async def limited_reg_account(nodego_wallet: Nodego_Wallet):
#         async with semaphore:
#             await reg_account(nodego_wallet)
#     tasks = [limited_reg_account(nodego_wallet) for nodego_wallet in nodego_wallets]
#     await asyncio.gather(*tasks, return_exceptions=True)

# async def oauth_twitter(auth_token: str, user_agent: str, proxy_url: str):
#     try:
#         # 初始化客户端
#         client = TwiiterOAuth_1(
#             auth_token=auth_token,
#             user_agent=user_agent,
#             proxy_url=proxy_url
#         )
#         # 第一步：登录获取ct0
#         login_result = await client.login_1()
#         if not login_result.ok:
#             logger.error(f"登录失败: {login_result.msg}")
#             return login_result
#         # 第二步：获取授权码
#         await client.get_html()
#         auth_code = await client.get_auth_code()
#         # 第三步：授权确认
#         final_code = await client.authorize(auth_code)
#         logger.success(f"OAuth流程完成，最终授权码: {final_code}")
#         return final_code
#     except Exception as e:
#         logger.error(f"OAuth流程异常: {str(e)}")
#         raise Exception(f"OAuth流程异常: {str(e)}")


# async def con_twitter(nodego_wallet: Nodego_Wallet, proxy_url):
#     try:
#         node_api = NodeApi(proxy_url=proxy_url, account=nodego_wallet)
#         if not nodego_wallet.nodego_access_token:
#             captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#             await node_api.login(captcha_token=captcha_token)
#         # 初始化客户端
#         final_code = await oauth_twitter(
#             auth_token=nodego_wallet.tw_token,
#             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
#             proxy_url=proxy_url
#         )
#         logger.success(f"OAuth流程完成，最终授权码: {final_code}")
#         await node_api.oauth2(final_code)
#         nodego_wallet.is_tw_connected = True
#         await nodego_wallet.save()

#     except Exception as e:
#         logger.error(f"OAuth流程异常: {str(e)}")


# async def process_con_twitter(limit_numbers: int = 15):
#     try:
#         nodego_wallets = await Nodego_Wallet.filter(
#             username__isnull=False,
#             is_email_verified=True,
#             is_tw_connected=False,
#             tw_token__isnull=False
#         )
#         # proxy_urls = await load_proxy_url_list(r'D:\codes\nodego\data\proxies.txt')
#         proxy_urls_cycle = cycle(proxy_urls)
#         semaphore = asyncio.Semaphore(limit_numbers)
        
#         async def limited_con_twitter(nodego_wallet: Nodego_Wallet, proxy_url):
#             async with semaphore:
#                 await con_twitter(nodego_wallet, proxy_url)
        
#         tasks = [
#             limited_con_twitter(wallet, next(proxy_urls_cycle))
#             for wallet in nodego_wallets
#         ]
#         await asyncio.gather(*tasks)
        
#     except Exception as e:
#         logger.error(f"处理Twitter连接时出错: {str(e)}")

# async def process_check_in(limit_numbers: int = 10):
#     try:
#         nodego_wallets = await Nodego_Wallet.filter(
#             Q(check_in_at__isnull=True) | Q(check_in_at__lt=datetime.now() - timedelta(hours=24)),
#             username__isnull=False,
#             is_email_verified=True,
#             nodego_access_token__isnull=False
#         )

#     #     proxy_urls = config.proxies



#     # # proxy_urls_cycle = cycle(proxies)
#     #     proxy_urls_cycle = cycle(proxy_urls)
#         semaphore = asyncio.Semaphore(limit_numbers)  # 默认并发限制为10
#         async def limited_check_in(nodego_wallet: Nodego_Wallet):
#             async with semaphore:
#                 await check_in(nodego_wallet)
#         tasks = [
#             limited_check_in(wallet)
#             for wallet in nodego_wallets
#         ]
#     except Exception as e:
#         logger.error(f"process_check_in出错{str(e)}")
#     await asyncio.gather(*tasks, return_exceptions=True)




# async def login(nodego_wallet: Nodego_Wallet):
#     # if "http" in nodego_wallet.proxy_url:
#     #     return
#     node_api = NodeApi(account=nodego_wallet)
#     try:
#         # 
#         # await node_api.login(captcha_token=captcha_token)
#         try:
#             await node_api.login(captcha_token=captcha_token)
#         except Exception as e:
#             if "Invalid captcha verification" in str(e):
#                 captcha_token = await solve_nodego_captcha(api_key=config.two_captcha_api_key)
#                 try:
#                     await node_api.login(captcha_token=captcha_token)
#                 except Exception as e:
#                     logger.error(f"如果依然出现链接失败,说明是时间问题,不是ip问题: {str(e)}")
#                     return False
#             raise e

#         # await nodego_wallet.save()
#         # await asyncio.sleep(0.1)
#         # await node_api.request_verify_email(email=nodego_wallet.email)
#         logger.success(f"登录成功！用户名: {nodego_wallet.username}")
#         return True
#     except Exception as e:
#         logger.error(f"登录失败: {str(e)}")
#         return False



# async def process_login_accounts(limit_numbers: int = 15):
#     nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=True, nodego_access_token__isnull=True)
#     semaphore = asyncio.Semaphore(limit_numbers)
#     async def limited_login_account(nodego_wallet: Nodego_Wallet):
#         async with semaphore:
#             await login(nodego_wallet)
#     tasks = [limited_login_account(nodego_wallet) for nodego_wallet in nodego_wallets]
#     await asyncio.gather(*tasks, return_exceptions=True)




# async def update_proxy_urls():
#     proxy_urls = config.proxies
#     proxy_urls_cycle = cycle(proxy_urls)
#     # username__isnull=False, is_email_verified=True
#     accounts = await Nodego_Wallet.filter()
#     # 批量更新代理地址
#     for acc in accounts:
#         acc.proxy_url = next(proxy_urls_cycle)
#         logger.debug(f"为账户 {acc.email} 设置代理: {acc.proxy_url}")
#     if len(accounts) > 0:
#         await Nodego_Wallet.bulk_update(accounts, fields=['proxy_url'])
#         logger.success(f"成功批量更新了 {len(accounts)} 个账户的代理地址")



# # async def refersh_token():
# #     nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=True)
# #     # proxy_urls_cycle = cycle(proxy_urls)
# #     semaphore = asyncio.Semaphore(10)
# #     async def limited_refresh_token(nodego_wallet: Nodego_Wallet, proxy_url):
# #         async with semaphore:
# #             await refresh_token(nodego_wallet, proxy_url)



# async def process_verify_email_accounts(limit_numbers: int = 10):
#     # proxy_urls = await load_proxy_url_list(r'D:\codes\nodego\data\proxies.txt')
#     proxy_urls_cycle = cycle(proxy_urls)
#     nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=False)
#     # 协程限制
#     semaphore = asyncio.Semaphore(limit_numbers)
#     async def limited_verify_email_account(nodego_wallet: Nodego_Wallet, proxy_url):
#         async with semaphore:
#             await only_verify_email(nodego_wallet, proxy_url)
#     tasks = [limited_verify_email_account(nodego_wallet, next(proxy_urls_cycle)) for nodego_wallet in nodego_wallets]
#     await asyncio.gather(*tasks)



# async def reset_nodego_points(nodego_wallet: Nodego_Wallet):
#     # nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=True, nodego_access_token__isnull=False)
#     logger.info(f"开始重置账户 {nodego_wallet.email} 的积分数据")
#     nodego_wallet.points_diff = nodego_wallet.last_points - nodego_wallet.points
#     logger.debug(f"计算积分差: {nodego_wallet.points_diff} (last_points={nodego_wallet.last_points}, points={nodego_wallet.points})")
#     nodego_wallet.points = nodego_wallet.last_points 
#     await nodego_wallet.save()
#     logger.success(f"成功重置账户 {nodego_wallet.email} 的积分数据")


# async def process_reset_nodego_points():
#     nodego_wallets = await Nodego_Wallet.filter(username__isnull=False, is_email_verified=True, nodego_access_token__isnull=False)
#     semaphore = asyncio.Semaphore(10)
#     async def limited_reset_nodego_points(nodego_wallet: Nodego_Wallet):
#         async with semaphore:
#             await reset_nodego_points(nodego_wallet)
#     tasks = [limited_reset_nodego_points(nodego_wallet) for nodego_wallet in nodego_wallets]
#     await asyncio.gather(*tasks)





# async def main_update_points():
#     await init_db()
#     try:
#         # 更新分数任务
#         while True:
#             now = datetime.now()
#             # 设置目标时间为中国时区晚上11点
#             target_time = now.replace(hour=23, minute=0, second=0, microsecond=0)
#             # 如果现在时间已经过了11点，就设置目标时间为明天的11点
#             if now > target_time:
#                 target_time += timedelta(days=1)
#             # 计算需要等待的时间
#             wait_seconds = (target_time - now).total_seconds()
#             logger.info(f"等待 {wait_seconds/3600:.2f} 小时直到晚上11点...")
#             await asyncio.sleep(wait_seconds)
#             # 到达目标时间后执行任务
#             logger.info("开始执行每日积分更新任务...")
#             for _ in range(3):
#                 await process_update_points()
#                 await asyncio.sleep(300)
#             # 分数更新
#             await process_reset_nodego_points()

#     except Exception as e:
#         logger.error(f"出现错误{str(e)}")
#     finally:
#         await close_db()



# async def main_check_in():
#     await init_db()
#     try:
#         # 签到任务
#         while True:
#             await process_check_in(10)
#             logger.info("任务执行完成，等待12小时后重新执行...")
#             await asyncio.sleep(7 * 60 * 60)  # 休眠12小时
        
#     except Exception as e:
#         logger.error(f"出现错误{str(e)}")
#     finally:
#         await close_db()





