import asyncio
import os
mjs_path = os.path.join(os.path.dirname(__file__), "m.js")
async def generate_private_key(password ="6b66260453d590ba82faf310"):
    try:
        normalized_path = mjs_path.replace("\\", "/")
        cmd = ['node', '-e', 
            f'const {{ GeneratePrivateKey }} = require("{normalized_path}");'
            f'GeneratePrivateKey("{password}").then(console.log)']
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
        stdout, _ = await proc.communicate()
        await proc.wait()
        return stdout.decode().strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
    
async def get_signature(encryptedKey = ""):
    try:
        cmd = ['node', '-e', f'const {{ getSignature }} = require(".//m.js"); getSignature("{encryptedKey}").then(console.log)']
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE)
        stdout, _ = await proc.communicate()
        await proc.wait()
        return stdout.decode().strip()
    except Exception as e:
        print(f"Error: {e}")
        return None



# async def process_task(encrypted_key):
#     data = await get_signature(encrypted_key)
#     print(data)
#     return data

# def run_async_task(encrypted_key):
#     asyncio.run(process_task(encrypted_key))

# async def main():
#     # 生成1000个相同的加密密钥（或根据需要生成不同的）
#     encrypted_keys = ["mMwU4Fo0wnfSZmnU9sMFBhcxLoOle+3aZOe+YuNAlMJPys4QcesxAhyo1rLsoa8A6BgrddZ/XzFwn+4ItQWLXnfyY2CfbWJOsfte/sDJI2K4wvFV8j0KJXh6B7NscsC8ubSPeJWsm6DkkoxpG1kXEPQ"] * 1000
#     # 使用多进程池
#     with Pool(processes=10) as pool:  # 可以根据CPU核心数调整进程数
#         pool.map(run_async_task, encrypted_keys)


# if __name__ == "__main__":
#     asyncio.run(main())    