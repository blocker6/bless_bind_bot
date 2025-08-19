# 更精确的实现（需要安装 pip install py-libp2p）
import asyncio
from libp2p.crypto.ed25519 import Ed25519PrivateKey as LibP2PEd25519PrivateKey
from libp2p.peer.id import ID
import json

async def generate_private_key_libp2p(e):
    """
    使用py-libp2p库的更精确实现
    """
    # 1. 生成Ed25519密钥对
    private_key = LibP2PEd25519PrivateKey.new()
    
    # 2. 创建PeerId
    peer_id = ID.from_pubkey(private_key.get_public_key())
    
    # 3. 导出加密私钥（这部分可能需要自定义实现，因为py-libp2p可能没有完全相同的export方法）
    private_key_bytes = private_key.encode()
    encrypted_key = encrypt_private_key(private_key_bytes, e)
    
    # 4. 返回结果
    result = {
        "peerId": str(peer_id),
        "encryptedKey": encrypted_key
    }
    
    return json.dumps(result)

# 异步调用示例
# result = asyncio.run(generate_private_key_libp2p("6b66260453d590ba82faf310"))

encrypt_key = generate_private_key_libp2p("6b66260453d590ba82faf310")
print(encrypt_key)
