import requests
import json

def send_adyen_save_state_request(encrypted_card_number, encrypted_security_code, cart_id=None):
    """
    发送Adyen保存状态数据的GraphQL请求到Arc'teryx API
    
    Args:
        encrypted_card_number (str): 加密的卡号
        encrypted_security_code (str): 加密的安全码
        cart_id (str, optional): 购物车ID，如果不提供则使用默认值
    
    Returns:
        dict: API响应数据，如果请求失败则返回None
    """
    
    # API端点
    url = "https://arcteryx.com/api/mcgql"
    
    # 请求头
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://arcteryx.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://arcteryx.com/us/en/checkout/',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'arcteryx_en',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'x-country-code': 'us',
        'x-is-checkout': 'true',
        'x-jwt': '',
        'x-kpsdk-cd': '{"workTime":1751193175107,"id":"7438f082c28928d4d5ff45e8da2a807a","answers":[1,8],"duration":85.7,"d":554,"st":1751188878228,"rst":1751188878782}',
        'x-kpsdk-ct': '0E2d9wTp6pf4Zq4ofHglPKOhr2rfy7rpYwiOpeHID1ZKjm1q7zmqeZHhUZOMm5bBBykVtRt8eoNEN1bWbOlBjwJXpZ43G8bEgX2AOugjn0tzWPNuPnFaUB2sbRro0oiEpOPTbmolKZKItDRJzSXaXtW3JZED0x8i1H831q5Q',
        'x-kpsdk-v': 'j-1.1.0'
    }
    
    # 如果没有提供cart_id，使用默认值
    if cart_id is None:
        cart_id = "OjMXueUso748doGRSvsmTo89gVO7swoI"
    
    # 构建stateData对象
    state_data = {
        "paymentMethod": {
            "type": "giftcard",
            "brand": "svs",
            "encryptedCardNumber": encrypted_card_number,
            "encryptedSecurityCode": encrypted_security_code
        },
        "giftcard": {
            "pspReference": "LVX8RT48NR2S39F6",
            "resultCode": "Success",
            "balance": {
                "currency": "USD",
                "value": 28167
            },
            "title": "SVS"
        }
    }
    
    # 将stateData转换为JSON字符串
    state_data_json = json.dumps(state_data, separators=(',', ':'))
    # GraphQL请求数据
    payload = {
        "query": "mutation adyenSaveStateData($stateData: String!, $cartId: String!) { adyenSaveStateData(stateData: $stateData, cartId: $cartId) { stateDataId } }",
        "variables": {
            "stateData": state_data_json,
            "cartId": cart_id
        }
    }
    
    try:
        # 发送POST请求
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        # 检查响应状态
        response.raise_for_status()
        
        # 返回JSON响应
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"响应状态码: {e.response.status_code}")
            print(f"响应内容: {e.response.text}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
        return None

# 使用示例
if __name__ == "__main__":
    # 示例加密数据（请替换为实际的加密数据）
    encrypted_card_number = "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.neRDxsOjJ_woQPJ8r-sLOt5DP3iFhcmcBFUqDJrkOU7_N9s6fUvjJXFvvIVtJJ3ak0qjxyGxH4bdMLjT6M3k5B0wHgZF5-9Mo8Hcmunz4kOPrmnBE1Z8NQ-bqIAIf9uph8HLuA7x75bXVKA0f72BUqvzDR194KomwMhJzrMh0KOzP6_bLaIufSoB6BSxEsnX0Zyb4jwd-_kHnDd-ud8bS3Rzbl3pkOT1aKbVpljwma4X-KpSW7gr4ckkIT6UG-nfiMLUEVIJ2ycoO090Ww_mtWCGQuXtcloVyHvDXAlTPYV6ooL62jYZr8OwQ1GnY3qUOcsjuD6muMLQJM3nB9zQmA.r93NvNg_tdhoN2xcksXy8Q.frXqyfmvqE4w7GlG7kzacmRxwm2r0dZIwS4jvfahxIGlAIu0kJtY56jt_Mr9wtxnoR46M16CkrRFHtZ27sUZsN_3PFZkxsOf8A9jD1VZqFtlrHrFgAOti9mfvs7unZkT.7wJeXk-8SktDHUXwbfB-pKmqJLhSxpJg8Okg37nqD8Y"
    encrypted_security_code = "eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZDQkMtSFM1MTIiLCJ2ZXJzaW9uIjoiMSJ9.pjNuN-b-tMc1o_Xh8JQVaYHT-"
    send_adyen_save_state_request(encrypted_card_number, encrypted_security_code)

    
# ```json
# {
#   "error": true,
#   "message": "network error"
# }
