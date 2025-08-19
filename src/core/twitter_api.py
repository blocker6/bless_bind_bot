import asyncio
from dataclasses import dataclass
import json
import os
import re
import ssl
# import traceback
from urllib.parse import parse_qs, urlparse
import aiohttp
import httpx
# import requests
# from fake_useragent import UserAgent
# from utils.RandomAcceptLanguage import RandomAcceptLanguage
from loguru import logger
import requests
from tenacity import retry, stop_after_attempt, wait_exponential, wait_fixed
from tenacity import before_log, retry, retry_any, retry_if_exception, stop_after_attempt, wait_fixed, retry_if_exception_type
from bs4 import BeautifulSoup

# from database.models import Account  # 添加BeautifulSoup导入


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
    
    # Find a <script> tag whose text contains `window.__INITIAL_STATE__`
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


def setup_retry_decorator():
    return retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),  # 改为指数退避等待
        retry=retry_any(
            retry_if_exception_type((
                aiohttp.ClientError,        # aiohttp客户端错误
                httpx.TransportError,       # httpx传输错误
                asyncio.TimeoutError,       # 异步超时错误
                requests.exceptions.RequestException,  # requests库异常
                ssl.SSLError,               # SSL错误
                ConnectionResetError,       # 连接重置错误
                OSError                     # 操作系统错误
            )),
            retry_if_exception(lambda e: any(
                err in str(e) for err in [
                    "OPENSSL_internal:WRONG_VERSION_NUMBER",
                    "Connection reset by peer",
                    "Remote end closed connection"
                ]
            ))  # 扩展常见网络错误关键词
        ),
        reraise=True,
        before=before_log(logger, "INFO")
    )





@dataclass
class TwiiterOAuth:
    oauth_token: str
    oauth_verifier: str
    redirect_url: str

class TwiiterOAuth_1:
    def __init__(self, auth_token: str = None, user_agent: str = None, proxy_url: str = None):


        # if not user_agent:
        #     raise ValueError("user_agent is required")
        # if not proxy_url:
        #     raise ValueError("proxy_url is required")
        
        self.proxy_url = proxy_url
        self.twitter_http = None

        #proxies = {'http://': proxy_url, 'https://': proxy_url}
        
        # httpx的代理格式与requests不同
        # httpx代理格式应该是 "http://" 或 "https://" 而不是带冒号的 "http://:" 和 "https://:"
        self.http = httpx.AsyncClient(verify=False, timeout=50, proxy=proxy_url)
        self.user_agent = user_agent
                                      
        self.ct0 = ''
        self.oauth_token = ''
        self.auth_token = auth_token
        self.http.cookies.update({'auth_token': self.auth_token})
        self.http.headers.update({"user-agent": self.user_agent, "accept-language": "en-US,en;q=0.9"})


    # @setup_retry_decorator()
    async def login_1(self):
        try:
            print(self.auth_token)
            if not self.auth_token:
                raise ValueError("auth_token is required")
            headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "cache-control": "no-cache",
                    "pragma": "no-cache",
                    "priority": "u=0, i",
                    "upgrade-insecure-requests": "1",
                }
            url = "https://twitter.com/"
            # print(self.http.headers)
            self.http.headers.update(headers)
            resp = await self.http.get(url)
            logger.debug(resp.text[:60])
            self.ct0 = resp.cookies.get("ct0", None)
            if self.ct0 and len(self.ct0) > 120:
                self.http.headers.update({'x-csrf-token': self.ct0})
                logger.success(f"成功获取推特ct0:{self.ct0}")
                return TwitterResult.success()
            else:
                logger.error(f"未获取到twitter_token")
            logger.error(f"获取ct0失败.....")
            raise Exception("获取ct0失败.....")
        except Exception as e:
            logger.error(f"出现异常---->{str(e)}")
            raise Exception("出现异常.....")

        #print(res.text)
        # # exit()
        # if res.status_code == 200 and 'https://twitter.com/x/migrate?tok=' in res.text and 'document.location' in res.text:
        #     return TwitterResult.account_dead()
        # initial_state = extract_initial_state(res.text)
        # login_success = is_logged_in(initial_state)
        # if login_success:
        #     self.ct0 = res.cookies.get("ct0")
        #     if self.ct0 and len(self.ct0) > 120:
        #         self.http.headers.update({'x-csrf-token': self.ct0})
        #         logger.success(f"成功获取推特ct0:{self.ct0}")
         #       return TwitterResult.success()
        
        # return TwitterResult.login_failed(resp.text)
     
        
    @setup_retry_decorator()
    async def get_authenticity_token_2(self, oauth_token: str, oauth_token_secret: str) -> str:
        self.oauth_token = oauth_token
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://api.x.com/",
            "upgrade-insecure-requests": "1"
        }
        url = f"https://api.twitter.com/oauth/authorize?oauth_token={oauth_token}&oauth_token_secret={oauth_token_secret}&oauth_callback_confirmed=true"
        response = await self.http.get(url, headers=headers)
        # logger.success(response.text)
        if "authenticity_token" in response.text:
            logger.success(f"获取authenticity_token成功,响应长度{len(response.text)}")
            pattern = r'name="authenticity_token"\s+type="hidden"\s+value="(.+?)"'
            match = re.search(pattern, response.text)
            authenticity_token = match[1]
            return authenticity_token
        logger.error(response.text[:60])
        raise Exception(response.text[:60])


    @setup_retry_decorator()
    async def authorize_3(self, authenticity_token: str) -> TwiiterOAuth:
        """
        授权Twitter账号
        Args:
            authenticity_token: 认证token
            oauth_token: oauth token
        Returns:
            授权结果
        """
        url = "https://x.com/oauth/authorize"
        
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://api.x.com",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": "https://api.x.com/",
            "upgrade-insecure-requests": "1",
        }

        data = {
            "authenticity_token": authenticity_token,
            "oauth_token": self.oauth_token
        }

        resp = await self.http.post(url, headers=headers, data=data)
        logger.success(f"Twitter授权成功,响应正文长度:{len(resp.text)}")
        if resp.status_code == 200:
            # 提取重定向URL
            pattern = r'http-equiv="refresh" content="0;url=([^"]+)"'
            match = re.search(pattern, resp.text)
            if match:
                redirect_url = match.group(1)
                logger.success(f"成功获取重定向URL:{redirect_url}")
                # 从重定向URL中解析oauth_token和oauth_verifier
                oauth_verifier = redirect_url.split('&amp;oauth_verifier=')[1]
                if oauth_verifier:
                    logger.success(f"成功提取oauth_token和oauth_verifier: {self.oauth_token}, {oauth_verifier}")
                    return TwiiterOAuth(oauth_token=self.oauth_token, oauth_verifier=oauth_verifier, redirect_url=redirect_url)
                else:
                    logger.error("未能从URL中提取oauth_token和oauth_verifier")
                    raise Exception("未能从URL中提取oauth_token和oauth_verifier")
        
        logger.error(resp.text[:60])
        raise Exception(resp.text[:60])
                

    @setup_retry_decorator()
    async def follow(self, username):
        """异步执行关注操作"""
        url = "https://x.com/i/api/1.1/friendships/create.json"
        
        # 动态构建请求参数
        payload = {
            'include_profile_interstitial_type': '1',
            'include_blocking': '1',
            'include_blocked_by': '1',
            'include_followed_by': '1',
            'include_want_retweets': '1',
            'include_mute_edge': '1',
            'include_can_dm': '1',
            'include_can_media_tag': '1',
            'include_ext_is_blue_verified': '1',
            'include_ext_verified_type': '1',
            'include_ext_profile_image_shape': '1',
            'skip_status': '1',
            'user_id': '1793256796083412992'  # 保持硬编码或改为参数传入
        }

        # 使用实例已有的HTTP客户端和headers
        headers = {
            'x-csrf-token': self.ct0,
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'referer': f'https://x.com/intent/follow?screen_name={username}',
            'content-type': 'application/x-www-form-urlencoded',
            #QC/umYCgjnBRgfNJX2xi44Md5qGdhqSSixJyk3cOJRsgh19QgJB+HwblRlz3bbzcdANeHkPhpwdMcNA9gih/ceU2jPkmQw
            # 9DkRRJWBRU2mvBEW5ujkBsrZ/sVjA45S5Zoh2MWgC2u6mPAr1TCHF00Y6C3ysUWhoZfcqvfyyetrJU4ylwuheqvIrs8f9w

            'x-client-transaction-id': '9DkRRJWBRU2mvBEW5ujkBsrZ/sVjA45S5Zoh2MWgC2u6mPAr1TCHF00Y6C3ysUWhoZfcqvfyyetrJU4ylwuheqvIrs8f9w',
        }
        try:
            logger.debug(f"尝试关注用户 @{username}")
            response = await self.http.post(url, data=payload, headers=headers)
            
            if response.status_code != 200:
                logger.error(f"{self.auth_token} 关注失败 | 用户: @{username} | 状态码: {response.status_code}")
                raise Exception(f'关注失败: {response.text}')
            
            logger.success(f"成功关注用户 @{username}")
            return response.json()
            
        except Exception as e:
            logger.error(f"关注操作异常 | 用户: @{username} | 错误: {str(e)}")
            raise Exception(f'关注错误: {str(e)}')


    def create_twitter_http_session(self):
        """创建新的OAuth会话"""
        self.twitter_http = httpx.AsyncClient(verify=False, timeout=50, proxy=self.proxy_url)
                                      
        self.oauth_token = ''
        self.auth_token = self.auth_token
        # self.twitter_http.cookies = self.http.cookies

        self.twitter_http.headers.update({"user-agent":  self.user_agent, 
                                  "accept-language": "en-US,en;q=0.9"})

        # 配置代理
        self.twitter_http.proxies = {
            'http': self.proxy_url,
            'https': self.proxy_url
        }

        # 设置固定cookies和headers
        self.twitter_http.cookies.update({
            'auth_token': self.auth_token,
            'ct0': self.ct0
        })
        
        headers = {
            'x-csf-token': self.ct0,
        }
        
        self.twitter_http.headers.update(headers)
        # self.session = session
        # session.headers.update(headers)
        # return session



    async def twitter_http_get_auth_code(self):
        # if self.twitter_http is None:
        #     raise ValueError("twitter_http is not initialized")
        """获取OAuth授权码"""
        url ="https://twitter.com/i/api/2/oauth2/authorize?client_id=dGdQVjlfLUdiUVJPZnpYSzQ0aF86MTpjaQ&code_challenge=test&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fbless.network%2Fdashboard%2Fachievements&response_type=code&scope=follows.write%20users.read%20tweet.read&state=state"
        
        self.http.headers.update(
            headers = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    'sec-ch-ua-platform': '"Windows"',
                    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                    # 'x-client-uuid': '69acc7cd-ae37-49ce-87e3-6f1058feae92',
                    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
                    'x-twitter-client-language': 'en',
                    'sec-ch-ua-mobile': '?0',
                    'x-twitter-active-user': 'no',
                    'x-client-transaction-id': 'P1ijD/BmUjKJ/mfR+w0qgKVIAAexg0QNB0r57Ir4z7yFaLCqMG28IqkTaVdYoKME1Ox+WDyTPthESy5mr3JGHCRP+wPDPA',
                    'x-twitter-auth-type': 'OAuth2Session',
                    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
                    'accept': '*/*',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://x.com/i/oauth2/authorize?state=state&code_challenge_method=plain&code_challenge=test&client_id=dGdQVjlfLUdiUVJPZnpYSzQ0aF86MTpjaQ&scope=follows.write%20users.read%20tweet.read&response_type=code&redirect_uri=https%3A%2F%2Fbless.network%2Fdashboard%2Fachievements',
                    'accept-encoding': 'gzip, deflate, br, zstd',
                    'accept-language': 'en-US,en;q=0.9',
                    'priority': 'u=1, i',
                })
        try:
            response = await self.http.get(url=url)
            response.raise_for_status()
            return response.json().get('auth_code')
        except Exception as e:
            logger.error(f"获取OAuth code失败: {str(e)}")
            raise



    @setup_retry_decorator()
    async def authorize_oauth2(self, code: str):
        """OAuth2授权确认"""
        # url = "https://x.com/i/api/2/oauth2/authorize"
        url = "https://twitter.com/i/api/2/oauth2/authorize"

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://twitter.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://twitter.com/i/oauth2/authorize?state=state&code_challenge_method=plain&code_challenge=test&client_id=dGdQVjlfLUdiUVJPZnpYSzQ0aF86MTpjaQ&scope=follows.write%20users.read%20tweet.read&response_type=code&redirect_uri=https%3A%2F%2Fbless.network%2Fdashboard%2Fachievements',
            # 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'x-client-transaction-id': 'qtcdHZXEzrF9oXQWYKg984T2JLXdwCfc38SIXNnfHtYf1yqlRVZ2Hj3j4TxNEUiHs9Bdja7uo8q/og1dRN0f6AJ31QQdqQ',
            'x-csrf-token': self.ct0,
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            # 'Cookie': 'guest_id_marketing=v1%3A175265222211462225; guest_id_ads=v1%3A175265222211462225; guest_id=v1%3A175265222211462225; __cf_bm=lO2rQvhzgVXqoRRDp8nH2Zo_pNulEPVp4L1kvEwj3Cg-1752652222-1.0.1.1-tfSOcrUn6ztv5KgX9nNcxFZ.mMZqGeFnDFJJxRMIhZd1yS3vLET0j3pisphA5FmGhBsGL30aTUMAkWGaHvNlt6eW5U1jUMgWIOGOSrn65ks; personalization_id="v1_VuSeF0VeLJTgrhUHB1cbsw=="; gt=1945390536380309920; external_referer=padhuUp37zhS73Kl8dCzIr5TOsDU4wuk|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCLebNhKYAToMY3NyZl9p%250AZCIlMzViZWJmMTVkNzU5OThiMDkyYmViYWJiNGYxYTI4MDc6B2lkIiVmMzMx%250AMzA3MWRkMjFmM2M1N2VkM2JlNjFhZGI4MTg3ZA%253D%253D--354646657b4137a4e301e817f30c3b504c7bffd5; kdt=jgB4MGrDLLMV7SKEdNmXEbKllRr4sBzegTJFi5fi; auth_token=76dfaadf5ea2b983caa91160bea1afa0ba69a963; ct0=e3b247f97b2075af49a7f41ebc67adfc291d01db58fe848c75517c916a053aa4c2fa083bae1ad26a68c354cb1a0d2086fc88d0fb739fb4641e00bcd98267cbc5a4463df64367bc50ff03125593e68310; twid=u%3D1332064407749234690; att=1-qQfbmvWdHT3tYfssLAcIa60kXbFoJxFLf31Brx0b; lang=en; guest_id=v1%3A172241560998354170; guest_id_ads=v1%3A172241560998354170; guest_id_marketing=v1%3A172241560998354170; personalization_id="v1_lcpVN9BY6NByX4HDTCb+kg=="'
            }
        
        payload = f'approval=true&code={code}'

        try:
            response = await self.http.post(url, headers=headers, data=payload)
            logger.debug(response.text)
            logger.success(f"OAuth2授权成功,响应正文长度:{len(response.text)}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"OAuth2授权失败: {str(e)}")
            raise


async def test():
    twiiter_oauth = TwiiterOAuth_1(auth_token="7fe5296f2e0c6abbdf800131380699bad7a749a8",
                                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                                    proxy_url="http://127.0.0.1:7891")
    await twiiter_oauth.login_1()
    # twiiter_oauth.create_twitter_http_session()
    auth_code = await twiiter_oauth.twitter_http_get_auth_code()
    print(auth_code)
    # logger.success(auth_code)
    data = await twiiter_oauth.authorize_oauth2(auth_code)
    


if __name__ == "__main__":
    asyncio.run(test())