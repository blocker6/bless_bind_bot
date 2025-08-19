import json
import time
import hashlib
import base58
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

class LibP2PKeyManager:
    def __init__(self):
        self.backend = default_backend()
    
    def _create_peer_id_from_public_key(self, public_key_bytes):
        """
        根据公钥创建PeerId (遵循libp2p规范)
        """
        # libp2p使用的是multihash格式
        # 0x12: SHA256哈希类型, 0x20: 32字节长度
        hash_digest = hashlib.sha256(public_key_bytes).digest()
        multihash = b'\x12\x20' + hash_digest
        
        # 使用base58编码
        peer_id = base58.b58encode(multihash).decode('utf-8')
        return peer_id
    
    def generate_private_key(self, password):
        """
        生成Ed25519密钥对并返回加密的私钥和PeerId
        """
        # 1. 生成Ed25519密钥对
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
        
        # 2. 获取公钥字节
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        
        # 3. 创建PeerId
        peer_id = self._create_peer_id_from_public_key(public_key_bytes)
        
        # 4. 加密私钥
        encrypted_key = self._encrypt_private_key(private_key, password)
        
        return json.dumps({
            'peerId': peer_id,
            'encryptedKey': encrypted_key
        })
    
    def _encrypt_private_key(self, private_key, password):
        """
        使用密码加密私钥 (PKCS#8格式)
        """
        # 将私钥序列化为PKCS#8格式并加密
        encrypted_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(
                password.encode('utf-8')
            )
        )
        
        # 转换为base64以便存储
        return base64.b64encode(encrypted_key).decode('utf-8')
    
    def _decrypt_private_key(self, encrypted_key_b64, password):
        """
        解密私钥
        """
        import base64
        encrypted_key_bytes = base64.b64decode(encrypted_key_b64)
        
        # 从加密的PKCS#8格式恢复私钥
        private_key = serialization.load_pem_private_key(
            encrypted_key_bytes,
            password=password.encode('utf-8'),
            backend=self.backend
        )
        
        return private_key
    
    def setup_peer(self, encrypted_key, password):
        """
        从加密私钥恢复密钥对和PeerId
        """
        try:
            # 解密私钥
            private_key = self._decrypt_private_key(encrypted_key, password)
            
            # 获取公钥
            public_key = private_key.public_key()
            public_key_bytes = public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw
            )
            
            # 重建PeerId
            peer_id = self._create_peer_id_from_public_key(public_key_bytes)
            
            return {
                'pk': private_key,
                'peer_id': peer_id,
                'public_key': public_key
            }
        except Exception as error:
            print(f'节点初始化失败: {error}')
            raise error
    
    def get_signature(self, encrypted_key, password="6b66260453d590ba82faf310"):
        """
        生成签名
        """
        if not encrypted_key:
            return None
        
        # 恢复密钥对
        key_info = self.setup_peer(encrypted_key, password)
        private_key = key_info['pk']
        peer_id = key_info['peer_id']
        
        try:
            # 生成时间窗口凭证（每分钟更新）
            timestamp = int(time.time() // 60) * 60000  # 转换为毫秒并对齐到分钟
            message = f"{peer_id}-{timestamp}"
            
            # 生成ED25519签名
            signature = private_key.sign(message.encode('utf-8'))
            
            # 转换签名为HEX格式
            return signature.hex()
            
        except Exception as error:
            print(f'签名生成失败: {error}')
            raise error

# 使用示例
# async def main():
#     key_manager = LibP2PKeyManager()
    
#     # 生成密钥对
#     password = "your_password_here"
#     key_data = await key_manager.generate_private_key(password)
#     print("生成的密钥数据:")
#     print(key_data)
    
#     # 解析生成的数据
#     key_info = json.loads(key_data)

#     # print(key_info)

#     encrypted_key = key_info['encryptedKey']
    
#     # 生成签名
#     signature = key_manager.get_signature(encrypted_key)
#     print(f"\n生成的签名: {signature}")
    
#     # 验证可以正确恢复密钥
#     peer_info = key_manager.setup_peer(encrypted_key, password)
#     print(f"\n恢复的PeerId: {peer_info['peer_id']}")

# 同步版本的便利函数
def generate_private_key_sync(password):
    """同步版本的密钥生成函数"""
    key_manager = LibP2PKeyManager()
    data = key_manager.generate_private_key(password)
    return data

def get_signature_sync(encrypted_key, password="6b66260453d590ba82faf310"):
    """同步版本的签名生成函数"""
    key_manager = LibP2PKeyManager()
    return key_manager.get_signature(encrypted_key, password)


async def main():
    data = generate_private_key_sync("6b66260453d590ba82faf310")
    data = json.loads(data)
    encryptedKey = data["encryptedKey"]
    data = get_signature_sync(encryptedKey, "6b66260453d590ba82faf310")
    print(data)
    


# 如果需要异步支持，可以这样运行
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())