import requests
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def send_request():
    url = "http://localhost:3000/signature"
    payload = json.dumps({
        "encryptedKey": "mMwU4Fo0wnfSZmnU9sMFBhcxLoOle+3aZOe+YuNAlMJPys4QcesxAhyo1rLsoa8A6BgrddZ/XzFwn+4ItQWLXnfyY2CfbWJOsfte/sDJI2K4wvFV8j0KJXh6B7NscsC8ubSPeJWsm6DkkoxpG1kXEPQ"
    })
    headers = {'Content-Type': 'application/json'}
    
    try:
        start_time = time.time()
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        end_time = time.time()
        
        return {
            'status_code': response.status_code,
            'response_time': end_time - start_time,
            'success': response.status_code == 200
        }
    except Exception as e:
        return {
            'status_code': 0,
            'response_time': 0,
            'success': False,
            'error': str(e)
        }

def concurrent_test(num_threads=100, num_requests=1000):
    results = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        
        for future in futures:
            results.append(future.result())
    
    end_time = time.time()
    
    # 统计结果
    successful_requests = sum(1 for r in results if r['success'])
    failed_requests = len(results) - successful_requests
    avg_response_time = sum(r['response_time'] for r in results if r['success']) / max(successful_requests, 1)
    total_time = end_time - start_time
    qps = len(results) / total_time
    
    print(f"总请求数: {len(results)}")
    print(f"成功请求数: {successful_requests}")
    print(f"失败请求数: {failed_requests}")
    print(f"成功率: {successful_requests/len(results)*100:.2f}%")
    print(f"平均响应时间: {avg_response_time:.3f}秒")
    print(f"总耗时: {total_time:.3f}秒")
    print(f"QPS: {qps:.2f}")



if __name__ == "__main__":
    concurrent_test(num_threads=50, num_requests=500)
