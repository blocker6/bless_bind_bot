from datetime import datetime, timedelta
from enum import Enum
from tortoise import Model, fields, Tortoise
from loguru import logger

class Account(Model):
    """钱包模型"""
    email = fields.CharField(max_length=255, unique=True)
    headers = fields.JSONField(null=True)
    sleep_until = fields.DatetimeField(null=True)
    session_blocked_until = fields.DatetimeField(null=True)
    user_agent = fields.CharField(max_length=255, null=True)
    points = fields.IntField(default=0)
    proxy_url = fields.CharField(max_length=255, null=True, default=None)
    user_agent = fields.CharField(max_length=255, null=True, default=None)
    created_at = fields.DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = fields.DatetimeField(auto_now=True)  # 更新时间
    is_wallet_connected = fields.BooleanField(default=False)  # 是否连接过钱包
    is_twitter_connected = fields.BooleanField(default=False)  # 是否认证过推特
    is_dc_connected = fields.BooleanField(default=False)  # 是否认证过DC
    is_dc_alive = fields.BooleanField(default=True)  # DC是否为活
    is_twitter_alive = fields.BooleanField(default=True)  # 推特是否为活
    bless_auth_token = fields.CharField(max_length=750, unique=True, null=True)  # Bless Token
    twitter_auth_token = fields.CharField(max_length=750, unique=True, null=True)  # Twitter Token
    discord_auth_token = fields.CharField(max_length=750, unique=True, null=True, default=None)
    wallet_address = fields.CharField(max_length=255,null=True, default=None)  # 钱包地址,不能为空因为需要用来唯一标识账户和进行钱包相关操作
    private_key = fields.CharField(max_length=255, null=True, unique=True, default=None)  # 私钥
    is_delete = fields.BooleanField(default=False)  # 是否跳过
    pub_key = fields.CharField(max_length=255, null=True, default=None)
    encrypted_key = fields.CharField(max_length=255, null=True, default=None)
    hardware_info = fields.JSONField(null=True, default=None)
    hardware_id = fields.CharField(max_length=255, null=True, default=None)
    is_registed = fields.BooleanField(default=False)  # DC是否为活
    is_quiz_0_completed = fields.BooleanField(default=False)  # 是否完成成就测验
    nodes = fields.JSONField(null=True, default=None)
    nodes_len = fields.IntField(default=0)
    nodes_infos = fields.JSONField(null=True, default=None)
    # 修改为今天/昨天/前天的积分表示
    # today_points = fields.IntField(default=0)  # 今天的积分
    # yesterday_points = fields.IntField(default=0)  # 昨天的积分
    # day_before_yesterday_points = fields.IntField(default=0)  # 前天的积分
    

    class Meta:
        table = "bless_node_v1.1"
    
    def __str__(self):
        return f"{self.wallet_address or '未命名钱包'} ({self.address[:10]}...)"
    
    @classmethod
    async def get_account(cls, email: str):
        return await cls.get_or_none(email=email)

    @classmethod
    async def get_accounts(cls):
        return await cls.all()

    @classmethod
    async def create_account(cls, email: str, headers: dict = None):
        account = await cls.get_account(email=email)
        if account is None:
            account = await cls.create(email=email, headers=headers)
            return account
        else:
            account.headers = headers
            await account.save()
            return account

    @classmethod
    async def delete_account(cls, email: str):
        account = await cls.get_account(email=email)
        if account is None:
            return False

        await account.delete()
        return True

    @classmethod
    async def transfer_discord_tokens(cls):
        """
        转移Discord Token：
        1. 获取所有有token但points=0的账户（来源账户）
        2. 获取所有无token但points>0的账户（目标账户）
        3. 按创建时间倒序进行token转移
        """
        # 获取来源账户（points=0且有token）
        source_accounts = await cls.filter(
            points=0,
            discord_auth_token__not_isnull=True,
            discord_auth_token__not='',
            is_delete=False,
            is_dc_connected=False
        ).order_by('-created_at')
        # 获取目标账户（points>0且无token）
        target_accounts = await cls.filter(
            points__gt=0,
            discord_auth_token__isnull=True,
            is_delete=False,
            is_dc_connected=False
        ).order_by('-created_at')

        transferred = 0
        # 逐个转移直到其中一个列表耗尽
        for source, target in zip(source_accounts, target_accounts):
            # 跳过相同token已存在的情况
            # if await cls.exists(discord_auth_token=source.discord_auth_token):
            #     continue
                
            target.discord_auth_token = source.discord_auth_token
            source.discord_auth_token = None  # 清空来源账户的token
            await source.save()
            await target.save()
            # await asyncio.gather(target.save(), source.save())
            transferred += 1
            logger.success(f"转移成功 | 来源: {source.email} -> 目标: {target.email}")

        return {
            "total_transferred": transferred,
            "remaining_sources": len(source_accounts) - transferred,
            "remaining_targets": len(target_accounts) - transferred
        }
    
    @classmethod
    async def clear_bless_auth_token(cls, email: str):
        account = await cls.get_account(email=email)
        if account is None:
            return False

        account.bless_auth_token = None
        await account.save()
        return True




    @classmethod
    async def set_sleep_until(cls, email: str, sleep_until: datetime):
        account = await cls.get_account(email=email)
        if account is None:
            return False

        if sleep_until.tzinfo is None:
            sleep_until = pytz.UTC.localize(sleep_until)
        else:
            sleep_until = sleep_until.astimezone(pytz.UTC)

        account.sleep_until = sleep_until
        await account.save()
        logger.info(f"Account: {email} | Set new sleep_until: {sleep_until}")
        return True

    @classmethod
    async def set_session_blocked_until(
        cls, email: str, session_blocked_until: datetime
    ):
        account = await cls.get_account(email=email)
        if account is None:
            account = await cls.create_account(email=email)
            account.session_blocked_until = session_blocked_until
            await account.save()
            logger.info(
                f"Account: {email} | Set new session_blocked_until: {session_blocked_until}"
            )
            return

        if session_blocked_until.tzinfo is None:
            session_blocked_until = pytz.UTC.localize(session_blocked_until)
        else:
            session_blocked_until = session_blocked_until.astimezone(pytz.UTC)

        account.session_blocked_until = session_blocked_until
        await account.save()
        logger.info(
            f"Account: {email} | Set new session_blocked_until: {session_blocked_until}"
        )
