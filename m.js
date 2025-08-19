const { log } = require('console');
const { keys } = require('libp2p-crypto');
const PeerId = require('peer-id');

// e是 6b66260453d590ba82faf310
async function GeneratePrivateKey(e) {
    // 1. 生成Ed25519密钥对（对应generateKeyPair$3）
    const keyPair = await keys.generateKeyPair('Ed25519');
    // 2. 创建PeerId（对应peerIdFromKeys）
    const peerId = await PeerId.createFromPubKey(keyPair.public.bytes);
    // 3. 导出加密私钥（直接使用密钥对的export方法）
    const encryptedKey = await keyPair.export(e);
    return JSON.stringify({
        peerId: peerId.toB58String(),
        encryptedKey: encryptedKey
    });
}


async function setupPeer(encryptedKey, password) {
    try {
        // 使用正确的keys.import方法
        const privateKey = await keys.import(encryptedKey, password);
        // 重建PeerID
        const peerId = await PeerId.createFromPubKey(privateKey.public.bytes);
        return {
            pk: privateKey,
            peer: peerId,
            peerId: peerId.toB58String()
        };
    } catch (error) {
        console.error('节点初始化失败:', error);
        throw error;
    }
}


// encryptedKey  "m2N5PgZxAfgnxdDzvYihXwTPLbfJ6iQDyeNCdlR8K6aOMs5GpUBluhbfFLTOeiV/xCU7tviS6Zj9q9rxymr4N7tEs2/szQp++v7WaEgXTuT+T7Py77L9XPUqhmLBZhyrF9zvU2SUxfeitnZatwLy71Q"
async function getSignature(encryptedKey) {
    if (!encryptedKey) return null;
    const key = await setupPeer(encryptedKey, "6b66260453d590ba82faf310")
    const privateKey = key.pk
    const peerId = key.peerId

    try {
        // 生成时间窗口凭证（每分钟更新）
        const timestamp = Math.floor(Date.now() / 60000) * 60000;
        const message = `${peerId}-${timestamp}`;
        
        // 生成ED25519签名（兼容RFC8032标准）
        const signature = await privateKey.sign(
            new TextEncoder().encode(message)
        );
        
        // 转换签名为HEX格式（兼容多平台验证）
        return Buffer.from(signature).toString('hex');
    } catch (error) {
        console.error('签名生成失败:', error);
        throw error;
    }
}

module.exports = { GeneratePrivateKey, getSignature};
