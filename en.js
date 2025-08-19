const { EncryptJWT, generateKeyPair } = require('jose');

async function encryptWithJose() {
    try {
        // 生成RSA密钥对
        const { publicKey, privateKey } = await generateKeyPair('RSA-OAEP', {
            modulusLength: 2048,
        });

        // 礼品卡数据
        // const giftCardData = {
        //     "giftCardNumber": "6006 4969 4750 1290 823",
        //     "generationtime": "2025-06-29T12:27:40Z"
        // };

        const code = {
            "giftCardPin": "4966",
            "generationtime": "2025-06-30T03:46:48Z"
        }

        const number =
        {
            "giftCardNumber": "6006 4969 4750 1290 823",
            "generationtime": "2025-06-30T03:46:48Z"
        }
        
        // 创建JWE
        const jwe = await new EncryptJWT(giftCardData)
            .setProtectedHeader({ 
                alg: 'RSA-OAEP', 
                enc: 'A256CBC-HS512',
                version: '1'  // 自定义字段
            }).encrypt(publicKey);
        console.log('JWE加密结果:', jwe);
        console.log('是否以ey开头:', jwe.startsWith('ey'));
        return jwe;
    } catch (error) {
        console.error('加密失败:', error);
    }
}

encryptWithJose();