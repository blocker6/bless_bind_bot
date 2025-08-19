const fs = require('fs');

// 读取WASM文件
const wasmBuffer = fs.readFileSync('beacdee13d73ac0e.wasm');

// 实例化WASM模块
WebAssembly.instantiate(wasmBuffer, {
    // 导入对象，提供WASM需要的外部函数
    env: {
        // 模拟浏览器环境的函数
        console_log: (ptr, len) => {
            // 处理控制台输出
        },
        // 其他必要的导入函数
    }
}).then(result => {
    const { instance } = result;
    // 调用WASM导出的函数
    const exportedFunction = instance.exports.your_function;
    console.log(exportedFunction());
});
