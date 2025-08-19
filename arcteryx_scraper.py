import asyncio
from zoneinfo import ZoneInfo

from loguru import logger
from collections import defaultdict
from dataclasses import dataclass, field
import datetime
import json
import random
import sys
import time
from typing import List
from better_proxy import Proxy
from bs4 import BeautifulSoup
import requests
import pandas as pd
from dataclasses import dataclass, asdict
from curl_cffi.requests import AsyncSession
from tenacity import retry, stop_after_attempt, wait_fixed
# For Windows compatibility
if sys.platform == 'win32':
    from asyncio import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# @dataclass
# class ColorGroupAnalysis:
#     color_name: str
#     total_skus: int
#     available_sizes: list[str]
#     average_inventory: float
#     stock_distribution: dict

@dataclass
class ColorGroupAnalysis:
    color_name: str
    available_sizes: list[str]  # 有货尺码
    price: str                  # 价格
    total_inventory: int        # 该颜色总库存
    change_message: str = ""
    available_sizes_keys: list[str] = field(default_factory=list)




@dataclass
class ColorVariant:
    color_name: str
    size_stocks: dict  # 格式为 {尺码: 库存}


@dataclass
class ProductVariant:
    id: str
    color: str
    size: str
    price: str      # 格式示例："500 CAD"
    inventory: int



@dataclass
class SKUDetail:
    id: str
    color: str
    size: str
    price: str
    stock_status: str
    inventory: int
    tags: list[str]
    upc: str



@dataclass
class SKUResult:
    sku_details: list[SKUDetail]
    sku_hash: int

@dataclass
class ProductInfo:
    product_image: str = None
    product_name: str = None
    product_code: str = None
    product_url: str = None

def load_config(config_path: str = "arc_config.json") -> tuple:
    """读取JSON配置文件（参考网页[3,4](@ref)的实现方案）"""
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return (
                config.get("product_url_list", []),
                config.get("interval_minutes", 10) * 60,  # 分钟转秒
                config.get("proxy_file_path", "proxies.txt"),
                config.get("discord_webhook_url", ""),
                config.get("error_wait_seconds", 5) * 60
            )
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Config load failed: {str(e)}")
        return [], 600, "proxies.txt", "", 5
    

def load_proxies(file_path: str) -> list[str]:
    """读取代理列表文件（参考网页[1](@ref)的代理存储方案）"""
    try:
        with open(file_path, 'r') as f:
            return [Proxy.from_str(line.strip()).as_url for line in f if line.strip()]
    except FileNotFoundError:
        logger.error(f"Proxy file {file_path} not found")
        return []

class ArcteryxScraper:
    DEFAULT_HEADERS = headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'cache-control': 'no-cache',
      'pragma': 'no-cache',
      'priority': 'u=0, i',
      'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
  }

    def __init__(self, url, headers=None, proxy=None):
        if proxy is None:
            raise ValueError("proxy is required")
        self.url = url
        self.headers = headers or self.DEFAULT_HEADERS
        self.product_data = None
        self.color_map = {}
        self.size_map = {}
        self.sku_details = []
        # self.session = AsyncSession(impersonate="chrome124", verify=False, timeout=60)
        self.product_image = None
        self.product_name = None
        self.product_code = None
        # self.product_url = None
        self.product_info = ProductInfo()
        self.proxy = Proxy.from_str(proxy)

        # self.session.proxies = {
        #     "http": proxy.as_url,
        #     "https": proxy.as_url
        # }


    async def fetch_data(self):
        try:
            self.session = AsyncSession(impersonate="chrome124", verify=False, timeout=60)
            self.session.proxies = {
                "http": self.proxy.as_url,
                "https": self.proxy.as_url
            }
            response = await self.session.get(self.url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            next_data = soup.find('script', id='__NEXT_DATA__')
            self.product_data = json.loads(json.loads(next_data.string)['props']['pageProps']['product'])
            product_image = self.product_data.get('colourOptions', {}).get('options', [])[0].get('image', {}).get('url')
            product_name = self.product_data.get('analyticsName', None)
            product_code = self.product_data.get('id', None)

            if not any([product_image is None, product_name is None, product_code is None]):
                self.product_image = product_image
                self.product_name = product_name
                self.product_code = product_code
                self.product_info = ProductInfo(product_image, product_name, product_code, self.url)

            self._build_mappings()
            return self.product_data
        finally:
            await asyncio.sleep(0.8)
            await self.session.close()

    def _build_mappings(self):
        self.color_map = {
            item['value']: item['label']
            for item in self.product_data['colourOptions']['options']
        }
        self.size_map = {
            item['value']: item['label']
            for item in self.product_data['sizeOptions']['options']
        }
    
    def generate_sku_details(self, product_data) -> SKUResult:
        self.sku_details = [
            SKUDetail(
                id=variant['id'],
                color=self.color_map.get(variant['colourId'], '未知颜色'),
                size=self.size_map.get(variant['sizeId'], '未知尺码'),
                price=f"{variant['price']} {product_data['currencyCode']}",
                stock_status="有货" if variant['inventory'] > 0 else "缺货",
                inventory=variant['inventory'],
                tags=[badge['label'].strip() for badge in variant['badges']],
                upc=variant['upc']
            )
            for variant in product_data['variants']
        ]
        return SKUResult(
            sku_details=self.sku_details,
            sku_hash=hash(str([asdict(sku) for sku in self.sku_details]))
        )        

    def generate_color_variants(self):
        color_groups = {}
        for sku in self.sku_details:
            if sku.color not in color_groups:
                  color_groups[sku.color] = ColorVariant(
                      color_name=sku.color,
                      size_stocks={}
                  )
        color_groups[sku.color].size_stocks[sku.size] = sku.inventory
        self.color_variants = list(color_groups.values())
        
    # 校验 sku_details 库存是否正确
    def verify_inventory(self):
        for sku in self.sku_details:
            if sku.inventory <= 0:
                logger.error(f"错误：SKU {sku.id} 的库存为 {sku.inventory}，应大于0")


    @staticmethod
    def group_by_color(sku_details) -> dict[str, list[SKUDetail]]:
        color_groups = defaultdict(list)
        # print(color_groups)
        for sku in sku_details:
            color_groups[sku.color].append(sku)
        return color_groups

# 如果有2个一样, 2个一样的为真实结果, 如果3个一样, 3个一样的为真实结果
def compare_sku_results(sku_result1, sku_result2, sku_result3):
    hashes = [
        sku_result1.sku_hash,
        sku_result2.sku_hash,
        sku_result3.sku_hash
    ]
    
    # 统计哈希值出现次数
    hash_counts = {}
    for h in hashes:
        hash_counts[h] = hash_counts.get(h, 0) + 1
    
    # 找出出现次数最多的哈希值
    max_count = max(hash_counts.values())
    if max_count < 2:
        raise ValueError("没有找到两个或三个一致的结果")
    
    # 获取所有符合最大次数的哈希值
    common_hashes = [h for h, count in hash_counts.items() if count == max_count]
    
    # 返回第一个匹配的结果（三个相同则任意，两个相同则取第一个匹配对）
    for result in [sku_result1, sku_result2, sku_result3]:
        if result.sku_hash in common_hashes:
            return result



async def fetch(product_url: str, proxy_list: list[str]) -> list[ArcteryxScraper]:
    # 创建三个独立的爬虫实例
    scrapers = [
        ArcteryxScraper(product_url, proxy=random.choice(proxy_list)),
        ArcteryxScraper(product_url, proxy=random.choice(proxy_list)),
        ArcteryxScraper(product_url, proxy=random.choice(proxy_list))
    ]
    
    # 同时发送三个请求
    results = await asyncio.gather(
        *[scraper.fetch_data() for scraper in scrapers],
        return_exceptions=True
    )


    for result in results:
        if isinstance(result, Exception):
            raise Exception(f"任务异常: {result}")
    return scrapers



@dataclass
class DiscordNotifier:
    webhook_url: str
    # cache: list[ColorGroupAnalysis] = {}
    cache: dict[str, list[ColorGroupAnalysis]] = field(default_factory=dict)
    def _find_changes(self, product_code: str, new_analysis: list[ColorGroupAnalysis]) -> list[ColorGroupAnalysis]:
        """对比新旧分析结果，生成变更信息"""
        if product_code not in self.cache:
            return new_analysis
        
        changed_analysis = []
        old_map = {a.color_name: a for a in self.cache[product_code]}
        
        for new in new_analysis:
            old = old_map.get(new.color_name)
            if not old:
                new.change_message = "❗新增颜色"
                changed_analysis.append(new)
                continue
            
            changes = []
            # 检测价格变化
            if new.price != old.price:
                changes.append(f"价格变动: {old.price} → {new.price}")
                print(f"价格变动: {old.price} → {new.price}")
                
            # 检测尺码变化
            new_sizes = set(new.available_sizes_keys)
            old_sizes = set(old.available_sizes_keys)
            if added := new_sizes - old_sizes:
                changes.append(f"新增尺码: {', '.join(added)}")
            if removed := old_sizes - new_sizes:
                changes.append(f"减少尺码: {', '.join(removed)}")
            
            if changes:
                new.change_message = "\n".join(changes)
                changed_analysis.append(new)
        
        return changed_analysis
        
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))  # 每2秒重试一次，最多3次
    def send_notification(self, message: str, embeds: List[dict] = None):
        # try:
        """发送基础通知到Discord"""
        payload = {"content": message}
        if embeds:
            payload["embeds"] = embeds
            
        requests.post(
            self.webhook_url,
            json=payload,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                "Content-Type": "application/json"},
            timeout=20,
        )
        time.sleep(1.3)
            # print(response.text)
            # response.raise_for_status()
        # except Exception as e:
        #     logger.error(f"发送通知失败: {e}")

    
    def send_color_analysis(self, product_info: ProductInfo, color_analysis: list[ColorGroupAnalysis]):
        # 检测变更
        changed_analysis = self._find_changes(product_info.product_code, color_analysis)
        current_time = datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat()

        # 更新缓存
        self.cache[product_info.product_code] = color_analysis
        color_embed = {
                "title": f"{product_info.product_name}",
                "description": f"**产品代码:** {product_info.product_code}\n[🛒 点击购买]({product_info.product_url})",
                "color": 0x009688,
                "fields": [],
                "timestamp": current_time
            }
        embeds = []
        lines = ["\n\n\n"]
        for analysis in changed_analysis:
            # analysis.available_sizes
            line = ""
            line += f"🎨 颜色: {analysis.color_name}\n"
            line += f"💰 价格: {analysis.price}\n"
            # line += f"📦 总库存: {analysis.total_inventory}件\n"
            # 修改尺码显示格式为 尺码(库存量)
            size_stock = [f"{size}({stock})" for size, stock in analysis.available_sizes.items()]
            line += f"👕 尺码库存: {', '.join(size_stock)}\n"  # 显示具体库存
            # line += f"👕 尺码: {','.join(analysis.available_sizes_keys)}\n\n"
            if analysis.change_message:
                line += f"📢 变更: {analysis.change_message}\n"
            line += "\n"
            lines.append(line)

        color_embed["fields"].append({
                "name": f"",  # 添加必要字段
                "value": "".join(lines),
                "inline": False
            })
        color_embed["thumbnail"] = {"url": product_info.product_image}
        embeds.append(color_embed)

        if changed_analysis:
            for i in range(0, len(embeds), 10):
                try:
                    self.send_notification(
                        f"",
                        embeds=embeds[i:i+10]
                    )
                except Exception as e:
                    logger.error(f"发送通知失败: {e}")
        


# 获取正确的最终结果
async def get_correct_result(product_url: str, proxy_list: list[str]):
    scrapers = await fetch(product_url=product_url, proxy_list=proxy_list)
    results = [scraper.generate_sku_details(scraper.product_data) for scraper in scrapers]
    final_result = compare_sku_results(*results)
    return final_result, scrapers[0].product_info



def analyze_color_groups(product_color_groups: dict[str, list[SKUDetail]]) -> list[ColorGroupAnalysis]:
    """修改后的统计逻辑"""
    analysis = []
    
    for color_name, skus in product_color_groups.items():
        # 统计尺码库存字典（包含具体库存量）
        size_inventory = defaultdict(int)

        # if random.randint(0, 10) < 8:
        #     skus[2].inventory = 0
        
        for sku in skus:
            if sku.inventory > 0:
                size_inventory[sku.size] += sku.inventory  # 累加相同尺码库存
        
        # 转换格式并排序（示例：{"S": 5, "M": 3}）
        sorted_sizes = dict(sorted(
            size_inventory.items(),
            key=lambda x: x[0]  # 按尺码字母顺序排序
        ))
        
        # 获取价格（取第一个有效SKU的价格）
        price = next((sku.price for sku in skus if sku.price), "无价格信息")
        available_sizes_keys = list(sorted_sizes.keys())
        # if available_sizes_keys:  # 转换为列表后检查是否为空
        #     available_sizes_keys.remove(random.choice(available_sizes_keys))
        #str_X = ""
        # random_X = random.randint(0, 10)
        analysis.append(ColorGroupAnalysis(
            color_name=color_name,
            available_sizes=sorted_sizes,  # 使用字典格式
            available_sizes_keys=available_sizes_keys,
            price=price,
            total_inventory=sum(sku.inventory for sku in skus),
        ))
    
    return analysis




async def monitor_task(proxy_list: list[str], product_url: str, interval: int = 10, webhook_url: str= "", error_wait_seconds: int = 5, start_delay: int = 0):
    #生成中国时间
    notifier = DiscordNotifier(webhook_url=webhook_url)
    await asyncio.sleep(start_delay)
    error_times = 0  # 初始化错误计数器

    while True:
        china_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
        try:
            final_result, product_info = await get_correct_result(product_url=product_url, proxy_list=proxy_list)
            product_color_groups: dict[str, list[SKUDetail]] = ArcteryxScraper.group_by_color(final_result.sku_details)   
            color_analysis: list[ColorGroupAnalysis] = analyze_color_groups(product_color_groups)
            logger.success(f"{china_time.strftime('%Y-%m-%d %H:%M:%S')}--->{product_url}--->monitor success")
            notifier.send_color_analysis(product_info, color_analysis)
            # notifier.send_end_notification(product_info, color_analysis)
            await asyncio.sleep(interval)
        except Exception as e:
            error_times += 1
            logger.error(f"{china_time.strftime('%Y-%m-%d %H:%M:%S')}--->{product_url} wait {error_wait_seconds} seconds ----> {error_times} times ---->{e}")
            await asyncio.sleep(error_wait_seconds)


async def process_monitor():
    product_urls, interval_seconds, proxy_path, webhook_url, error_wait_seconds = load_config('arc_config.json')
    proxy_list = load_proxies(proxy_path)
    
    tasks = [
            monitor_task(
                proxy_list=proxy_list,
                product_url=product_url,
                interval=interval_seconds,
                webhook_url=webhook_url,
                # notifier=notifier,
                error_wait_seconds=error_wait_seconds,
                start_delay=random.randint(0, 15) # 为每个任务分配递增的延迟
            )
            for i, product_url in enumerate(product_urls)
        ]    
    await asyncio.gather(*tasks)



if __name__ == "__main__":
    asyncio.run(process_monitor())
