import asyncio
# from core.solvers import *
from src.utils import load_config
config = load_config()
semaphore = asyncio.Semaphore(config.threads)
# single_semaphore = asyncio.Semaphore(1)
# captcha_solver = (
#     AntiCaptchaImageSolver(config.anti_captcha_api_key)
#     if config.captcha_module == "anticaptcha"
#     else TwoCaptchaImageSolver(config.two_captcha_api_key)
# )
# captcha_cloudflare_solver = (config.cloudflare_turnstile_api_key)
# file_operations = FileOperations()