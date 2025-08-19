import aiofiles
from better_proxy import Proxy

async def read_file_lines(file_path: str):
    """
    异步读取文件的函数
    
    参数:
        file_path: 要读取的文件路径
        
    返回:
        包含文件所有行的列表（每行已去除结尾的换行符）
    """
    lines = []
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            async for line in file:
                lines.append(line.rstrip('\n'))
        return lines
    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'")
        return []
    except IOError as e:
        print(f"读取文件时发生错误: {str(e)}")
        return []


async def load_proxy_url_list(path):
    proxy_url_list = await read_file_lines(path)
    proxy_url_list = [Proxy.from_str(proxy_url.strip()).as_url for proxy_url in proxy_url_list]
    return proxy_url_list
