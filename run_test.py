import asyncio
import json
import random
import sys
from loguru import logger
from better_proxy import Proxy
# from curl_cffi.requests import AsyncSession
from curl_cffi import requests

# Windows兼容性
if sys.platform == 'win32':
    from asyncio import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

def load_config(config_path: str = "arc_config.json") -> tuple:
    """读取配置文件，获取第一个URL"""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            product_urls = config.get("product_url_list", [])
            first_url = product_urls[0] if product_urls else None
            return first_url, config.get("proxy_file_path", "proxies.txt")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Config load failed: {str(e)}")
        return None, "proxies.txt"

def load_proxies(file_path: str) -> list[str]:
    """读取代理列表"""
    try:
        with open(file_path, 'r') as f:
            return [Proxy.from_str(line.strip()).as_url for line in f if line.strip()]
    except FileNotFoundError:
        logger.error(f"Proxy file {file_path} not found")
        return []

async def single_request():
    """发送单次请求"""
    # 加载配置
    # product_url, proxy_path = load_config('arc_config.json')
    # if not product_url:
    #     logger.error("未找到产品URL")
    #     return
    
    # # 加载代理
    # proxy_list = load_proxies(proxy_path)
    # if not proxy_list:
    #     logger.error("未找到可用代理")
    #     return
    
    # 请求头
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }
    
    try:
        # 选择随机代理
        resp = await asyncio.to_thread(requests.get, "https://arcteryx.com/us/en/shop/womens/norvan-ld-4-gtx-shoe-9617", headers=headers, proxy="http://127.0.0.1:7891")
        



















        resp.raise_for_status()
        
        logger.success(f"请求成功! 状态码: {resp.status_code}")
        logger.info(resp.cookies)
        print(resp.text)
        for cookie in resp.cookies:
            logger.info(cookie)
        #await session.close()
        
    except Exception as e:
        logger.error(f"请求失败: {e}")

if __name__ == "__main__":
    asyncio.run(single_request())
