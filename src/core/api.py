import asyncio
import random
from loguru import logger
from src.core.twitter_api import TwiiterOAuth_1
from database.models import Account
# from src.utils.p2p_utils import get_signature_sync
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_fixed
from curl_cffi import requests
from datetime import datetime

# from utils import get_signature



class ResultFormatter:
    """结果格式化器"""
    
    @staticmethod
    def format_success(title: str, message: str) -> str:
        return f"✅ {title}: {message}"
    
    @staticmethod
    def format_error(title: str, message: str) -> str:
        return f"❌ {title}: {message}"
    
    @staticmethod
    def format_info(title: str, message: str) -> str:
        return f"ℹ️  {title}: {message}"
    
    @staticmethod
    def format_warning(title: str, message: str) -> str:
        return f"⚠️  {title}: {message}"
    
    @staticmethod
    def create_separator(title: str = "") -> str:
        if title:
            return f"\n{'='*20} {title} {'='*20}"
        return f"\n{'='*50}"
    
    @staticmethod
    def format_summary(account_email: str, results: list) -> str:
        """格式化执行摘要"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success_count = sum(1 for r in results if "✅" in str(r))
        error_count = sum(1 for r in results if "❌" in str(r))
        
        # 构建详细结果列表
        detailed_results = "\n".join([f"  {result}" for result in results]) if results else "  无执行结果"
        
        summary = f"""
    {ResultFormatter.create_separator(f"执行摘要 - {account_email}")}
    🕒 执行时间: {timestamp}
    📊 总任务数: {len(results)}
    ✅ 成功任务: {success_count}
    ❌ 失败任务: {error_count}
    📈 成功率: {(success_count/len(results)*100):.1f}% (如果有任务的话)

    📋 详细执行结果:
    {detailed_results}
    {ResultFormatter.create_separator()}
    """
        return summary



# 自定义异常类（不被捕获）
class APIException(Exception):
    """自定义API异常，不会被捕获"""
    pass

class API():
    def __init__(self, account: Account):
        self.account = account

    @retry(stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=retry_if_exception(lambda e: hasattr(e, 'status_code') and e.status_code in (500, 502, 503, 504)),
        sleep=asyncio.sleep)  # 添加这一行使等待变为异步
    async def ping(self, pub_key: str, node: dict):
        logger.debug(f"开始执行ping......")
        try:
            # signature = await asyncio.to_thread(get_signature_sync(node.get("encrypted_key")))
            signature = await self.get_signature(node.get('encrypted_key'))
            url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/ping"
            payload = { "isB7SConnected": False }
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
                raise APIException(f"HTML响应错误: {text}")
            else:
                logger.debug(f"{self.account.email}---->{resp.text}")
            
            if resp.status_code == 200 and "ok" in resp.text:
                logger.success(resp.text)
                return ResultFormatter.format_success("PING", f"{pub_key[-15:]}... 成功")
            
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
            
        except APIException as e:
            return ResultFormatter.format_error("PING", f"{pub_key[-15:]}... 失败 - {str(e)}")
        except Exception as e:
            return ResultFormatter.format_error("PING", f"{pub_key[-15:]}... 异常 - {str(e)}")


    async def start_session(self, pub_key: str, node: dict):
        try:
            signature = await self.get_signature(node.get('encrypted_key'))
            # logger.success(f"生成的签名: {signature}")
            url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/start-session"
            payload = {}
            headers = {
                'accept': '*/*',
                'authorization': f'Bearer {self.account.bless_auth_token}',
                'cache-control': 'no-cache',
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
            #logger.debug(resp.text)
            if resp.status_code == 200 and "ok" in resp.text:
                return ResultFormatter.format_success("START SESSION", f"{pub_key[-15:]}... 启动成功")
            
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
            
        except APIException as e:
            return ResultFormatter.format_error("START SESSION", f"{pub_key[-15:]}... 启动失败 - {str(e)}")
        except Exception as e:
            return ResultFormatter.format_error("START SESSION", f"{pub_key[-15:]}... 启动异常 - {str(e)}")



    async def stop_session(self, pub_key: str, node: dict):
        try:
            signature = await self.get_signature(node.get('encrypted_key'))
            url = f"https://gateway-run.bls.dev/api/v1/nodes/{pub_key}/stop-session"
            payload = {}
            headers = {
                'accept': '*/*',
                'authorization': f'Bearer {self.account.bless_auth_token}',
                'cache-control': 'no-cache',
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
            # logger.debug(resp.text)
            if resp.status_code == 200 and "ok" in resp.text:
                logger.success(resp.text)
                return ResultFormatter.format_success("STOP SESSION", f"{pub_key[-15:]}... 停止成功")
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
            
        except APIException as e:
            return ResultFormatter.format_error("STOP SESSION", f"{pub_key[-15:]}... 停止失败 - {str(e)}")
        except Exception as e:
            return ResultFormatter.format_error("STOP SESSION", f"{pub_key[-15:]}... 停止异常 - {str(e)}")
    


    async def overview(self) -> int:
        try:
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
                allTimeTotalReward = data.get("allTimeTotalReward", 0)
                self.account.points = int(allTimeTotalReward)
                await self.account.save()
                return ResultFormatter.format_success("OVERVIEW", f"总积分: {self.account.points}")
            
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
            
        except APIException as e:
            return ResultFormatter.format_error("OVERVIEW", f"获取总览失败 - {str(e)}")
        except Exception as e:
            return ResultFormatter.format_error("OVERVIEW", f"获取总览异常 - {str(e)}")


    async def earnings(self) -> int:
        try:
            url = "https://gateway-run-indexer.bls.dev/api/v1/users/earnings"
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
                'sec-fetch-site': 'cross-site',
            }
            headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
            resp = await asyncio.to_thread(requests.get, url=url, headers=headers, proxy=self.account.proxy_url, timeout=20, impersonate="safari15_5")
            if resp.status_code == 200 and "totalReward" in resp.text:
                data = resp.json()
                last_three_data = data[-3:] if len(data) >= 3 else data
                
                if len(last_three_data) >= 3:
                    self.account.day_before_yesterday_points = int(last_three_data[0].get("totalReward", 0))
                    self.account.yesterday_points = int(last_three_data[1].get("totalReward", 0))
                    self.account.today_points = int(last_three_data[2].get("totalReward", 0))
                    
                    # 1/5 的概率执行保存操作
                    if random.randint(1, 5) == 1:
                        await self.account.save()
                    
                    return ResultFormatter.format_success("EARNINGS", 
                        f"前天:{self.account.day_before_yesterday_points}, "
                        f"昨天:{self.account.yesterday_points}, "
                        f"今天:{self.account.today_points}")
                else:
                    return ResultFormatter.format_warning("EARNINGS", "数据不足3天")
            
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
            
        except APIException as e:
            return ResultFormatter.format_error("EARNINGS", f"获取收益失败 - {str(e)}")
        except Exception as e:
            return ResultFormatter.format_error("EARNINGS", f"获取收益异常 - {str(e)}")
        


    async def get_signature(self, encrypted_key):
        try:
            url = "http://localhost:3000/signature"
            payload = {
                "encryptedKey": encrypted_key
            }
            headers = {
                'Content-Type': 'application/json'
            }
            resp = await asyncio.to_thread(requests.post, url=url, headers=headers, json=payload, timeout=20, impersonate="safari15_5")
            if resp.status_code == 200 and "success" in resp.text:
                data = resp.json()
                signature = data.get("signature")
                return signature
            else:
                raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
        except APIException as e:
            raise e
        except Exception as e:
            raise Exception("GET SIGNATURE", f"获取签名异常 - {str(e)}")
        



    async def get_socials(self, proxy_url: str = None):
        try:
            url = "https://gateway-run-indexer.bls.dev/api/v1/users/socials"

            payload = {}
            headers = {
                'accept': '*/*',
                'accept-language': 'en,en-US;q=0.9',
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
            if proxy_url:
                proxy_url= self.account.proxy_url
            resp = await asyncio.to_thread(requests.get, url=url, headers=headers, json=payload, timeout=30, impersonate="safari15_5", proxy=proxy_url)
            logger.debug(resp.text)
            if resp.status_code == 200 and ('discordConnected' in resp.text or 'xConnected' in resp.text):
                data = resp.json()
                discordConnected = data.get("discordConnected", False)
                xConnected = data.get("xConnected", False)
                self.account.is_dc_connected = discordConnected
                self.account.is_twitter_connected = xConnected
                await self.account.save()
                logger.success(resp.text)
                return
            logger.error(f"状态码: {resp.status_code}, 响应: {resp.text}")
            raise APIException(f"状态码: {resp.status_code}, 响应: {resp.text}")
        except APIException as e:
            logger.error(str(e))
            raise Exception(ResultFormatter.format_error("GET SOCIALS", f"获取社交账户状态失败 - {str(e)}"))
        


    
    async def bind_discord(self, proxy_url: str = None, code:str=None):
        """绑定Discord账号"""
        url = "https://bless.network/dashboard/api/discord/verify-user"
        payload = {
            "discordAccessToken": code,
            "gatewayAuthToken": self.account.bless_auth_token,
            "socialPlatform": "discord"
        }
        headers = {
            'host': 'bless.network',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': self.account.user_agent,
            'content-type': 'text/plain;charset=UTF-8',
            'accept': '*/*',
            'origin': 'https://bless.network',
            'referer': 'https://bless.network/dashboard/achievements',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i'
        }
        if not proxy_url:
            proxy_url = self.account.proxy_url
        resp = await asyncio.to_thread(requests.post, url=url, headers=headers, json=payload, timeout=30, impersonate="safari15_5", proxy=proxy_url)
        logger.debug(resp.text)
        logger.debug(resp.status_code)
        if 'DISCORD Connect Success' in resp.text:
            logger.success("Discord 绑定成功")
            self.account.is_dc_connected = True
            await self.account.save()
            return
        raise Exception("Discord 绑定失败")

    
    async def bind_twitter(self, code: str, proxy_url: str = None):
        try:
            logger.debug(f"开始绑定Twitter账号")
            """绑定Twitter账号"""
            url = "https://bless.network/dashboard/api/x/verify-user"
            
            payload = {
                "code": code,
                "gatewayAuthToken": f"{self.account.bless_auth_token}\n"
            }
            logger.success(payload)
            
            headers = {
                'host': 'bless.network',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'sec-ch-ua-platform': '"Windows"',
                'content-type': 'text/plain;charset=UTF-8',
                'accept': '*/*',
                'origin': 'https://bless.network',
                'referer': f'https://bless.network/dashboard/achievements?state=state&code={code}',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'priority': 'u=1, i'
            }
            headers.update({'user-agent': self.account.user_agent, 'accept-language': 'en,en-US;q=0.9'})
            if proxy_url:
                proxy_url= self.account.proxy_url
            resp = await asyncio.to_thread(requests.post, url=url, headers=headers, json=payload, timeout=30, impersonate="safari15_5", proxy=proxy_url)
            logger.debug(resp.text)

            if 'X Connect Success!' in resp.text:
                logger.success(f"绑定Twitter成功！")
                self.account.is_twitter_connected = True
                await self.account.save()
                return resp.json()
            logger.debug(F"执行绑定推特{resp.text}")
            # response = await self.session.post(url, headers=headers, json=payload)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.error(f"绑定Twitter失败: {str(e)}")
            raise Exception(f"绑定Twitter失败: {str(e)}")