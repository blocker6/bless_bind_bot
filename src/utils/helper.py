import random
import string
import aiofiles
from better_proxy import Proxy

def read_file_lines(file_path: str):
    """
    同步读取文件的函数
    
    参数:
        file_path: 要读取的文件路径
        
    返回:
        包含文件所有行的列表（每行已去除结尾的换行符）
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.rstrip('\n'))
        return lines
    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'")
        return []
    except IOError as e:
        print(f"读取文件时发生错误: {str(e)}")
        return []


def load_proxy_url_list(path):
    proxy_url_list = read_file_lines(path)
    proxy_url_list = [Proxy.from_str(proxy_url.strip()).as_url for proxy_url in proxy_url_list]
    return proxy_url_list



def generate_password() -> str:
    # 定义字符集
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = "!@#$^"
    
    # 确保每种类型至少有一个字符
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # 添加随机字符使总长度达到10
    all_chars = lower + upper + digits + special
    password.extend(random.choice(all_chars) for _ in range(6))
    
    # 打乱顺序
    random.shuffle(password)
    return ''.join(password)


def generate_username() -> str:
    """生成11位随机用户名(数字+小写字母)"""
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(11))
