import asyncio
from typing import Any, Tuple
from better_proxy import Proxy
from curl_cffi.requests import AsyncSession
from loguru import logger
from curl_cffi import requests

CAPTCHA_SITE_KEY = "0x4AAAAAAA4zgfgCoYChIZf4"
PAGE_URL         = "https://app.nodego.ai"

# session = noble_tls.Session(client=Client.CHROME_120, random_tls_extension_order=True)
# if proxy:
#     session.proxies = {
#         "http": proxy,
#         "https": proxy
#     }

# session.timeout = 30


class TwoCaptchaSolver:
    BASE_URL = "https://api.2captcha.com"

    def __init__(self, api_key: str =None, proxy_str: str = None):
        if not proxy_str:
            proxy_str = "http://127.0.0.1:7891"
        if not api_key:
            raise Exception("api_key is required")
        self.api_key = api_key
        self.session = AsyncSession(impersonate="chrome124", verify=False)
        proxy = Proxy.from_str(proxy_str)
        self.proxy_url = proxy.as_url
        # self.session.proxies = {
        #     "http": proxy_url,
        #     "https": proxy_url
        # }
        # self.session.timeout = 30


    async def solve_turnstile(self, sitekey: str, page_url: str) -> Tuple[str, bool]:
        try:
            captcha_data = {
                "clientKey": self.api_key,
                "task": {
                    "type": "TurnstileTaskProxyless",
                    "websiteURL": page_url,
                    "websiteKey": sitekey,
                }
            }
            
            # resp = await self.session.post(
            #     f"{self.BASE_URL}/createTask", json=captcha_data
            # )
            resp = await asyncio.to_thread(requests.post, url=F"{self.BASE_URL}/createTask", proxy=self.proxy_url, json=captcha_data, timeout=120, impersonate="safari15_5") 
            resp.raise_for_status()
            data = resp.json()
            
            if data.get("errorId") == 0:
                return await self.get_captcha_result(data.get("taskId"), type="turnstile")
            logger.error(data.get("errorDescription"))
            raise Exception(data.get("errorDescription"))

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}", False
        finally:
            await self.session.close()


    async def get_captcha_result(
        self, task_id: int | str, type: str = "image"
    ) -> tuple[Any, bool, int | str] | tuple[str, bool, int | str] | tuple[str, bool]:
        try:
            for _ in range(20):
                # resp = await self.session.post(
                #     f"{self.BASE_URL}/getTaskResult",
                #     json={"clientKey": self.api_key, "taskId": task_id},
                # )
                payload = {"clientKey": self.api_key, "taskId": task_id}
                resp = await asyncio.to_thread(requests.post, url=F"{self.BASE_URL}/getTaskResult", proxy=self.proxy_url, json=payload, timeout=120, impersonate="safari15_5") 
                # resp = await asyncio.to_thread(resp.json)
                resp.raise_for_status()
                result = resp.json()
                if result.get("errorId") != 0:
                    return result.get("errorDescription"), False
                if result.get("status") == "ready":
                    if type == "image":
                        return result["solution"].get("text", ""), True
                    elif type == "turnstile":
                        return result["solution"].get("token", ""), True

                await asyncio.sleep(3)
            
        except Exception as e:
            return f"An unexpected error occurred: {e}", False, task_id
    
SOLVE_SEMAPHORE = asyncio.Semaphore(30)

async def solve_nodego_captcha(api_key: str = None, proxy_url: str ="http://127.0.0.1:7891"):
    """解决NodeGo网站的验证码"""
    async with SOLVE_SEMAPHORE:
        two_captcha_solver = TwoCaptchaSolver(api_key=api_key, proxy_str=proxy_url)
        captcha_token, success = await two_captcha_solver.solve_turnstile(
            sitekey="0x4AAAAAAA4zgfgCoYChIZf4",
            page_url="https://app.nodego.ai",
        )
        if not success:
            raise Exception("Failed to solve captcha")
        return captcha_token


# async def main():
#     """
#     演示如何使用 TwoCaptchaSolver 类解决 Turnstile 验证码
#     """
#     solver = TwoCaptchaSolver(api_key=, proxy="http://127.0.0.1:7891")
#     token, success = await solver.solve_turnstile(
#         sitekey=CAPTCHA_SITE_KEY,
#         page_url=PAGE_URL
#     )
#     if success:
#         print(f"验证码解决成功！令牌: {token}")
#     else:
#         print(f"验证码解决失败: {token}")


# if __name__ == "__main__":
#     asyncio.run(main())