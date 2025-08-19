from tortoise import Tortoise
from loguru import logger
from pathlib import Path



async def init_db():
    """初始化数据库连接"""
    db_path = Path(__file__).parent / "db" / "bless.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    await Tortoise.init(
        db_url=f"sqlite://{db_path}",
        modules={"models": ["database.models"]}
    )
    await Tortoise.generate_schemas(safe=True)
    logger.info("数据库初始化完成")

async def close_db():
    """关闭数据库连接"""
    await Tortoise.close_connections()
    logger.info("数据库连接已关闭")