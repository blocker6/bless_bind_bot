# 更进一步的通用版本，支持更多自定义选项
from loguru import logger
from database.connection import close_db, init_db
from database.models import Account


async def batch_update_account_field_advanced(
    field_name: str, 
    new_values: list,
    filter_condition: dict = None,
    allow_duplicates: bool = False
):
    """
    高级通用的账户字段批量更新函数
    
    Args:
        field_name: 需要更新的字段名
        new_values: 新的值列表
        filter_condition: 自定义过滤条件，默认为字段为空
        allow_duplicates: 是否允许重复值，默认False
    """
    await init_db()
    try:
        # 参数验证
        if not field_name or not new_values:
            raise ValueError("字段名和新值列表不能为空")
        
        # 处理可用值
        available_values = new_values.copy()
        
        if not allow_duplicates:
            # 获取已存在的值并去重
            all_accounts = await Account.all().values(field_name)
            existing_values = [account[field_name] for account in all_accounts if account[field_name]]
            existing_values_set = set(existing_values)
            available_values = list(set(new_values) - existing_values_set)
        
        # 构建过滤条件
        if filter_condition is None:
            filter_condition = {f"{field_name}__isnull": True}
        
        need_update_accounts = await Account.filter(filter_condition).all()
        need_update_accounts_list = list(need_update_accounts)
        
        # 检查可用值是否足够
        if len(available_values) < len(need_update_accounts_list):
            print(f"警告：可用{field_name}数量({len(available_values)})少于需要更新的账户数量({len(need_update_accounts_list)})")
            need_update_accounts_list = need_update_accounts_list[:len(available_values)]
        
        # 分配值
        for i, account in enumerate(need_update_accounts_list):
            setattr(account, field_name, available_values[i])
        
        print(f"准备更新的{field_name}: {available_values[:len(need_update_accounts_list)]}")
        
        # 批量更新
        await Account.bulk_update(need_update_accounts_list, fields=[field_name])
        print(f"成功更新了 {len(need_update_accounts_list)} 个账户的 {field_name}")
        
        return len(need_update_accounts_list)  # 返回更新的数量
        
    except Exception as e:
        logger.error(f"批量更新{field_name}时出现错误: {str(e)}")
        raise
    finally:
        await close_db()