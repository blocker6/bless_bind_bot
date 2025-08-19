const cluster = require('cluster');
const numCPUs = require('os').cpus().length;
const { log } = require('console');
const { keys } = require('libp2p-crypto');
const PeerId = require('peer-id');
const http = require('http');

// 直接设置 Peer 的函数
async function setupPeer(encryptedKey, password) {
    try {
        const privateKey = await keys.import(encryptedKey, password);
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

// 主进程：启动集群
if (cluster.isMaster) {
    console.log(`主进程 ${process.pid} 正在启动`);
    
    // 创建工作进程
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on('exit', (worker, code, signal) => {
        console.log(`工作进程 ${worker.process.pid} 已退出`);
        cluster.fork(); // 重启死掉的进程
    });

} else {
    // 工作进程：运行HTTP服务器

    // 优化的签名生成函数
    async function getSignatureWithTimeout(encryptedKey, timeout = 5000) {
        const signaturePromise = async () => {
            if (!encryptedKey) return null;
            
            // 直接设置 peer，不使用缓存
            const key = await setupPeer(encryptedKey, "6b66260453d590ba82faf310");
            const privateKey = key.pk;
            const peerId = key.peerId;

            const timestamp = Math.floor(Date.now() / 60000) * 60000;
            const message = `${peerId}-${timestamp}`;
            
            const signature = await privateKey.sign(
                new TextEncoder().encode(message)
            );
            
            return Buffer.from(signature).toString('hex');
        };

        const timeoutPromise = new Promise((_, reject) => {
            setTimeout(() => reject(new Error('签名生成超时')), timeout);
        });

        return Promise.race([signaturePromise(), timeoutPromise]);
    }

    // 优化的HTTP服务器
    const server = http.createServer(async (req, res) => {
        // 设置keep-alive
        res.setHeader('Connection', 'keep-alive');
        res.setHeader('Keep-Alive', 'timeout=5, max=1000');
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Content-Type', 'application/json');
        res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

        if (req.method === 'OPTIONS') {
            res.writeHead(200);
            res.end();
            return;
        }

        if (req.method === 'POST' && req.url === '/signature') {
            try {
                let body = '';
                let bodyLength = 0;
                const maxBodySize = 1024 * 1024; // 1MB限制

                req.on('data', chunk => {
                    bodyLength += chunk.length;
                    if (bodyLength > maxBodySize) {
                        res.writeHead(413);
                        res.end(JSON.stringify({ error: 'Request too large' }));
                        return;
                    }
                    body += chunk.toString();
                });

                req.on('end', async () => {
                    try {
                        const { encryptedKey } = JSON.parse(body);
                        
                        if (!encryptedKey) {
                            res.writeHead(400);
                            res.end(JSON.stringify({ error: 'encryptedKey is required' }));
                            return;
                        }

                        const signature = await getSignatureWithTimeout(encryptedKey);
                        
                        res.writeHead(200);
                        res.end(JSON.stringify({ 
                            success: true, 
                            signature: signature,
                            timestamp: Date.now(),
                            worker: process.pid
                        }));
                    } catch (error) {
                        res.writeHead(500);
                        res.end(JSON.stringify({ 
                            success: false, 
                            error: error.message 
                        }));
                    }
                });
            } catch (error) {
                res.writeHead(500);
                res.end(JSON.stringify({ 
                    success: false, 
                    error: error.message 
                }));
            }
        } else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'Not Found' }));
        }
    });

    // 服务器优化配置
    server.keepAliveTimeout = 65000;
    server.headersTimeout = 66000;
    server.maxConnections = 1000;

    const PORT = process.env.PORT || 3000;
    server.listen(PORT, () => {
        console.log(`工作进程 ${process.pid} 在端口 ${PORT} 启动签名服务`);
    });
}
