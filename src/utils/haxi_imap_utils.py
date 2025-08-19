from datetime import datetime
import random
import string

from imap_tools import MailBox, AND
import time
from dataclasses import dataclass

# from bs4 import BeautifulSoup
# from urllib.parse import urlparse, parse_qs, unquote
# import re



from loguru import logger


@dataclass
class MailConfig:
    mail_server: str
    email_address: str
    password: str

@dataclass
class EmailCriteria:
    recipient_email: str
    from_address: str
    body_substring: str = ""  # 添加默认值使其成为可选参数

class MailboxManager:
    # 初始化的时候传入，email_criteria
    def __init__(self, email_criteria: EmailCriteria, mail_config: MailConfig):
        self.email_criteria = email_criteria
        self.mail_config = mail_config
        
    def clear_matching_emails(
        self,
    ) -> int:
        """
        清空符合条件的所有邮件

        Args:
            mail_config (MailConfig): 邮件服务器和登录凭证的配置
            email_criteria (EmailCriteria): 用于筛选邮件的条件

        Returns:
            int: 被删除的邮件数量

        Raises:
            Exception: 如果操作过程中出现错误
        """

        mail_config = self.mail_config

        try:
            deleted_count = 0
            with MailBox(mail_config.mail_server).login(mail_config.email_address, mail_config.password) as mailbox:
                # 构建搜索条件
                query = AND(
                    to=self.email_criteria.recipient_email,
                    from_=self.email_criteria.from_address
                )
                
                # 获取所有匹配的邮件
                messages = list(mailbox.fetch(query))
                
                # 标记删除并执行清理
                for msg in messages:
                    mailbox.delete(msg.uid)
                    deleted_count += 1
                
                # 立即执行清理操作
                if deleted_count > 0:
                    mailbox.expunge()
                
                logger.info(f"成功删除 {deleted_count} 封匹配邮件")
                return deleted_count

        except Exception as e:
            logger.exception(f"清空邮件时发生错误: {e}")
            raise



    @staticmethod
    def generate_email():
        """
        生成随机邮箱地址
        :return: 随机生成的邮箱地址
        """
        domains = [
            "19980321.xyz", "stakely.cloud", "55foundry.vip", "altos.live",
            "blackfin.online", "blockcamp.website", "compute.wiki", "deepcore.info",
            "erinaceous.nl", "finnimbrun.space", "hashhub.one", "icetea.biz",
            "kryptos.cc", "mungo.life", "nihilarian.de",
            "pronk.best", "scopperloit.in", "soulcapital.us", "team8.tech",
            "tyrotoxism.ca", "widdiful.dev", "bitcog.design"]

        prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 16)))
        domain = random.choice(domains)
        return f"{prefix}@{domain}"




    # @staticmethods
    def retrieve_matching_email_content(
        mail_config: MailConfig,
        email_criteria: EmailCriteria,
        max_attempts: int = 15,
        interval: int = 15
    ) -> str:
        """
        登录邮箱，搜索符合条件的第一封邮件，并返回其HTML内容。

        Args:
            mail_config (MailConfig): 邮件服务器和登录凭证的配置。
            email_criteria (EmailCriteria): 用于筛选邮件的条件。
            max_attempts (int, optional): 最大搜索尝试次数。默认为10。
            interval (int, optional): 尝试之间的间隔（秒）。默认为15秒。

        Returns:
            str: 第一封匹配邮件的HTML内容。

        Raises:
            Exception: 如果在最大尝试次数后未找到符合条件的邮件。
        """
        try:
            with MailBox(mail_config.mail_server).login(mail_config.email_address, mail_config.password) as mailbox:
                for attempt in range(1, max_attempts + 1):
                    logger.info(f"{email_criteria.recipient_email} --- 尝试 {attempt} 次获取匹配的邮件")
                    # 使用 `since_date` 限制搜索的邮件日期
                    messages = mailbox.fetch(
                        AND(
                            to=email_criteria.recipient_email,
                            from_=email_criteria.from_address
                        )
                    )
  
                    matched_messages = messages
                    bodys = [msg.html for msg in matched_messages if msg.html]

                    if bodys:
                        try:
                            first_body = bodys[0]  # 只获取第一个匹配的邮件
                            logger.info("找到第一封匹配的邮件。")
                            return first_body
                        except Exception as e:
                            logger.error(f"处理邮件内容时出错: {e}")
                            raise
                    else:
                        logger.info(f"未找到匹配的邮件。尝试 {attempt}/{max_attempts}。{interval} 秒后重试...")
                        time.sleep(interval)

                logger.error("在最大尝试次数后未找到匹配的邮件。")
                raise Exception("在最大尝试次数后未找到匹配的邮件。")
        except Exception as e:
            logger.exception(f"检索邮件内容时发生错误: {e}")
            raise
# 
# x-y8s6k3db-b
if __name__ == "__main__":
    email_criteria = EmailCriteria(recipient_email='jndsgrw5ws57ad@blockcamp.website', from_address='no-reply@web3auth.io')
    mail_config = MailConfig(mail_server='mail.hforest.xyz', email_address='zx@hforest.xyz', password='abcd654321')
    mail_box = MailboxManager(email_criteria, mail_config)
    mail_box.clear_matching_emails()
    content = mail_box.retrieve_matching_email_content(mail_config, email_criteria)
    print(content)