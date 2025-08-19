import asyncio
from dataclasses import dataclass
import json
import re
from urllib.parse import parse_qs, urlparse
from curl_cffi import AsyncSession
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential, wait_fixed
from tenacity import before_log, retry, retry_any, retry_if_exception, stop_after_attempt, wait_fixed, retry_if_exception_type
from bs4 import BeautifulSoup  # 添加BeautifulSoup导入

import httpx
def to_json(obj):
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=True)




class UserNotFound(Exception):
    def __init__(self):
        super().__init__('User not found')

@dataclass
class TwitterResult:
    ok: bool
    code: str
    msg: str

    @staticmethod
    def success():
        return TwitterResult(ok=True, code="SUCCESS", msg="推特登录成功")

    @staticmethod
    def error(code: str, msg: str):
        return TwitterResult(ok=False, code=code, msg=msg)
    
    @staticmethod
    def account_dead():
        return TwitterResult.error("ACCOUNT_DEAD", "推特账号已死")
    
    @staticmethod
    def login_failed(msg: str):
        return TwitterResult.error("LOGIN_FAILED", f"推特登录失败: {msg}")




def is_logged_in(initial_state_json: dict) -> bool:
    # 1. 在 session 中找 user_id
    session = initial_state_json.get('session', {})
    user_id = session.get('user_id')
    if not user_id:
        return False
    
    # 2. 在 entities.users.entities 里是否有对应 user_id
    try:
        user_entities = initial_state_json['entities']['users']['entities']
        # 只要这里能找到 user_id 且信息较为丰富，一般可判定已登录
        if user_id in user_entities:
            return True
    except KeyError:
        pass
    
    return False



def extract_initial_state(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', string=re.compile(r'window\.__INITIAL_STATE__'))
    if not script_tag:
        raise ValueError("Could not find script tag containing window.__INITIAL_STATE__")
    text = script_tag.string
    pattern = r"window\.__INITIAL_STATE__=(\{.*?\});"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise ValueError("Could not extract JSON object from script text.")
    json_str = match.group(1)  # The entire {...} part
    # Now parse that JSON into a Python object.
    data = json.loads(json_str)
    return data






@dataclass
class TwiiterOAuth:
    oauth_token: str
    oauth_verifier: str
    redirect_url: str

class TwiiterOAuth_1:
    def __init__(self, auth_token: str = None, user_agent: str = None, proxy_url: str = None):

        if not user_agent:
            raise ValueError("user_agent is required")
        if not proxy_url:
            raise ValueError("proxy_url is required")
    
        self.proxy_url = proxy_url
        self.twitter_http = None
        self.session = httpx.AsyncClient(verify=False, timeout=50, proxy=proxy_url)

        self.ct0 = ''
        self.auth_token = auth_token
        self.session.cookies.update({'auth_token': auth_token})
        self.session.headers.update({"user-agent": user_agent, "accept-language": "en-US,en;q=0.9"})

    # @setup_retry_decorator()
    async def login_1(self):
        try:
            if not self.auth_token:
                raise ValueError("auth_token is required")
            headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "cache-control": "no-cache",
                    "pragma": "no-cache",
                    "priority": "u=0, i",
                    "upgrade-insecure-requests": "1",
                }
            url = "https://x.com/"
            # print(self.session.headers)
            # self.session.headers.update(headers)
            res = await self.session.get(url, headers=headers)
            logger.debug(res.text[:60])
            self.ct0 = res.cookies.get("ct0", None)
            if self.ct0 and len(self.ct0) > 120:
                self.session.headers.update({'x-csrf-token': self.ct0})
                logger.success(f"成功获取推特ct0:{self.ct0}")
                return TwitterResult.success()
            
            return TwitterResult.login_failed(res.text)
        except Exception as e:
            logger.error(f"获取ct0失败.....{str(e)}")
            raise Exception("获取ct0失败.....")
     
        
    async def get_html(self):
        url = "https://x.com/i/oauth2/authorize?response_type=code&client_id=eGswQzA2STlwRWJmRUxwUlN5Vmw6MTpjaQ&redirect_uri=https%3A%2F%2Fapp.nodego.ai%2Fconnect-x&scope=tweet.read+users.read&state=state&code_challenge=challenge&code_challenge_method=plain"
        payload = {}
        headers = {
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://app.nodego.ai/',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'priority': 'u=0, i',
        }

        res = await self.session.get(url, headers=headers, params=payload)

        print(len(res.text))


    async def get_auth_code(self) -> str:
        """异步获取OAuth授权码"""
        # 动态构建请求参数
        url = "https://x.com/i/api/2/oauth2/authorize?client_id=eGswQzA2STlwRWJmRUxwUlN5Vmw6MTpjaQ&code_challenge=challenge&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fapp.nodego.ai%2Fconnect-x&response_type=code&scope=tweet.read%20users.read&state=state"
        # 使用实例已有的headers和cookies
        headers = {
            'host': 'x.com',
            'sec-ch-ua-platform': '"Windows"',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-twitter-client-language': 'en',
            'sec-ch-ua-mobile': '?0',
            'x-twitter-active-user': 'yes',
            'x-client-transaction-id': 'udyvQR3T2t4B1mtQPyexDcr+iLOSQ4T76D98QAsf5AzPPuul5Fdw8yoyB44qw0l6WRLeLLq6HtSckZb9xi/b27P1Kzidug',
            'x-twitter-auth-type': 'OAuth2Session',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://x.com/i/oauth2/authorize?response_type=code&client_id=eGswQzA2STlwRWJmRUxwUlN5Vmw6MTpjaQ&redirect_uri=https%3A%2F%2Fapp.nodego.ai%2Fconnect-x&scope=tweet.read+users.read&state=state&code_challenge=challenge&code_challenge_method=plain',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'priority': 'u=1, i',
            }
        try:
            response = await self.session.get(
                url, headers=headers
            )
            response.raise_for_status()
            return response.json().get('auth_code')
            
        # except httpx.HTTPStatusError as e:
        #     logger.error(f"获取授权码失败 HTTP错误: {e.response.status_code}")
        #     raise
        # except json.JSONDecodeError:
        #     logger.error("响应解析失败")
        #     raise
        except Exception as e:
            logger.error(f"未知错误: {str(e)}")
            raise


    async def authorize(self, auth_code: str) -> str:
        """异步处理OAuth2授权确认"""
        url = "https://x.com/i/api/2/oauth2/authorize"
        # 动态构建请求参数
        payload = f'approval=true&code={auth_code}'
        # 使用实例已有的认证信息
        headers = {
            'sec-ch-ua-platform': '"Windows"',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-twitter-client-language': 'en',
            'sec-ch-ua-mobile': '?0',
            'x-twitter-active-user': 'yes',
            'x-client-transaction-id': 'QSRXueUrIib5LpOox99J9TIGcEtqu3wDEMeEuPPnHPQ3xhNdHK+IC9LK/3bSO7GCofIm1ELI6K4YhDQeRcy8qc9ZF22bQg',
            'x-twitter-auth-type': 'OAuth2Session',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://x.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://x.com/i/oauth2/authorize?response_type=code&client_id=eGswQzA2STlwRWJmRUxwUlN5Vmw6MTpjaQ&redirect_uri=https%3A%2F%2Fapp.nodego.ai%2Fconnect-x&scope=tweet.read+users.read&state=state&code_challenge=challenge&code_challenge_method=plain',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'priority': 'u=1, i'
        }
        # 使用异步客户端发送请求
        resp = await self.session.post(url, headers=headers, data=payload)
        resp.raise_for_status()
            # 新增代码：解析重定向URL
        if 'redirect_uri' in resp.text:
            redirect_uri = resp.json().get('redirect_uri')
            code = redirect_uri.split('&code=')[1]
            return code
            # return redirect_uri
        logger.error(resp.text)
        raise Exception("获取重定向URL失败")
    





async def main():
    # 初始化参数（需要替换为实际值）
    auth_token = "your_auth_token"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
    proxy_url = "http://127.0.0.1:7891"

    try:
        # 初始化客户端
        client = TwiiterOAuth_1(
            auth_token=auth_token,
            user_agent=user_agent,
            proxy_url=proxy_url
        )
        # 第一步：登录获取ct0
        login_result = await client.login_1()
        if not login_result.ok:
            logger.error(f"登录失败: {login_result.msg}")
            return login_result
        # 第二步：获取授权码
        auth_code = await client.get_auth_code(
        )
        # 第三步：授权确认
        final_code = await client.authorize(auth_code)
        
        logger.success(f"OAuth流程完成，最终授权码: {final_code}")
        return TwitterResult.success()

    except Exception as e:
        logger.error(f"OAuth流程异常: {str(e)}")
        return TwitterResult.error(
            "OAUTH_FAILED",
            f"OAuth授权流程失败: {str(e)}"
        )

# 使用示例
if __name__ == "__main__":
    asyncio.run(main())