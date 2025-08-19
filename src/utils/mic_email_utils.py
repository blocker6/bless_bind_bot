

import asyncio
from dataclasses import dataclass
import time
import imaplib
import email
import re
from typing import Optional, List
import aiohttp
from bs4 import BeautifulSoup
from loguru import logger
from datetime import datetime



@dataclass
class MicEmail:
    mic_email: str
    mic_password: str
    mic_client_id: str
    mic_refresh_token: str

    def __post_init__(self):
        # 邮箱格式验证
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.mic_email):
            raise ValueError(f"Invalid email format: {self.mic_email}")
            
        # 客户端ID长度验证
        if len(self.mic_client_id) != 36:
            raise ValueError(f"mic_client_id长度必须为36，当前长度：{len(self.mic_client_id)}，值：{self.mic_client_id}")
            
        # Refresh Token长度验证
        if len(self.mic_refresh_token) < 200:
            logger.error(f"mic_refresh_token长度必须大于200，当前长度：{len(self.mic_refresh_token)}，值：{self.mic_refresh_token}")
            raise ValueError(f"mic_refresh_token长度必须大于200，当前长度：{len(self.mic_refresh_token)}，值：{self.mic_refresh_token}")

@dataclass
class Mic_Account:
    email: str
    client_id: str
    refresh_token: str

@dataclass
class MailConfig:
    mail_server: str
    email_address: str
    password: str

@dataclass
class EmailCriteria:
    from_address: str
    
    body_substring: str = ""  # 添加默认值使其成为可选参数


def generate_auth_string(email_name: str, access_token: str):
    """
    Generates the authentication string for XOAUTH2.

    :param email_name: The email address.
    :param access_token: The OAuth2 access token.
    :return: The authentication string as bytes.
    """
    auth_string = f"user={email_name}\1auth=Bearer {access_token}\1\1"
    return auth_string  # Ensure bytes are returned


def extract_verification_link(email_content):
    """
    从邮件内容中提取邮箱验证链接
    
    Args:
        email_content (str): 邮件的HTML内容
        
    Returns:
        str: 提取到的验证链接，如果未找到则返回None
    """
    # 使用正则表达式提取URL
    pattern = r'https://app\.nodego\.ai/verify-email\?token=[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'

    match = re.search(pattern, email_content)
    if match:
        return match.group(0)
    return None




def extract_verification_code(email_content):
    """
    从邮件内容中提取邮箱验证码
    
    Args:
        email_content (str): 邮件的HTML内容
        
    Returns:
        str: 提取到的验证码，如果未找到则返回None
    """
    # 使用正则表达式提取6位数字验证码
    pattern = r'<p>(\d{6})</p>'
    match = re.search(pattern, email_content)
    if match:
        return match.group(1)
    return None




def get_mic_emails(lines: list[str]):
    mic_emails = [MicEmail(
        mic_email=line.split(":")[0],
        mic_password=line.split(":")[1],
        mic_client_id=line.split(":")[2], 
        mic_refresh_token=line.split(":")[3]
    ) for line in lines]
    if mic_emails:
        return mic_emails
    else:
        raise ValueError("mic_emails is empty")



class MicLinkExtractor:
    """
    A class to asynchronously check an email account for a specific verification link using OAuth2 authentication.
    """
    # 支持的mode类型:
    # - register: 注册邮箱验证链接模式
    # - verify: 重新验证邮箱链接模式
    def __init__(
        self,
        account: Mic_Account,
        mode: str = "register",  # mode可选值: register, verify
        max_attempts: int = 8,
        delay_seconds: int = 20,
        search_folders: Optional[List[str]] = None,
        since_timestamp: Optional[datetime] = None,  # New parameter
        proxy = None
    ):
        """
        Initializes the EmailLinkChecker with necessary parameters.

        :param account: Account object containing email and access token.
        :param mode: 邮件链接模式,可选值:register(注册验证),verify(重新验证)
        :param max_attempts: Maximum number of attempts to check for the link.
        :param delay_seconds: Delay between attempts in seconds.
        :param search_folders: List of folders to search in addition to 'inbox'.
        :param since_timestamp: Only fetch emails received after this timestamp.
        """
        self.account = account
        self.client_id = account.client_id
        self.refresh_token = account.refresh_token  # Ensure refresh_token is available
        self.max_attempts = max_attempts
        self.delay_seconds = delay_seconds
        self.access_token = None
        self.search_folders = search_folders or ['inbox']
        self.since_timestamp = since_timestamp  # Store the timestamp
        self.proxy = proxy
        



    def delete_matching_emails(self, account: Mic_Account, email_criteria: EmailCriteria):
        """
        根据指定条件删除邮件
        
        Args:
            account (Account): 账户信息，包含邮箱地址和认证令牌
            email_criteria (EmailCriteria): 邮件筛选条件
        """
        try:
            # 确保已获取访问令牌
            # if not self.access_token:
            #     await self.refresh_access_token()
                
            # 连接到IMAP服务器
            mail = imaplib.IMAP4_SSL('outlook.office365.com', 993)
            mail.authenticate('XOAUTH2', lambda x: generate_auth_string(account.email, self.access_token))
            
            logger.info(f"准备清理 {account.email} 的邮件")
            
            # 构建搜索条件
            criteria_parts = []
            
            # 添加发件人条件
            if email_criteria.from_address:
                criteria_parts.append(f'(FROM "{email_criteria.from_address}")')
            
            # 添加收件人条件（如果需要）
            # if email_criteria.recipient_email and email_criteria.recipient_email != account.email:
            #     criteria_parts.append(f'(TO "{email_criteria.recipient_email}")')
                
            # 组合搜索条件
            search_criteria = " ".join(criteria_parts) if criteria_parts else "ALL"
            
            logger.info(f"使用搜索条件: {search_criteria}")
            
            # 在所有文件夹中执行删除操作
            for folder_name in self.all_folders:
                try:
                    # 选择当前文件夹
                    mail.select(folder_name)
                    
                    # 搜索匹配的邮件
                    status, messages = mail.search(None, search_criteria)
                    
                    # 删除匹配的邮件
                    if status == 'OK' and messages[0]:
                        message_count = len(messages[0].split())
                        logger.info(f"在文件夹 {folder_name} 中找到 {message_count} 封匹配的邮件")
                        
                        for num in messages[0].split():
                            mail.store(num, '+FLAGS', '\\Deleted')
                        
                        # 永久删除
                        mail.expunge()
                        logger.info(f"已从 {folder_name} 删除 {message_count} 封邮件")
                    else:
                        logger.info(f"文件夹 {folder_name} 中没有匹配的邮件")
                        
                    mail.close()
                except Exception as e:
                    logger.error(f"处理文件夹 {folder_name} 失败: {e}")
            
            mail.logout()
            logger.info(f"邮件删除操作完成")
            return True
            
        except imaplib.IMAP4.error as e:
            logger.error(f"IMAP错误: {e}")
            return False
        except Exception as e:
            logger.error(f"操作失败: {e}")
            return False




    async def refresh_access_token(self) -> bool:
            """
            Fetches a new access token using the refresh token.

            :return: True if the access token was refreshed successfully, else False.
            """
            url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
            data = {
                'client_id': self.client_id,
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
                'scope': 'https://outlook.office.com/IMAP.AccessAsUser.All offline_access',
            }
            logger.debug(f"Fetching new access token for {self.account.email}")

            try:
                timeout = aiohttp.ClientTimeout(total=30)  # 设置超时
                proxy_str = str(self.proxy) if self.proxy else None  # 确保代理是字符串格式
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.post(url, data=data, proxy=proxy_str) as response:
                        
                        if response.status != 200:
                            logger.error(response.text)
                            logger.error(f"Failed to refresh access token: HTTP {response.status}")
                            # raise Exception(f"Failed to refresh access token: HTTP {response.status}")
                            return response.status
                        response_json = await response.json()
                        if 'access_token' in response_json:
                            self.access_token = response_json['access_token']
                            # Optionally update the refresh token if it's rotated
                            if 'refresh_token' in response_json:
                                self.refresh_token = response_json['refresh_token']
                                self.refresh_token = self.refresh_token  # Update the Account model
                            logger.info(f"Access token refreshed for {self.account.email}")
                            return response.status
                        else:
                            error = response_json.get('error', 'Unknown error')
                            logger.error(f"Failed to refresh access token: {error}")
                            raise Exception(f"Failed to refresh access token: {error}")
            except Exception as e:
                logger.error(f"Exception while refreshing access token: {e}")
                raise Exception(f"Exception while refreshing access token: {e}")

    @property
    def all_folders(self) -> List[str]:
        return ['Drafts', 'Sent', 'Deleted', 'Junk', 'Notes', 'Inbox', 'Outbox']




    def retrieve_matching_email_content(
        self,
        account: Mic_Account,
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

            # Connect to the IMAP server
            mail = imaplib.IMAP4_SSL('outlook.office365.com')
            mail.authenticate('XOAUTH2', lambda x: generate_auth_string(account.email, self.access_token))
            all_folders = self.all_folders
            if not all_folders:
                raise Exception("Folder Listing Failed")
            for attempt in range(1, max_attempts + 1):
                logger.info(f"{account.email} --- 尝试第 {attempt} 次获取匹配的邮件")
                for folder in all_folders:
                    logger.debug(f"Selecting folder: {folder}")
                    mail.select(folder)
                    # 构建搜索条件
                    if email_criteria.from_address:
                        search_criteria = f'(FROM "{email_criteria.from_address}")'
                        logger.debug(f"使用发件人筛选条件: {search_criteria}")
                        result, data = mail.search(None, search_criteria)
                    else:
                        raise Exception("from_address is required")
                
                     # 修改判断逻辑：不仅检查result是否为OK，还要检查data[0]是否为空
                    if result == "OK" and data[0]:  # 确保data[0]不为空
                        logger.info(f"在{folder}中找到匹配的邮件")
                        break
                    else:
                        logger.info(f"在{folder}中未找到匹配的邮件")
                        continue

                # 获取邮件ID列表
                mail_ids = data[0].split()
                logger.debug(f"邮件ID列表: {mail_ids}")
                if result == "OK" and not mail_ids:
                    logger.info(f"尝试{attempt}/{max_attempts}次后未找到匹配的邮件, 等待{interval}秒后重试")
                    time.sleep(interval)
                    continue


                latest_mail_id = mail_ids[-1]
                result, msg_data = mail.fetch(latest_mail_id, "(RFC822)")

                if result != "OK":
                    logger.error(f"未找到 RFC822 邮件")
                    raise Exception(f"在{folder}中未找到匹配的邮件")

                body = ""
                raw_email = msg_data[0][1]
                email_message = email.message_from_bytes(raw_email)
                    
                if email_message.is_multipart():
                    for part in email_message.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/html":
                            payload = part.get_payload(decode=True)
                            if payload:
                                body += payload.decode('utf-8', errors='ignore')
                else:
                    # 处理非多部分邮件
                    payload = email_message.get_payload(decode=True)
                    if payload:
                        body = payload.decode('utf-8', errors='ignore')
                # 在处理完所有部分后返回body
                return body
            
        except imaplib.IMAP4.error as e:
            logger.error(f"IMAP error for account {account.email}: {e}")
            return {"error_key": "IMAP Error", "error_msg": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error while fetching emails for account {account.email}: {e}")
            return {"error_key": "Unexpected Error", "error_msg": str(e)}



async def get_verification_link(
    email: str,
    client_id: str,
    refresh_token: str,
    from_address: str = 'no-reply@nodego.ai'
) -> str:
    account = Mic_Account(
        email=email,
        client_id=client_id,
        refresh_token=refresh_token
    )
    email_criteria = EmailCriteria(
        recipient_email=email,
        from_address=from_address
    )
    mic_link_extractor = MicLinkExtractor(account=account)
    await mic_link_extractor.refresh_access_token()
    email_content = mic_link_extractor.retrieve_matching_email_content(account=account, email_criteria=email_criteria)
    return extract_verification_link(email_content)


# async def delete_matching_emails(
#     email: str,
#     client_id: str,
#     refresh_token: str,
#     from_address: str = 'no-reply@nodego.ai'
# ) -> bool:
#     account = Account(
#         email=email,
#         client_id=client_id,
#         refresh_token=refresh_token
#     )
#     email_criteria = EmailCriteria(
#         recipient_email=email,
#         from_address=from_address
#     )
#     mic_link_extractor = MicLinkExtractor(account=account)
#     await mic_link_extractor.refresh_access_token()
#     return await mic_link_extractor.delete_matching_emails(account=account, email_criteria=email_criteria)


async def main():
    account = Mic_Account(email='m61g08ngv94ka@outlook.com',
                      client_id='dbc8e03a-b00c-46bd-ae65-b683e7707cb0', 
                      refresh_token='M.C522_BL2.0.U.-Ci*yMV9qLFri5u2aY*Ae5!j2j7NvG!eon1y7PdwrQhy53Hf2OtlbPcDsAxD091x5aoR7EX0Yw1HvXWrd6AQr8gbksAGdGZdezFsCqGiHJevV!WoFONQfEebGgVfMF5ex8eL9A6tnbgOKL7Vt3Px!vVJdgKc1dNYTiswyBsnqvkV4Vtcexo2ii441zTKVmR3zMSrZixIR53pO6B!Igz4PGGlmo*KXXoDbZYf*YkxoZuHcNPHL7YBCmvDFv2Lhkl5m9qvKb7geMbliKjcQUsJxsWTZ7qayxhST8yiQsQNPUsaPRIRIR3tjjzN*M7Mq7GhD8NPOVMNFFyoxlSA4usQUUvkzy9!zXcZUNyZfTDMvY!rheVRX5dxpwQ4viK4CMeu8*Q$$')
    email_criteria = EmailCriteria(from_address='no-reply@nodego.ai')
    mic_link_extractor = MicLinkExtractor(account=account)
    await mic_link_extractor.refresh_access_token()
    # await mic_link_extractor.delete_matching_emails(account=account, email_criteria=email_criteria)
    email_content = mic_link_extractor.retrieve_matching_email_content(account=account, email_criteria=email_criteria)
    # print(email_content)
    verification_link = extract_verification_link(email_content)
    print(verification_link)
    # return verification_link



if __name__ == "__main__":
    asyncio.run(main())
