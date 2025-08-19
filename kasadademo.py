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


def work_time(session, t , ua):
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
    spider_headers = {
        "Content-Type": "application/json"
    }
    url = 'https://sync.ez-captcha.com/createSyncTask'
    r = session.post(url, json=data, headers=spider_headers)
    return r.json()["solution"]["payload"]


def get_tl(session,ips_text, ua):
    data = {
        "clientKey": clientKey,
        "task": {
            "type": "KasadaTaskProxyless",
            "ua": f"{ua}",
            "ipsContent": ips_text,
            "lang": "zh",
            "bmsc": "",
            "domain": "arcteryx.com"
            # "domain": "mcprod.arcteryx.com"
        }
    }
    print(data)

    resp = session.post("https://sync.ez-captcha.com/createSyncTask", json=data)
    print(resp.text)
    ct = resp.json().get("solution").get("ct")
    dt = resp.json().get("solution").get("dt")
    tl = resp.json().get("solution").get("tl")
    tl = decode_base64(tl)
    return ct, dt, tl


def pass_test():
    session = requests.session()
    session.verify = False
    session.proxies = {
        "http": "http://127.0.0.1:7891",
        "https": "http://127.0.0.1:7891"
    }
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
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
    print(resp.session.cookies)
    ips_response = resp.text
    ct, dt, tl = get_tl(session, ips_response, ua)

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

    cd = work_time(session,st,ua)

    headers = {
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "x-kpsdk-cd": f"{cd}",
        "x-kpsdk-ct": f"{ct}",
        "x-is-checkout": "false",
        "sec-ch-ua-mobile": "?0",
        "user-agent": f"{ua}",
        "x-px-cookie": "_px2=eyJ1IjoiZDkzMTM5MjEtYjYxNi0xMWVlLTllMTMtMjI5YzExODE1YzlhIiwidiI6ImQ5MzEzYzdmLWI2MTYtMTFlZS05ZTEzLTUxNDRjMDA2NTc2MyIsInQiOjE3MDU1OTIyOTAzNDMsImgiOiJjZDQ1YzQwNDQzY2U2YWYyYWZhMWQzYmExNmIwMzhlOGYyYmIwOTA0ZjgxYmNiOGRlNDI0ZDAwMjJmNWM2NzEzIn0=",
        "content-type": "application/json",
        "store": "arcteryx_en",
        "x-jwt": "",
        "x-kpsdk-v": "j-0.0.0",
        "x-country-code": "ca",
        "sec-ch-ua-platform": "\"Windows\"",
        "accept": "*/*",
        "origin": "https://arcteryx.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://arcteryx.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
    }
    data = '{"query":"query gqlGetProductInventoryBySkus($productSkus: [String!]) { products(filter: { sku: { in: $productSkus } }, pageSize: 500) { items { name sku ...on ConfigurableProduct { variants { product { sku quantity_available } } } } } }","variables":{"productSkus":["X000006510"]}}'
    # Target API
    resp = session.post("https://mcprod.arcteryx.com/graphql", headers=headers,data=data)
    print(resp.text)


if __name__ == '__main__':
    pass_test()