import os
import yaml
from itertools import cycle
from loguru import logger
from better_proxy import Proxy
from typing import List, Dict, Generator
from pydantic import BaseModel
from typing import Optional
# from bot import get_mic_emails
from .helper import load_proxy_url_list
# from utils.utils import load_proxy_url_list
# from .helper import load_proxy_url_list
from .mic_email_utils import MailConfig, MicEmail, get_mic_emails

CONFIG_PATH = os.path.join(os.getcwd(), "config")
CONFIG_DATA_PATH = os.path.join(CONFIG_PATH, "data")
CONFIG_PARAMS = os.path.join(CONFIG_PATH, "settings.yaml")

# REQUIRED_DATA_FILES = ("accounts.txt", "proxies.txt")
# REQUIRED_PARAMS_FIELDS = (
#     "threads",
#     "keepalive_interval",
#     "imap_settings",
#     "captcha_module",
#     "delay_before_start",
#     "referral_codes",
#     "redirect_settings",
#     "two_captcha_api_key",
#     "anti_captcha_api_key",
# )

class Config(BaseModel):
    # 声明已知属性
    threads: Optional[int] = None
    keepalive_interval: Optional[int] = None
    proxies: Optional[List[str]] = None
    mic_emails: Optional[List[MicEmail]] = None
    two_captcha_api_key: Optional[str] = None
    anti_captcha_api_key: Optional[str] = None
    yes_captcha_api_key: Optional[str] = None
    haxi_imap_setting: Optional[Dict[str, str]] = None
    imap_settings: Optional[MailConfig] = None
    user_agents: Optional[List[str]] = None
    # 执行 代理任务 的进程数
    FRAMING_PROCESSES: Optional[int] = None
    # 登录并发数 避免同时大量消耗 cloudflare 的次数
    FRAMING_CONCURRENCY: Optional[int] = None
    twitters: Optional[List[str]] = None
    discords: Optional[List[str]] = None


    class Config:
        extra = 'allow'  # 允许额外字段

def read_file(
    file_path: str, check_empty: bool = True, is_yaml: bool = False
) -> List[str] | Dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if check_empty and os.stat(file_path).st_size == 0:
        raise ValueError(f"File is empty: {file_path}")

    if is_yaml:
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def get_params() -> Dict:
    data = read_file(CONFIG_PARAMS, is_yaml=True)
    return data

def load_config() -> Config:
    try:
        params = get_params()
        proxies = load_proxy_url_list(os.path.join(CONFIG_DATA_PATH, "proxies.txt"))
        mic_emails = get_mic_emails(read_file(os.path.join(CONFIG_DATA_PATH, "mic_email.txt"), check_empty=False))
        user_agents = read_file(os.path.join(CONFIG_DATA_PATH, "user_agents.txt"), check_empty=False)
        config = Config(
            **params, proxies=proxies, mic_emails=mic_emails, user_agents= user_agents
        )
        twitters = read_file(os.path.join(CONFIG_DATA_PATH, "twitters.txt"), check_empty=False)
        discords = read_file(os.path.join(CONFIG_DATA_PATH, "discords.txt"), check_empty=False)
        config.twitters = twitters
        config.discords = discords
        return config

    except Exception as exc:
        logger.error(f"Failed to load config: {exc}")
        exit(1)