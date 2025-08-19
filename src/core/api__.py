import asyncio
import json
import os

from tenacity import retry, retry_if_exception, stop_after_attempt, wait_fixed

from database.models import Account
# import names
from loguru import logger


from curl_cffi import requests

# from models import Account
# from .exceptions.base import APIError, SessionRateLimited, ServerError
# from datetime import datetime, timezone
# from typing import Literal, Tuple, Any
# from loader import captcha_solver, config




# mjs_path = os.path.join(os.path.dirname(__file__), "m.js")
# async def generate_private_key(password ="6b66260453d590ba82faf310"):
#     try:
#         normalized_path = mjs_path.replace("\\", "/")
#         cmd = ['node', '-e', 
#             f'const {{ GeneratePrivateKey }} = require("{normalized_path}");'
#             f'GeneratePrivateKey("{password}").then(console.log)']
#         proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
#         stdout, _ = await proc.communicate()
#         await proc.wait()
#         return stdout.decode().strip()
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

        
    
# async def get_signature(encryptedKey = ""):
#     try:
#         logger.debug(f"开始执行signature脚本")
#         cmd = ['node', '-e', f'const {{ getSignature }} = require(".//m.js"); getSignature("{encryptedKey}").then(console.log)']
#         proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
#         stdout, _ = await proc.communicate()
#         await proc.wait()
#         sigature = stdout.decode().strip()
#         logger.success(f"成功生成签名: {sigature}")
#         return sigature
#     except Exception as e:
#         print(f"Error: {e}")
#         return None





class API():
    # API_URL = "https://www.aeropres.in/chromeapi/dawn"

    def __init__(self, account: Account):
        self.account = account
        # self.wallet_data: dict[str, Any] = {}
        # self.session = self.setup_session()

    @retry(stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=retry_if_exception(lambda e: hasattr(e, 'status_code') and e.status_code in (500, 502, 503, 504)),
        sleep=asyncio.sleep)  # 添加这一行使等待变为异步
    async def ping(self, pub_key: str, node: dict):
        logger.debug(f"开始执行ping......")
        try:
            signature=  get_signature(node.get("encrypted_key"))
            url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/ping"
            payload = {
                "isB7SConnected": False
            }
            headers = {
                'accept': '*/*',
                'authorization': f'Bearer {self.account.bless_auth_token}',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'chrome-extension://pljbjcehnhcnofmkdbjolghdcjnmekia',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'x-extension-signature': signature,
                'x-extension-version': '0.1.8'
            }
            headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
            resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=20, impersonate="safari15_5")
            if isinstance(resp.text, str) and '<html' in resp.text.lower():
                text = resp.text.replace('\n', '').replace('\r', '')[:500]
                logger.debug(f"{self.account.email}---->{text}")
                raise Exception(f"{self.account.email}---->{text}")
            else:
                logger.debug(f"{self.account.email}---->{resp.text}")
            if resp.status_code == 200 and "ok" in resp.text:
                logger.success(resp.text)
                return
        except Exception as e:
            logger.error(f"ping失败: {str(e)}")
            raise Exception(f"ping失败: {str(e)}")


    async def start_session(self, pub_key: str, node: dict):
        signature = await get_signature(node.get("encrypted_key"))
        url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/start-session"
        payload = {}
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {self.account.bless_auth_token}',
            'cache-control': 'no-cache',
            'content-length': '0',
            'origin': 'chrome-extension://pljbjcehnhcnofmkdbjolghdcjnmekia',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'x-extension-signature': signature,
            'x-extension-version': '0.1.8'
        }
        headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
        resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=20, impersonate="safari15_5")
        logger.debug(resp.text)
        if resp.status_code == 200 and "ok" in resp.text:
            logger.success(resp.text)
        raise Exception(resp.text)


    async def stop_session(self, pub_key: str, signature: str):
        url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/stop-session"
        payload = {}
        headers = {
            'accept': '*/*',
            'authorization': f'Bearer {self.account.bless_auth_token}',
            'cache-control': 'no-cache',
            'content-length': '0',
            'origin': 'chrome-extension://pljbjcehnhcnofmkdbjolghdcjnmekia',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'x-extension-signature': signature,
            'x-extension-version': '0.1.8'
        }
        headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
        resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=20, impersonate="safari15_5")
        logger.debug(resp.text)
        if resp.status_code == 200 and "ok" in resp.text:
            logger.success(resp.text)
        raise Exception(resp.text)
    


    async def overview(self) -> int:
        url = "https://gateway-run-indexer.bls.dev/api/v1/users/overview"
        """获取用户总览信息"""
        headers = {
            'accept': '*/*',
            'authorization': F'Bearer {self.account.bless_auth_token}',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://bless.network',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://bless.network/',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site'
        }
        headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
        resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=20, impersonate="safari15_5")
        if resp.status_code == 200 and "allTimeTotalReward" in resp.text:
            data = resp.json()
            logger.success(f"用户总览信息: {data}")
            allTimeTotalReward = data.get("allTimeTotalReward", None)
            return int(allTimeTotalReward)
        else:
            logger.error(f"error in get_user_overview | ")
            print(resp.text)
            return None

































    # async def start_session(self):
    #     """Start a new session"""
    #     print(
    #         f"[{datetime.now(timezone.utc).isoformat()}] Starting session for node {self.node_id}, it might take a while...")
    #     response = await self.send_request(
    #         method=f"/nodes/{self.node_id}/start-session"
    #     )
    #     print(f"[{datetime.now(timezone.utc).isoformat()}] Start session response:", response)
    #     return response

    # async def stop_session(self):
    #     """Stop the current session"""
    #     print(f"[{datetime.now(timezone.utc).isoformat()}] Stopping session for node {self.node_id}")
    #     response = await self.send_request(
    #         method=f"/nodes/{self.node_id}/stop-session"
    #     )
    #     print(f"[{datetime.now(timezone.utc).isoformat()}] Stop session response:", response)
    #     return response

    # async def ping_node(self):
    #     """Send ping to node"""
    #     # print(f"[{datetime.now(timezone.utc).isoformat()}] {self.account_data.email} Pinging node {self.node_id}")
    #     response = await self.send_request(
    #         request_type='POST',
    #         method=f"/nodes/{self.node_id}/ping"
    #     )
    #     log_message = (f"[{datetime.now(timezone.utc).isoformat()}] {self.account_data.email} Ping response: {response}")
    #     logger.success(log_message)
    #     return response

    # @staticmethod
    # async def solve_puzzle(
    #     image: str,
    # ) -> Tuple[str | int, bool, str | int] | Tuple[str, bool] | Tuple[str, bool, str]:
    #     response = await captcha_solver.solve(image)
    #     return response

    # @staticmethod
    # async def report_invalid_puzzle(task_id: int | str) -> None:
    #     await captcha_solver.report_bad(task_id)

    # async def get_puzzle_id(self) -> str:
    #     if "Berear" in self.session.headers:
    #         del self.session.headers["Berear"]
    #         self.session.cookies.clear()

    #     params = {
    #         'appid': 'undefined',
    #     }

    #     response = await self.send_request(
    #         method="/v1/puzzle/get-puzzle",
    #         request_type="GET",
    #         params=params,
    #     )
    #     return response["puzzle_id"]

    # async def get_puzzle_image(self, puzzle_id: str) -> str:
    #     response = await self.send_request(
    #         method="/v1/puzzle/get-puzzle-image",
    #         request_type="GET",
    #         params={"puzzle_id": puzzle_id, "appid": "undefined"},
    #     )

    #     return response.get("imgBase64")

    # async def register(self, puzzle_id: str, answer: str) -> dict:
    #     json_data = {
    #         "firstname": names.get_first_name(),
    #         "lastname": names.get_last_name(),
    #         "email": self.account_data.email,
    #         "mobile": "",
    #         "password": self.account_data.pub_key,
    #         "country": "+91",
    #         "referralCode": config.referral_code,
    #         "puzzle_id": puzzle_id,
    #         "ans": answer,
    #     }

    #     return await self.send_request(
    #         method="/v1/puzzle/validate-register",
    #         json_data=json_data,
    #     )

    # async def keepalive(self) -> dict | str:
    #     headers = {
    #         "accept": "*/*",
    #         "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    #         "authorization": f'Berear {self.session.headers["Berear"]}',
    #         "content-type": "application/json",
    #         "origin": "chrome-extension://fpdkjdnhkakefebpekbdhillbhonfjjp",
    #         "user-agent": self.session.headers["user-agent"],
    #     }

    #     json_data = {
    #         "username": self.account_data.email,
    #         "extensionid": "fpdkjdnhkakefebpekbdhillbhonfjjp",
    #         "numberoftabs": 0,
    #         "_v": "1.0.9",
    #     }

    #     params = {
    #         'appid': 'undefined',
    #     }

    #     return await self.send_request(
    #         method="/v1/userreward/keepalive",
    #         json_data=json_data,
    #         verify=False,
    #         headers=headers,
    #         params=params
    #     )

    # async def user_info(self) -> dict:
    #     headers = self.session.headers.copy()
    #     headers["authorization"] = f'Berear {self.session.headers["Berear"]}'
    #     headers["content-type"] = "application/json"
    #     del headers["Berear"]

    #     params = {
    #         'appid': 'undefined',
    #     }

    #     response = await self.send_request(
    #         url="https://www.aeropres.in/api/atom/v1/userreferral/getpoint",
    #         request_type="GET",
    #         headers=headers,
    #         params=params,
    #     )

    #     return response["data"]

    # async def complete_tasks(self, tasks: list[str] = None, delay: int = 1) -> None:
    #     if not tasks:
    #         tasks = ["telegramid", "discordid", "twitter_x_id"]

    #     headers = self.session.headers.copy()
    #     headers["authorization"] = f'Brearer {self.session.headers["Berear"]}'
    #     headers["content-type"] = "application/json"
    #     del headers["Berear"]

    #     for task in tasks:
    #         json_data = {
    #             task: task,
    #         }

    #         await self.send_request(
    #             method="/v1/profile/update",
    #             json_data=json_data,
    #             headers=headers,
    #         )

    #         await asyncio.sleep(delay)

    # async def verify_session(self) -> tuple[bool, str]:
    #     try:
    #         await self.user_info()
    #         return True, "Session is valid"

    #     except ServerError:
    #         return True, "Server error"

    #     except APIError as error:
    #         return False, str(error)




    # async def login(self, puzzle_id: str, answer: str):
    #     current_time = datetime.now(timezone.utc)
    #     formatted_datetime_str = (
    #         current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    #     )

    #     params = {
    #         'appid': 'undefined',
    #     }

    #     json_data = {
    #         "username": self.account_data.email,
    #         "password": self.account_data.password,
    #         "logindata": {
    #             "_v": "1.0.9",
    #             "datetime": formatted_datetime_str,
    #         },
    #         "puzzle_id": puzzle_id,
    #         "ans": answer,
    #     }

    #     response = await self.send_request(
    #         method="/v1/user/login/v2",
    #         json_data=json_data,
    #         params=params,
    #     )

    #     berear = response.get("data", {}).get("token")
    #     if berear:
    #         self.wallet_data = response.get("data", {}).get("wallet")
    #         self.session.headers.update({"Berear": berear})
    #     else:
    #         raise APIError(f"Failed to login: {response}")


    