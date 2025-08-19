import asyncio
from dataclasses import dataclass
import os
import re
import traceback
from urllib.parse import parse_qs, urlparse
import httpx
# import requests
# from fake_useragent import UserAgent
# from utils.RandomAcceptLanguage import RandomAcceptLanguage
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential, wait_fixed
# from curl_cffi.requests import AsyncSession
from curl_cffi import requests
from database.models import Account

# from database.models.accounts import Accounts


# def get_proxies():
#     if "https_proxy" in os.environ:
#         del os.environ["https_proxy"]
#     if "http_proxy" in os.environ:
#         del os.environ["http_proxy"]
#     while True:
#         try:
#             res = requests.get('http://192.168.20.104:19999/rand-ip')
#             data = res.json()
#             proxies = {"http://": f'http://{data["host"]}:{data["port"]}', "https://": f'http://{data["host"]}:{data["port"]}'}
#             res = requests.get('https://task.bsquared.network/points/', proxies=proxies, timeout=2)
#             if res.status_code == 200:
#                 return proxies["http://"]
#         except:
#             pass
@dataclass
class DiscordOAuth:
    location: str
    code: str
    status_code: int

@dataclass
class TwiiterOAuth:
    oauth_token: str
    oauth_verifier: str
    redirect_url: str

class DiscordApi:
    #dc_token: str = None, user_agent: str = None, proxy_url: str = None, 

    def __init__(self, account: Account, timeout: int = 6000): 

        # self.user_agent = db_account_data.user_agent
        self.dc_token = account.discord_auth_token
        self.timeout = timeout
        self.account = Account
        # self.task = task
        # self.session = self.setup_session(timeout)
        # if db_account_data.proxy_url:
        #     self.session.proxies = {
        #         "http": db_account_data.proxy_url,
        #         "https": db_account_data.proxy_url
        #     }
        # else:
        #     logger.warning("不存在代理ip")
        #     return
        #     }
        # elif self.task.proxy_url:
        #     self.session.proxies = {
        #         "http": self.task.proxy_url,
        #         "https": self.task.proxy_url
        #     }
        
    # def setup_session(self, timeout: int) -> AsyncSession:
    #     session = AsyncSession(impersonate="chrome124", verify=False, timeout=timeout)
    #     return session


    # @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def test_survival(self) -> int:
        headers = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "authorization": self.dc_token,
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://discord.com/channels/@me",
            # "user-agent": self.user_agent,
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "zh-CN",
            "x-discord-timezone": "Asia/Shanghai",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLUNOIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNDc2OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        url = "https://discord.com/api/v9/content-inventory/users/@me"
        # response = await self.session.get(url, headers=headers, proxies = self.proxies, timeout=60)
    # , 'accept-language': 'en,en-US;q=0.9'}
        headers.update({'user-agent': self.account.user_agent})
        resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=30, impersonate="safari15_5")
        logger.debug(resp.text)
        # logger.success(f"获取用户在线状态: {resp.text}")


        # await asyncio.to_thread()
        # return response.status_code


    


    # @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def get_location(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36", proxy_url:str=None, dc_token:str=None) -> DiscordOAuth:
    # https://discord.com/api/v9/oauth2/authorize?client_id=1310681717803061258&response_type=token&redirect_uri=https%3A%2F%2Fbless.network%2Fdashboard%2Fachievements&scope=identify%20guilds%20guilds.join 
    """
    获取Discord OAuth授权码
    """
    # url = "https://discord.com/api/v9/oauth2/authorize"
    url = "https://discord.com/api/v9/oauth2/authorize?client_id=1310681717803061258&response_type=token&redirect_uri=https%3A%2F%2Fbless.network%2Fdashboard%2Fachievements&scope=identify%20guilds%20guilds.join"

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en-US;q=0.7,en;q=0.6',
        'authorization': dc_token,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        # 'referer': 'https://discord.com/oauth2/authorize?client_id=1310681717803061258&response_type=token&redirect_uri=https://bless.network/dashboard/achievements&scope=identify%20guilds%20guilds.join',
        # 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user_agent,
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Asia/Shanghai',
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLUNOIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLz9kaXNjb3JkdG9rZW49TVRFeU1URTBPREkyTkRReU56Z3lNekkxTkEuR1k2MTc0Lm9RZ3hyblZGUHhXellhZ3dWQllXVVgxYXYxXzQ1RGsxV1R3MDZjIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vYmxlc3MubmV0d29yay8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJibGVzcy5uZXR3b3JrIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6NDE5NDM0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJjbGllbnRfbGF1bmNoX2lkIjoiNzRjMDMzODctYzAzNi00NzgzLWE0YTktYzk1ODA5OGQzZDAxIiwibGF1bmNoX3NpZ25hdHVyZSI6IjcwMzJlNzYwLTExNDktNDM1MC04YzU2LTVkMGJkNDYwMjM3NSIsImNsaWVudF9oZWFydGJlYXRfc2Vzc2lvbl9pZCI6IjUyYjc0NGJjLThiZTMtNDE1OS1iMTk2LWI3ZDliZjljYTBiMSIsImNsaWVudF9hcHBfc3RhdGUiOiJmb2N1c2VkIn0="
    }

    params = {
        "client_id": "1310681717803061258",
        "response_type": "token",
        "redirect_uri": "https://bless.network/dashboard/achievements",
        "scope": "identify guilds guilds.join"
    }

    data = {
        "permissions": "0",
        "authorize": True,
        "integration_type": 0,
        "location_context": {
            "guild_id": "10000",
            "channel_id": "10000",
            "channel_type": 10000
        },
        "dm_settings": {
            "allow_mobile_push": False
        }
        }

    try:
        resp = await asyncio.to_thread(requests.post, url=url, headers=headers, proxy=proxy_url, json=data, timeout=300, impersonate="safari15_5")
        logger.debug(resp.text)
        if resp.status_code == 200:
            logger.info(resp.json())
            if not resp.json().get('location'):
                raise Exception("获取OAuth授权码失败: 响应中缺少location字段")
            location = resp.json().get('location')
            access_token = location.split('&access_token=')[1].split('&expires_in')[0] if location else None
            return DiscordOAuth(location=location, code=access_token, status_code=resp.status_code)
        
        raise Exception(f"获取OAuth授权码时发生错误: {str(resp.text)}")

    except Exception as e:
        logger.error(f"获取OAuth授权码时发生错误: {str(e)}")
        raise Exception(f"获取OAuth授权码时发生错误: {str(resp.text)}")
