import secrets
import binascii

# 生成256位安全随机数（32字节）
private_key_bytes = secrets.token_bytes(32)

# 转换为十六进制字符串
private_key_hex = binascii.hexlify(private_key_bytes).decode('utf-8')

print("ETH 私钥（保密！切勿泄露）: 0x" + private_key_hex)
