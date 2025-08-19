# import asyncio
# #import base64
# from asyncio.log import logger
# import json
# # import aiohttp
# import random
# import sys
# from typing import Dict, Optional, Any
# # import noble_tls
# # from solders.keypair import Keypair
# # from better_proxy import Proxy
# from dataclasses import dataclass
# from curl_cffi.requests import AsyncSession
# from tenacity import retry, retry_if_exception, stop_after_attempt
# from database.models import Nodego_Wallet
# from loguru import logger
# from curl_cffi import requests

# from ..utils.solve_turnstile import solve_nodego_captcha

# # impersonates = ["chrome132_android", "chrome133_android", "chrome134_android", "chrome135_android", "chrome135", "edge135"] 
# impersonates = [
#     # Edge
#     # "edge99",
#     # "edge101",
#     # Chrome
#     # "chrome99",
#     # "chrome100",
#     # "chrome101",
#     # "chrome104",
#     # "chrome107",
#     # "chrome110",
#     # "chrome116",
#     # "chrome119",
#     # "chrome120",
#     # "chrome123",
#     # "chrome124",
#     # "chrome131",
#     # "chrome133a",
#     # "chrome99_android",
#     # "chrome131_android",
#     # Safari
#     # "safari15_3",
#     "safari15_5",
#     # "safari17_0",
#     # "safari17_2_ios",
#     # "safari18_0",
#     # "safari18_0_ios",
#     # Firefox
#     # "firefox133",
#     # "firefox135",
#     # alias
#     # "chrome",
#     # "edge",
#     # "safari",
#     # "safari_ios",
#     # "chrome_android",
#     # "firefox",
#     # Canonical names
#     # "edge_99",
#     # "edge_101",
#     # "safari_15.3_macos",
#     # "safari_15.5_macos",
#     # "safari_17.2_ios",
#     # "safari_17.0_macos",
#     # "safari_18.0_ios",
#     # "safari_18.0_macos",
# ]

# #import uuid
# @dataclass
# class Nodego_Account:
#     username: str
#     email: str
#     password: str

# class NodeApi():
#     def __init__(self, account: Nodego_Wallet=None) -> None:
#         self.account = account
#         # self.proxy_url = self.account.proxy_url
#         # logger.configure(
#         #     handlers=[
#         #         {
#         #             "sink": sys.stdout,  # 输出到控制台
#         #             "format": "{extra[account_id]} ----> {extra[proxy]} {message}",
#         #             "level": "DEBUG",  # 设置日志级别
#         #             "colorize": True  # 启用颜色
#         #         }
#         #     ],
#         #     patcher=lambda record: record.update(
#         #         extra={
#         #             "account_id": self.account.id if self.account else "N/A",
#         #             "proxy": self.proxy_url or "N/A"
#         #         }
#         #     )
#         # )
#         # logger.add(lambda msg: f"{{extra[account_id]}} ----> {{extra[proxy]}} {msg}")
    

#     async def register(self, account: Nodego_Account, captcha_token: str = None):
#         if not captcha_token:
#             raise Exception("captcha_token is required")
#         url = "https://nodego.ai/api/auth/register"
#         payload = {
#             "username": account.username,
#             "email": account.email,
#             "password": account.password,
#             "refBy": "",
#             "captcha": captcha_token
#         }
#         headers = {
#             'accept': 'application/json, text/plain, */*',   
#             'cache-control': 'no-cache',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             logger.success(f"注册成功: {resp.text}")
#             self.account.nodego_access_token = resp.json().get("metadata").get("accessToken")
#             self.account.username = account.username
#             self.account.password = account.password
#             self.account.email = account.email
#             await self.account.save()
#             return True
#         logger.error(f"注册失败: {resp.text}")
#         raise Exception(f"注册失败: {resp.text}")

#     async def login(self, captcha_token: str = None) -> str:
#         if not captcha_token:
#             raise Exception("captcha_token is required")
#         url = "https://nodego.ai/api/auth/login"
#         payload = {
#             "email": self.account.email,
#             "password": self.account.password,
#             "captcha": captcha_token
#         }
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'cache-control': 'no-cache',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site',
#             'user-agent': self.account.user_agent,
#             'accept-language': 'en,en-US;q=0.9'
#         }
#         # headers.update({'user-agent': user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=40, impersonate="safari15_5")
#         logger.debug(resp.text)
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             accessToken = resp.json().get("metadata").get("accessToken")
#             self.account.nodego_access_token = accessToken
#             await self.account.save()
#             return accessToken
#         else:
#             logger.error(f"登录失败: {resp.text}")
#             raise Exception(f"登录失败: {resp.text}")
#     # {"error":"Unauthorized: Invalid JwT Token"}
#     @retry(
#         retry=retry_if_exception(lambda e: any(
#             err in str(e) 
#             for err in ["Curl(97)", "Connection reset", "Curl(28)", "timed out", "Connection timed out"]
#         )),
#         stop=stop_after_attempt(1)
#     )
#     async def ping(self, api_key: str = None):
#         try:
#             async def _send_request():
#                 """封装请求发送逻辑"""
#                 headers = {
#                     'accept': 'application/json, text/plain, */*',
#                     'authorization': f'Bearer {self.account.nodego_access_token}',
#                     'cache-control': 'no-cache',
#                     'content-type': 'application/json',
#                     'origin': 'chrome-extension://jbmdcnidiaknboflpljihfnbonjgegah',
#                     'pragma': 'no-cache',
#                     'priority': 'u=1, i',
#                     'sec-ch-ua-mobile': '?0',
#                     'sec-ch-ua-platform': '"Windows"',
#                     'sec-fetch-dest': 'empty',
#                     'sec-fetch-mode': 'cors',
#                     'sec-fetch-site': 'none',
#                     'user-agent': self.account.user_agent,
#                     'accept-language': 'en,en-US;q=0.9'
#                 }
#                 return await asyncio.to_thread(
#                     requests.post,
#                     url="https://nodego.ai/api/user/nodes/ping",
#                     headers=headers,
#                     json={"type": "extension"},
#                     proxy=self.account.proxy_url,
#                     timeout=20,
#                     impersonate=random.choice(impersonates)
#                 )

#             def _handle_response(resp):
#                 """统一处理响应逻辑"""
#                 if resp.status_code == 200 and (data := resp.json()).get("statusCode") == 200:
#                     metadata = data.get("metadata", {})
#                     logger.success(f"{metadata.get('id')}-------------->{data.get('message')}")
#                     return True
#                 return False

#             # 主逻辑开始
#             if not self.account.nodego_access_token:
#                 raise Exception("Token is required")

#             resp = await _send_request()
#             logger.debug(F"{self.account.email} Ping Response: {resp.text}")
#             if _handle_response(resp):
#                 return True
                
#             if "Unauthorized" in resp.text:
#                 logger.error(f"登录失败: {resp.text}")
#                 captcha_token = await solve_nodego_captcha(api_key=api_key)
#                 await self.login(captcha_token=captcha_token)  # 刷新 token

#             logger.warning(f"Ping failed: {resp.text}")
#             return False
#         except Exception as e:
#             logger.error(f"{self.account.id} ----> {self.account.proxy_url} Ping failed: {e}")
#             raise e

#     async def get_tasks(self) -> list[dict]:
#         """获取任务列表"""
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
#         url = "https://nodego.ai/api/tasks"
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site',
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.get(url, headers=headers)
#         resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=120, impersonate="safari15_5") 
#         if resp.status_code == 200 and resp.json().get("statusCode") == 200:
#             tasks = resp.json().get("metadata", [])
#             logger.success("成功获取任务列表")
#             return tasks
            
#         logger.error(f"获取任务列表失败: {resp.text}")
#         raise Exception(f"获取任务列表失败: {resp.text}")


#     async def get_completed_tasks(self) -> list[dict]:
#         """获取已完成的任务列表"""
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
            
#         url = "https://nodego.ai/api/tasks"
        
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site',
#         }

#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})

# #     {
# #     "statusCode": 200,
# #     "metadata": {
# #         "_id": "67e3c104694b98d5cb968ad7",
# #         "username": "RkBiOkiFfHvS",
# #         "email": "l017c1b1gdx8os@outlook.com",
# #         "userRole": "USER",
# #         "refCode": "NODE4FA6FE8B2C0B",
# #         "refBy": "",
# #         "totalRef": 0,
# #         "rewardPoint": 110,
# #         "refPoint": 0,
# #         "refTon": 0,
# #         "refSol": 0,
# #         "socialTask": [
# #             "T001"
# #         ],
# #         "telegramId": null,
# #         "isVerified": true,
# #         "walletAddress": null,
# #         "isWalletAddressVerified": false,
# #         "verifiedAt": "2025-03-26T08:55:58.306Z",
# #         "checkinDay": 1,
# #         "lastCheckinAt": "2025-03-26T10:00:04.415Z",
# #         "buyNodePoint": 0,
# #         "telegramRefCode": null,
# #         "telegramRefBy": null,
# #         "checkingTon": false,
# #         "retryCheckingTon": 0,
# #         "nodes": [
# #             {
# #                 "_id": "67e3ddbfcd336c89770b8451",
# #                 "id": "81.104.181.72",
# #                 "userId": "67e3c104694b98d5cb968ad7",
# #                 "__v": 0,
# #                 "countryCode": "GB",
# #                 "createdAt": "2025-03-26T10:58:06.657Z",
# #                 "isActive": true,
# #                 "lastConnectedAt": "2025-03-26T10:26:48.879Z",
# #                 "miningSection": [],
# #                 "multiplier": 1,
# #                 "todayPoint": 0,
# #                 "totalPoint": 0,
# #                 "totalUptime": 0,
# #                 "type": "extension",
# #                 "updatedAt": "2025-03-26T11:15:50.238Z"
# #             },
# #             {
# #                 "_id": "67e3df1acd336c897714766b",
# #                 "id": "213.31.80.227",
# #                 "userId": "67e3c104694b98d5cb968ad7",
# #                 "__v": 0,
# #                 "countryCode": "GB",
# #                 "createdAt": "2025-03-26T11:03:53.803Z",
# #                 "isActive": true,
# #                 "lastConnectedAt": "2025-03-26T09:39:11.583Z",
# #                 "miningSection": [],
# #                 "multiplier": 1,
# #                 "todayPoint": 0,
# #                 "totalPoint": 0,
# #                 "totalUptime": 0,
# #                 "type": "extension",
# #                 "updatedAt": "2025-03-26T11:03:53.803Z"
# #             },
# #             {
# #                 "_id": "67e3e3e8cd336c89773219fb",
# #                 "id": "83.36.126.126",
# #                 "userId": "67e3c104694b98d5cb968ad7",
# #                 "__v": 0,
# #                 "countryCode": "ES",
# #                 "createdAt": "2025-03-26T11:24:23.884Z",
# #                 "isActive": true,
# #                 "lastConnectedAt": "2025-03-26T11:10:57.440Z",
# #                 "miningSection": [],
# #                 "multiplier": 1,
# #                 "todayPoint": 0,
# #                 "totalPoint": 0,
# #                 "totalUptime": 0,
# #                 "type": "extension",
# #                 "updatedAt": "2025-03-26T11:27:17.851Z"
# #             }
# #         ],
# #         "createdAt": "2025-03-26T08:55:32.142Z",
# #         "updatedAt": "2025-03-26T11:13:11.801Z"
# #     }
# # }





# # {
# #     "statusCode": 200,
# #     "metadata": [
# #         {
# #             "_id": "675b294fe6967169ad9ffe23",
# #             "title": "Verify Email",
# #             "desc": "It is a long established fact that a reader will be distracted by the readable content of a psum",
# #             "isActive": true,
# #             "reward": 100,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T001",
# #             "link": "",
# #             "time": 0,
# #             "button": "Claim Now",
# #             "icon": "/img/logo/verification.png",
# #             "isDesktopTask": true,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36d1",
# #             "title": "Join Telegram Channel",
# #             "desc": "Stay updated with the latest news, announcements, and opportunities by joining our official Telegram channel.",
# #             "isActive": true,
# #             "reward": 100,
# #             "createdAt": "2024-12-12T18:20:19.952Z",
# #             "updatedAt": "2024-12-12T18:20:19.952Z",
# #             "__v": 0,
# #             "code": "T002",
# #             "link": "https://t.me/nodegoai",
# #             "time": 0,
# #             "button": "Join Now",
# #             "icon": "/img/logo/tele.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": true,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36d4",
# #             "title": "Join Telegram Group",
# #             "desc": "Be part of the conversation! Connect with the community, ask questions, and share your insights in our official group.",
# #             "isActive": true,
# #             "reward": 100,
# #             "createdAt": "2024-12-12T18:20:19.959Z",
# #             "updatedAt": "2024-12-12T18:20:19.959Z",
# #             "__v": 0,
# #             "code": "T003",
# #             "link": "https://t.me/nodego_chat",
# #             "time": 0,
# #             "button": "Join Now",
# #             "icon": "/img/logo/tele.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": true,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36d7",
# #             "title": "Boost Telegram Channel",
# #             "desc": "Help spread the word by boosting our Telegram channel! Your support helps grow our community and reach more people.",
# #             "isActive": true,
# #             "reward": 200,
# #             "createdAt": "2024-12-12T18:20:19.962Z",
# #             "updatedAt": "2024-12-12T18:20:19.962Z",
# #             "__v": 0,
# #             "code": "T004",
# #             "link": "https://t.me/boost/nodegoai",
# #             "time": 10,
# #             "button": "Boost Us",
# #             "icon": "/img/logo/tele.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": true,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36da",
# #             "title": "Follow us on X",
# #             "desc": "Don’t miss out on updates! Follow us on X (formerly Twitter) for real-time news, tips, and exciting announcements.",
# #             "isActive": true,
# #             "reward": 100,
# #             "createdAt": "2024-12-12T18:20:19.965Z",
# #             "updatedAt": "2024-12-12T18:20:19.965Z",
# #             "__v": 0,
# #             "code": "T005",
# #             "link": "https://x.com/NodeGoAI",
# #             "time": 10,
# #             "button": "Follow NodeGo On X",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36dd",
# #             "title": "Rate Chrome Extension",
# #             "desc": "Give us a 5 stars review on Chrome Extension",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:20:19.968Z",
# #             "updatedAt": "2024-12-12T18:20:19.968Z",
# #             "__v": 0,
# #             "code": "T006",
# #             "link": "https://chromewebstore.google.com/detail/nodegoai-depin-hub/jbmdcnidiaknboflpljihfnbonjgegah/reviews",
# #             "time": 10,
# #             "button": "Rate Us",
# #             "icon": "/img/logo/chrome-extension.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36e0",
# #             "title": "Join Telegram MiniApp",
# #             "desc": "Join the telegram miniapps to get passive points",
# #             "isActive": true,
# #             "reward": 100,
# #             "createdAt": "2024-12-12T18:20:19.970Z",
# #             "updatedAt": "2024-12-12T18:20:19.970Z",
# #             "__v": 0,
# #             "code": "T007",
# #             "link": "https://t.me/nodego_bot/app?startapp=NODEDASHBOARD2",
# #             "time": 0,
# #             "button": "Open App",
# #             "icon": "/img/logo/tele.png",
# #             "isDesktopTask": true,
# #             "requiresTelegramApp": true,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36e6",
# #             "title": "Join Discord Channel",
# #             "desc": "Keep active on the NodeGo Discord Community server and support new members, If you continue to be helpful (actually helpful, don't try to pretend - we'll notice you for OG Role ).",
# #             "isActive": true,
# #             "reward": 50,
# #             "createdAt": "2024-12-12T18:20:19.974Z",
# #             "updatedAt": "2024-12-12T18:20:19.974Z",
# #             "__v": 0,
# #             "code": "T009",
# #             "link": "https://discord.com/invite/nodegoai",
# #             "time": 10,
# #             "button": "Open Discord",
# #             "icon": "/img/logo/dis.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675b29635c772c104a3b36e9",
# #             "title": "Add 'NodeGo.Ai' to your name",
# #             "desc": "Show your support for the community! Add 'NodeGo.Ai' to your Telegram display name and let everyone know you’re part of the decentralized revolution.",
# #             "isActive": true,
# #             "reward": 300,
# #             "createdAt": "2024-12-12T18:20:19.977Z",
# #             "updatedAt": "2024-12-12T18:20:19.977Z",
# #             "__v": 0,
# #             "code": "T010",
# #             "link": "",
# #             "time": 10,
# #             "button": "Checking",
# #             "icon": "/img/logo/tele.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": true,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675f2982b9fee43087002943",
# #             "title": "Share Your Referral Link on X",
# #             "desc": "Share your referral link and invite others to join the decentralized revolution. Earn rewards while contributing to a global network powering AI and innovation",
# #             "isActive": true,
# #             "reward": 50,
# #             "createdAt": "2024-12-12T18:20:19.970Z",
# #             "updatedAt": "2024-12-12T18:20:19.970Z",
# #             "__v": 0,
# #             "code": "T011317",
# #             "link": "https://x.com/intent/post?text=SHARE_CONTENT&url=USER_REF_LINK",
# #             "time": 10,
# #             "button": "Share Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675f2c3db9fee43087002946",
# #             "title": "Retweet,Like & Bookmark this tweet",
# #             "desc": "Check detail about our TGE verification process!",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:20:19.970Z",
# #             "updatedAt": "2024-12-12T18:20:19.970Z",
# #             "__v": 0,
# #             "code": "T012325",
# #             "link": "https://x.com/NodeGoAI/status/1904467849093300622",
# #             "time": 10,
# #             "button": "Share Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "675f2cc5b9fee43087002947",
# #             "title": "Comment on our post & Tag 3 friends",
# #             "desc": "🌟 Your comment helps us grow the community and drive innovation!",
# #             "isActive": true,
# #             "reward": 50,
# #             "createdAt": "2024-12-12T18:20:19.970Z",
# #             "updatedAt": "2024-12-12T18:20:19.970Z",
# #             "__v": 0,
# #             "code": "T0140308",
# #             "link": "https://x.com/intent/post?in_reply_to=1897593160085471475&related=depin+crypto",
# #             "time": 10,
# #             "button": "Comment Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "676bdae4f3a24637c9fa1ecd",
# #             "title": "Invite 1 friend",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 500,
# #             "__v": 0,
# #             "code": "T100",
# #             "link": "",
# #             "time": 0,
# #             "button": "Claim Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "invite",
# #             "condition": 1,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "676be081f3a24637c9fa1ecf",
# #             "title": "Invite 3 friends",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 800,
# #             "__v": 0,
# #             "code": "T101",
# #             "link": "",
# #             "time": 0,
# #             "button": "Claim Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "invite",
# #             "condition": 3,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "676be090f3a24637c9fa1ed1",
# #             "title": "Invite 5 friends",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 1000,
# #             "__v": 0,
# #             "code": "T102",
# #             "link": "",
# #             "time": 0,
# #             "button": "Claim Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "invite",
# #             "condition": 5,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "676be09df3a24637c9fa1ed3",
# #             "title": "Invite 10 friends",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 1500,
# #             "__v": 0,
# #             "code": "T103",
# #             "link": "",
# #             "time": 0,
# #             "button": "Claim Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "invite",
# #             "condition": 10,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67ae9c8e9acc872ef2b76f67",
# #             "title": "Follow us on CMC",
# #             "desc": "Don’t miss out on updates! Follow us on CMC for real-time news, tips, and exciting announcements.",
# #             "isActive": true,
# #             "reward": 50,
# #             "createdAt": "2024-12-12T18:20:19.965Z",
# #             "updatedAt": "2024-12-12T18:20:19.965Z",
# #             "__v": 0,
# #             "code": "T013",
# #             "link": "https://coinmarketcap.com/community/profile/nodegoai/",
# #             "time": 10,
# #             "button": "Follow NodeGo On X",
# #             "icon": "https://pbs.twimg.com/profile_images/1875098684469207040/IsOWDeZA_400x400.jpg",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67b2ece39acc872ef2b76fd2",
# #             "title": "Rate Us on Certik",
# #             "desc": "Give us a 5 stars review on Certik",
# #             "isActive": true,
# #             "reward": 50,
# #             "createdAt": "2024-12-12T18:20:19.968Z",
# #             "updatedAt": "2024-12-12T18:20:19.968Z",
# #             "__v": 0,
# #             "code": "T014",
# #             "link": "https://skynet.certik.com/projects/nodego-ai",
# #             "time": 10,
# #             "button": "Rate Us",
# #             "icon": "https://pbs.twimg.com/profile_images/1869644459589193728/oFR5I2i__400x400.jpg",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67d3006c12373626f280479b",
# #             "title": "Join Free Dogs",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T0023",
# #             "link": "https://t.me/theFreeDogs_bot/app?startapp=ref_wtBHOYcq",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/profile_images/1828399486688993281/c3ukSU9m_400x400.jpg",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67dc57da71ac6665f3e31d4c",
# #             "title": "Explore AITech AI Agent Taphub",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T0022",
# #             "link": "https://t.me/AITech_Agents_bot/app?startapp=ref_80pHgmvM",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/media/Gj4_OcOWMAAIgA0?format=jpg&name=small",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67dc580d71ac6665f3e31d4d",
# #             "title": "Join AITech AI Agent Taphub Channel",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T0021",
# #             "link": "https://t.me/aitechagenthub",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/media/Gj4_OcOWMAAIgA0?format=jpg&name=small",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67e2c90cd7ede847d1d0ab79",
# #             "title": "Retweet,Like & Bookmark tweet",
# #             "desc": "🚀 Become a NodeGo Ambassador!",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:20:19.970Z",
# #             "updatedAt": "2024-12-12T18:20:19.970Z",
# #             "__v": 0,
# #             "code": "T0123251",
# #             "link": "https://x.com/NodeGoAI/status/1904467849093300622",
# #             "time": 10,
# #             "button": "Share Now",
# #             "icon": "/img/logo/x.png",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67e3dce9d7ede847d1d0ab7d",
# #             "title": "Join Drops Bot × FOMO App",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T00211",
# #             "link": "https://t.me/+3tBECCkUEEM4YjM8",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/profile_images/1895142681061240832/ASp_kESK_400x400.jpg",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67e3ddd4d7ede847d1d0ab7e",
# #             "title": "Join Drops Analytics",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T00212",
# #             "link": "https://t.me/+0zfoVOd6MsFhMTg8",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/media/Gm9kOCzbYAEDI6g?format=png&name=900x900",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         },
# #         {
# #             "_id": "67e3de91d7ede847d1d0ab7f",
# #             "title": "Join FOMO",
# #             "desc": "",
# #             "isActive": true,
# #             "reward": 10,
# #             "createdAt": "2024-12-12T18:19:59.083Z",
# #             "updatedAt": "2024-12-12T18:19:59.083Z",
# #             "__v": 0,
# #             "code": "T00212",
# #             "link": "https://t.me/fomo/app?startapp=ref_RSU8P",
# #             "time": 10,
# #             "button": "Join Now",
# #             "icon": "https://pbs.twimg.com/profile_images/1895142681061240832/ASp_kESK_400x400.jpg",
# #             "isDesktopTask": false,
# #             "requiresTelegramApp": false,
# #             "type": "sponsor",
# #             "isTelegramTask": false
# #         }
# #     ]
# # }


#     async def client_ip(self) -> Optional[Dict]:
#         url = "https://api.bigdatacloud.net/data/client-ip"
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'cache-control': 'no-cache',
#             'origin': 'chrome-extension://jbmdcnidiaknboflpljihfnbonjgegah',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'cross-site',
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         try:
#             # response = await self.session.get(url, headers=headers)
#             resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=120, impersonate="safari15_5")
#             if resp.status_code == 200:
#                 data = resp.json()
#                 logger.info(f"IP查询成功: {data.get('ipString')}")
#                 return data
#             logger.warning(f"IP查询失败: {resp.text}")
#             return None
#         except Exception as e:
#             logger.error(f"IP查询异常: {str(e)}")
#             return None
    

#     @retry(
#         retry=retry_if_exception(lambda e: any(
#             err in str(e) 
#             for err in ["Curl(97)", "Connection reset", "Curl(28)", "timed out", "Connection timed out"]
#         )),
#         stop=stop_after_attempt(1)
#     )
#     async def update_points(self, api_key: str = None) -> tuple[int, dict]:
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
#         url = "https://nodego.ai/api/user/me"

#         payload = {}
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # resp = await self.session.get(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=120, impersonate="safari15_5")
#         logger.debug(resp.text)
#         if resp.status_code == 200 and resp.json().get("statusCode") == 200:
#             metadata = resp.json().get('metadata')
#             nodes = metadata.get("nodes")
#             totalPoints = float(metadata.get("rewardPoint", 0))
#             node_points = await asyncio.gather(*[
#                 asyncio.to_thread(lambda: float(node.get("totalPoint", 0)))
#                 for node in nodes
#             ])
#             totalPoints += sum(node_points)
#             self.account.last_points = int(totalPoints)
#             logger.success(f"当前积分: {self.account.points}")
#             await self.account.save()
#             # logger.success("积分保存成功......")
#             return int(totalPoints), resp.json()
#         # if "Unauthorized" in resp.text:
#         #     logger.error(f"token过期: {resp.text}")
#         #     captcha_token = await solve_nodego_captcha(api_key=api_key, proxy_url=self.proxy_url)
#         #     self.login(captcha_token=captcha_token)

#         logger.error(f"获取积分失败: {resp.text}")
#         raise Exception(f"获取积分失败: {resp.text}")




#     async def do_task(self, task_code: str) -> bool:
#         """执行指定任务"""
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
#         url = "https://nodego.ai/api/user/task"
#         payload = json.dumps({
#             "taskId": task_code
#         })
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'priority': 'u=1, i',
#             'cache-control': 'no-cache',
#             'pragma': 'no-cache'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.post(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             logger.success(f"任务 {task_code} 完成成功")
#             return True
        
#         if resp.status_code == 400 and resp.json().get("statusCode") == 400:
#             logger.warning(f"任务 {task_code} 完成失败，{resp.text}")


#         logger.error(f"任务执行失败: {resp.text}")
#         raise Exception(f"任务执行失败: {resp.text}")
    


#     async def task_list(self) -> dict:
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
#         url = "https://nodego.ai/api/tasks"
#         payload = {}
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site',
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # resp = await self.session.get(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 200 and resp.json().get("statusCode") == 200:
#             tasks = resp.json()
#             logger.success(f"获取任务列表成功......")
#             return tasks
#         logger.error(f"获取任务列表失败: {resp.text}")
#         raise Exception(f"获取任务列表失败: {resp.text}")



#     async def request_verify_email(self, email: str = None) -> bool:
#         if not email:
#             raise Exception("email is required")
            
#         url = "https://nodego.ai/api/auth/request-verify-email"
        
#         payload = {
#             "email": email
#         }
        
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.post(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             logger.success(f"邮箱验证请求发送成功{resp.text}")
#             return True
#         logger.error(f"邮箱验证请求失败: {resp.text}")
#         return False


#     async def verify_email(self, verification_token: str = None) -> bool:
#         if not verification_token:
#             raise Exception("verification_token is required")
#         url = "https://nodego.ai/api/auth/verify-email"
#         payload = {
#             "token": verification_token
#         }
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.post(url, headers=headers, data=payload, timeout=120)
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             logger.success(f"邮箱验证成功{resp.text}")
#             return True
#         logger.error(f"邮箱验证失败: {resp.text}")
#         return False


#     async def get_daily_earnings(self) -> bool:
#         """
#         获取日常收益信息，并检查最后一个元素是否包含奖励
        
#         Args:
#             token: 认证令牌
            
#         Returns:
#             bool: 如果最后一个元素有任何点数奖励则返回True，否则返回False
#         """
#         if not self.account.nodego_access_token:
#             raise Exception("token is required")
            
#         url = "https://nodego.ai/api/daily-earnings"
        
#         payload = {}
#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'cache-control': 'no-cache',
#             'origin': 'https://app.nodego.ai',
#             'pragma': 'no-cache',
#             'priority': 'u=1, i',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-site'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.get(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 200 and resp.json().get("statusCode") == 200:
#             metadata = resp.json().get("metadata", [])
#             if not metadata:
#                 logger.errot("未找到收益数据")
#                 raise Exception("未找到收益数据")
#             # 获取最后一个元素
#             last_earning = metadata[-1]           # 检查是否有任何类型的点数奖励
#             reward_points = last_earning.get("rewardPoints", 0)
 
#             if reward_points > 0:
#                 logger.success(f"当日以签到，奖励点数: {reward_points}")
#                 return True
#             else:
#                 logger.warning("当日未签到，无奖励点数")
#                 return False
        
#         logger.error(f"获取日常收益失败: {resp.text}")
#         raise Exception(f"获取日常收益失败: {resp.text}")
    

#     async def checkin(self, captcha_token: str) -> bool:
#             """
#             执行每日签到操作
            
#             Returns:
#                 bool: 签到成功返回True，否则返回False
#             """
#             if not self.account.nodego_access_token:
#                 raise Exception("token is required")
                
#             url = "https://nodego.ai/api/user/checkin"
            
#             payload = {
#                 "captcha": captcha_token
#             }

#             # print(payload)
#             # headers = {
#             #     'accept': 'application/json, text/plain, */*',
#             #     'authorization': f'Bearer {self.access_token}',
#             #     'cache-control': 'no-cache',
#             #     'origin': 'https://app.nodego.ai',
#             #     'pragma': 'no-cache',
#             #     'priority': 'u=1, i',
#             #     'referer': 'https://app.nodego.ai/',
#             #     'sec-ch-ua-mobile': '?0',
#             #     'sec-ch-ua-platform': '"Windows"',
#             #     'sec-fetch-dest': 'empty',
#             #     'sec-fetch-mode': 'cors',
#             #     'sec-fetch-site': 'same-site'
#             # }
#             # print(self.session.headers)
#             headers = {
#                 'accept': 'application/json, text/plain, */*',
#                 # 'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7',
#                 'authorization': f'Bearer {self.account.nodego_access_token}',
#                 'cache-control': 'no-cache',
#                 'content-type': 'application/json',
#                 'origin': 'https://app.nodego.ai',
#                 'pragma': 'no-cache',
#                 'priority': 'u=1, i',
#                 'referer': 'https://app.nodego.ai/',
#                 # 'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#                 'sec-ch-ua-mobile': '?0',
#                 'sec-ch-ua-platform': '"Windows"',
#                 'sec-fetch-dest': 'empty',
#                 'sec-fetch-mode': 'cors',
#                 'sec-fetch-site': 'same-site',
#                 # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
#             }
#             headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#             # response = await self.session.post(url, headers=headers, data=payload)
#             resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#             logger.debug(resp.text)
#             if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#                 logger.success(f"签到成功{resp.json().get('metadata').get('message')}")
#                 return True
#             if resp.json().get("statusCode") == 400 and resp.json().get("message") == "You can only check in once per day":
#                 logger.warning(resp.text)
#                 raise Exception("You can only check in once per day")
#             logger.error(f"签到失败: {resp.text}")
#             raise Exception(f"签到失败: {resp.text}")



#     async def oauth2(self, code=None):
#         if code is None:
#             raise Exception("code is required")
#         if not self.account.nodego_access_token:
#                 raise Exception("token is required")
        
#         url = "https://nodego.ai/api/auth/oauth2"

#         payload = {
#             "provider": "x",
#             "code": code
#         }

#         headers = {
#             'accept': 'application/json, text/plain, */*',
#             'authorization': f'Bearer {self.account.nodego_access_token}',
#             'content-type': 'application/json',
#             'origin': 'https://app.nodego.ai',
#             'referer': 'https://app.nodego.ai/',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-site': 'same-site',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-dest': 'empty',
#             'priority': 'u=1, i',
#             'cache-control': 'no-cache',
#             'pragma': 'no-cache'
#         }
#         headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
#         # response = await self.session.post(url, headers=headers, data=payload)
#         resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=self.account.proxy_url, json=payload, timeout=120, impersonate="safari15_5")
#         if resp.status_code == 201 and resp.json().get("statusCode") == 201:
#             metadata = resp.json().get("metadata", {})
#             logger.success(f"OAuth2认证成功: {metadata}")
#             # return (metadata.get("providerId"), metadata.get("providerUser"))
#         else:
#             logger.error(f"OAuth2认证失败: {resp.text}")
#             raise Exception(f"OAuth2认证失败: {resp.text}")

    


    

# # 返回值
# #     {
# #     "statusCode": 201,
# #     "metadata": {
# #         "userId": "67e3c18babbd49a2b64d3d2b",
# #         "provider": "x",
# #         "providerId": "1898145582415319040",
# #         "providerUser": "DedieW25124",
# #         "_id": "67e4cb25309cc9af38c7b025",
# #         "createdAt": "2025-03-27T03:51:01.806Z",
# #         "updatedAt": "2025-03-27T03:51:01.806Z",
# #         "__v": 0
# #     }
# # }





#     # response = requests.request("POST", url, headers=headers, data=payload)
#     # print(response.text)
