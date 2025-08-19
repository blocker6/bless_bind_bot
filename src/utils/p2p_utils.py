
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
    
    
    
    def generate_private_key(self):
        """
        直接生成Ed25519密钥对并返回私钥和PeerId（不加密）
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
        
        # 4. 将私钥序列化为PEM格式（不加密）
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        print(private_key_pem)
        
        # 5. 转换为base64以便存储
        private_key_b64 = base64.b64encode(private_key_pem).decode('utf-8')
        
        return json.dumps({
            'peerId': peer_id,
            'privateKey': private_key_b64
        })
    






    def _load_private_key(self, private_key_b64):
        """
        从base64编码的私钥加载私钥对象
        """
        private_key_bytes = base64.b64decode(private_key_b64)
        
        # 从PEM格式恢复私钥
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=self.backend
        )
        
        return private_key
    
    def setup_peer(self, private_key_b64):
        """
        从私钥恢复密钥对和PeerId
        """
        try:
            # 加载私钥
            private_key = self._load_private_key(private_key_b64)
            
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
    
    def get_signature(self, private_key_b64):
        """
        生成签名
        """
        if not private_key_b64:
            return None
        
        # 恢复密钥对
        key_info = self.setup_peer(private_key_b64)
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
        





def encode_bs64(input_string: str):
     # 将字符串转换为字节序列
    input_bytes = input_string.encode('utf-8')
    
    # 进行Base64编码
    encoded_bytes = base64.b64encode(input_bytes)
    
    # 将字节序列转换回字符串
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string


# 同步版本的便利函数
def generate_private_key_sync():
    """同步版本的密钥生成函数（不需要密码）"""
    key_manager = LibP2PKeyManager()
    data = key_manager.generate_private_key()
    return data

def get_signature_sync(private_key):
    private_key_b64 = encode_bs64(F'-----BEGIN PRIVATE KEY-----\n{private_key}\n-----END PRIVATE KEY-----\n')
    # '-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEIFnyIL7dzZ8UwyY9KHbfk/JoAalF3kM8+UyDjb5ljVjD\n-----END PRIVATE KEY-----\n'
    print(private_key_b64)
    """同步版本的签名生成函数"""
    key_manager = LibP2PKeyManager()
    return key_manager.get_signature(private_key_b64)

async def main():
    # 生成密钥对（不需要密码）
    data = get_signature_sync('m2N5PgZxAfgnxdDzvYihXwTPLbfJ6iQDyeNCdlR8K6aOMs5GpUBluhbfFLTOeiV/xCU7tviS6Zj9q9rxymr4N7tEs2/szQp++v7WaEgXTuT+T7Py77L9XPUqhmLBZhyrF9zvU2SUxfeitnZatwLy71Q')
    print(data)
    

# # 如果需要异步支持，可以这样运行
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
