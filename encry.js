// 模拟原始的异步包装器
function Wo(generatorFunction) {
    return function() {
        const generator = generatorFunction.apply(this, arguments);
        
        function handle(result) {
            if (result.done) {
                return Promise.resolve(result.value);
            }
            
            return Promise.resolve(result.value).then(
                res => handle(generator.next(res)),
                err => handle(generator.throw(err))
            );
        }
        
        try {
            return handle(generator.next());
        } catch (ex) {
            return Promise.reject(ex);
        }
    };
}

// RSA-OAEP 加密实现
async function Vo(data, keyConfig) {
    try {
        // 1. 生成或导入RSA公钥
        const publicKey = await generateOrImportPublicKey(keyConfig);
        
        // 2. 将数据转换为字符串然后编码为ArrayBuffer
        const dataString = JSON.stringify(data);
        const encoder = new TextEncoder();
        const dataBuffer = encoder.encode(dataString);
        
        // 3. 使用RSA-OAEP加密
        const encryptedBuffer = await crypto.subtle.encrypt(
            {
                name: "RSA-OAEP"
            },
            publicKey,
            dataBuffer
        );
        
        // 4. 转换为Base64字符串
        const encryptedArray = new Uint8Array(encryptedBuffer);
        const encryptedBase64 = btoa(String.fromCharCode(...encryptedArray));
        
        return encryptedBase64;
        
    } catch (error) {
        console.error("Encryption failed:", error);
        throw error;
    }
}

// 生成或导入RSA公钥
async function generateOrImportPublicKey(keyConfig) {
    // 如果keyConfig为空，生成新的密钥对（仅用于测试）
    if (!keyConfig || Object.keys(keyConfig).length === 0) {
        console.warn("No key provided, generating new key pair for testing");
        
        const keyPair = await crypto.subtle.generateKey(
            {
                name: "RSA-OAEP",
                modulusLength: 2048,
                publicExponent: new Uint8Array([1, 0, 1]), // 65537
                hash: "SHA-1"
            },
            true,
            ["encrypt", "decrypt"]
        );
        
        return keyPair.publicKey;
    }
    
    // 如果提供了具体的密钥数据，导入它
    if (keyConfig.kty || keyConfig.n) {
        // JWK格式
        return await crypto.subtle.importKey(
            "jwk",
            keyConfig,
            {
                name: "RSA-OAEP",
                hash: "SHA-1"
            },
            false,
            ["encrypt"]
        );
    }
    
    // 如果是PEM格式或其他格式，需要相应的处理
    throw new Error("Unsupported key format");
}

// 原始函数的完整实现
function Bo(e, t) {
    return Go.apply(this, arguments);
}

function Go() {
    return (Go = Wo(regeneratorRuntime.mark(function e(t, r) {
        var n;
        return regeneratorRuntime.wrap(function(e) {
            for (;;)
                switch (e.prev = e.next) {
                case 0:
                    if (r) {
                        e.next = 3;
                        break;
                    }
                    return console.warn("WARNING: No encryptionKey"),
                    e.abrupt("return", null);
                case 3:
                    return e.next = 5,
                    Vo(t, r);
                case 5:
                    return n = e.sent,
                    e.abrupt("return", n);
                case 7:
                case "end":
                    return e.stop();
                }
        }, e);
    }))).apply(this, arguments);
}

// 现代化的等价实现
async function modernBo(data, encryptionKey) {
    if (!encryptionKey) {
        console.warn("WARNING: No encryptionKey");
        return null;
    }
    
    const result = await Vo(data, encryptionKey);
    return result;
}


// 测试数据
const testData = {
    "giftCardNumber": "6006 4969 4750 1290 823",
    "generationtime": "2025-06-29T12:27:40Z"
};

// 方式1：使用空密钥（会生成新的密钥对）
async function testWithEmptyKey() {
    try {
        const result = await modernBo(testData, {});
        console.log("Encrypted result:", result);
        return result;
    } catch (error) {
        console.error("Encryption failed:", error);
    }
}

// 方式2：使用预定义的JWK公钥
async function testWithJWKKey() {
    const jwkPublicKey = {
        "kty": "RSA",
        "use": "enc",
        "key_ops": ["encrypt"],
        "alg": "RSA-OAEP",
        "n": "your-base64-encoded-modulus",
        "e": "AQAB" // 65537 in base64
    };
    
    try {
        const result = await modernBo(testData, jwkPublicKey);
        console.log("Encrypted result:", result);
        return result;
    } catch (error) {
        console.error("Encryption failed:", error);
    }
}

// 运行测试
testWithEmptyKey();
