import asyncio
from typing import Tuple
import curl_cffi
import requests
import json








import base64
import re
import requests
import urllib3
import random
import time
urllib3.disable_warnings()
clientKey = "31709b3d4b374795bab8dcb99cdac580220519"
# Base64 decode
def decode_base64(encoded):
    decoded = base64.b64decode(encoded)
    return decoded


def work_time(t , ua):
    work_t = int(time.time() * 1000)
    data = {
        "clientKey": clientKey,
        "task": {
            "type": "KasadaWorkTimeTaskProxyless",
            "st": f"{t}",
            "domain": "arcteryx.com",
            "userAgent": f"{ua}",
            "workTime": f"{work_t}"
        }
    }
    print(data)
    spider_headers = {
        "Content-Type": "application/json"
    }
    url = 'https://sync.ez-captcha.com/createSyncTask'
    # res = await asyncio.to_thread(curl_cffi.requests, url, json=data, headers=spider_headers)
    res = requests.post(url, json=data, headers=spider_headers)
    # r = session.post(url, json=data, headers=spider_headers)
    return res.json()["solution"]["payload"]


def get_tl(ips_text, ua):
    data = {
        "clientKey": clientKey,
        "task": {
            "type": "KasadaTaskProxyless",
            "ua": f"{ua}",
            "ipsContent": ips_text,
            "lang": "zh",
            "bmsc": " ",
            "domain": "arcteryx.com"
            # "domain": "mcprod.arcteryx.com"
        }
    }
    print(data)
    spider_headers = {
        "Content-Type": "application/json"
    }
    url  = 'https://sync.ez-captcha.com/createSyncTask'
    # resp = session.post(url, json=data)
    # resp = await asyncio.to_thread(curl_cffi.requests, url, json=data)
    resp = requests.post(url, json=data, headers=spider_headers)
    print(resp.text)
    ct = resp.json().get("solution").get("ct")
    dt = resp.json().get("solution").get("dt")
    tl = resp.json().get("solution").get("tl")
    tl = decode_base64(tl)
    print(ct, dt, tl)
    return ct, dt, tl


def get_ips_response(ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", proxy_url= "http://127.0.0.1:7891"):
    session = requests.session()
    session.verify = False
    session.proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://arcteryx.com/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "iframe",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "upgrade-insecure-requests": "1",
        "user-agent": f"{ua}"
    }
    resp = session.get("https://arcteryx.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-1.1.0",headers=headers)
    im = re.findall('x-kpsdk-im=(.*?)">', resp.text)
    im = im[0]
    src = re.findall('<script src="(.*?)">', resp.text)
    ips_url = 'https://mcprod.arcteryx.com' + src[0].replace('amp;', '')
    print(ips_url)
    headers = {
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": f"{ua}",
        "sec-ch-ua-platform": "\"Windows\"",
        "accept": "*/*",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-dest": "script",
        "referer": "https://arcteryx.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-1.1.0",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
    }
    resp = session.get(ips_url, headers=headers)
    ips_response = resp.text
    print(ips_response)
    ct, dt, tl = get_tl(ips_response, ua)
    headers = {
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "x-kpsdk-im": f"{im}",
        "x-kpsdk-ct": f"{ct}",
        "sec-ch-ua-mobile": "?0",
        "user-agent": f"{ua}",
        "content-type": "application/octet-stream",
        "x-kpsdk-dt": f"{dt}",
        "x-kpsdk-v": "j-0.0.0",
        "sec-ch-ua-platform": "\"Windows\"",
        "accept": "*/*",
        "origin": "https://mcprod.arcteryx.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://arcteryx.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-1.1.0",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
    }
    resp = session.post("https://arcteryx.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/tl", headers=headers, data=tl)
    st = resp.headers.get("x-kpsdk-st")
    ct = resp.headers.get("x-kpsdk-ct")
    cd = work_time(session,st, ua)
    return cd, ct, ua




def send_adyen_save_state_request():
    """
    发送Adyen保存状态数据的GraphQL请求到Arc'teryx API
    """    
    # API端点
    url = "https://arcteryx.com/api/mcgql"
    # 请求头
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://arcteryx.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://arcteryx.com/us/en/checkout/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'arcteryx_en',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-country-code': 'us',
        'x-is-checkout': 'true',
        'x-jwt': '',
        'x-kpsdk-cd': '{"workTime":1751193175107,"id":"7438f082c28928d4d5ff45e8da2a807a","answers":[1,8],"duration":85.7,"d":554,"st":1751188878228,"rst":1751188878782}',
        'x-kpsdk-ct': '0E2d9wTp6pf4Zq4ofHglPKOhr2rfy7rpYwiOpeHID1ZKjm1q7zmqeZHhUZOMm5bBBykVtRt8eoNEN1bWbOlBjwJXpZ43G8bEgX2AOugjn0tzWPNuPnFaUB2sbRro0oiEpOPTbmolKZKItDRJzSXaXtW3JZED0x8i1H831q5Q',
        'x-kpsdk-v': 'j-1.1.0'
    }
    
    # GraphQL请求数据
    payload = {
        "query": "mutation adyenSaveStateData($stateData: String!, $cartId: String!) { adyenSaveStateData(stateData: $stateData, cartId: $cartId) { stateDataId } }",
        "variables": {
            "stateData": '{"paymentMethod":{"type":"giftcard","brand":"svs","encryptedCardNumber":"","encryptedSecurityCode":"eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.pjNuN-b-tMc1o_Xh8JQVaYHT-GUPAZo9cIzGzT9Y10wpTqFDshRiZZHDbcYojMSQsfkUT6SrwfxZai_pPRUUdHEbtTvSJzN5PewEKBAh8nEsHkeTTGfSzTa4c4lpgiuIBcOIm4fc-TXYQWs0Z_P5IqMtp4vRH8Ph38_n9Hac-mUkuytB4h9rDVGfR27nTbFn3e7gA2XR-PV6kFebYYQ_K2rqWfCJLCMrk_-h5PJtf7kgU67K_gHkT5UxNXjj4tef7nU8UVi7DXSkx15UW4UTUNV9xuMVWejWE8G0ycsvi8BhW6tH0Hj4kktK6erP36jg6sUaoSEz9JMnggGqbZP3rQ.Io-MO94ogD1tcvRtJVysnw.nppJyAk25C2ZGEC6Vbo8oPI36Xf1Ax02mZai2xLq9BlAGy5N3fOVt9YNuBUbEXAO10M9JTaICehQDQ6yM6elOw.PMZcX0onCqPO56Hklk-3r2Ok12AJmI9YTGrtINjiWPI"},"giftcard":{"pspReference":"LVX8RT48NR2S39F6","resultCode":"Success","balance":{"currency":"USD","value":28167},"title":"SVS"}}',
            "cartId": "OjMXueUso748doGRSvsmTo89gVO7swoI"
        }
    }
    try:
        # 发送POST请求
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,  # 使用json参数自动设置Content-Type和序列化数据
            timeout=30  # 设置超时时间
        )

        # 检查响应状态
        response.raise_for_status()
        
        # 返回JSON响应
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
        return None



async def run():
    ips_response = await asyncio.to_thread(get_ips_response)
    print(ips_response)


# 使用示例
if __name__ == "__main__":
    asyncio.run(run())
