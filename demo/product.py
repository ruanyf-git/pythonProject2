import json
import random
import string
import pandas as pd
import requests

def generate_random_key(length=11):
    # 定义可选字符集：大小写字母和数字
    characters = string.ascii_letters + string.digits
    # 随机选择字符并连接
    random_key = ''.join(random.choice(characters) for _ in range(length))
    return random_key
def product():
    # 读取Excel文件
    df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/product.xlsx')  # 替换为你的Excel文件路径

    # 假设你需要读取某一列数据（例如第一列名为“data”）
    data = df['设备类名称'].tolist()

    # 调用API接口
    url = 'http://111.203.152.160:38080/api/device/dmc/product'  # 替换为实际的API URL
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'http://111.203.152.160:38080',
        'Referer': 'http://111.203.152.160:38080/os/device-manage',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'isc-api-version': '2.0',
        'token': '3cd35cc0-f44f-4726-96cb-18a96d47b831',
        'Content-Type': 'application/json'
    }

    # 假设接口需要传递JSON格式数据
    for item in data:
        payload = {
            "protocol": 0,
            "productKey": generate_random_key(),
            "connectType": "SUB_DEVICE",
            "deviceType": "SUB",
            "groupId": "1860855726147899393",
            "communicationType": "MQTT",
            "networkingType": "ETHERNET",
            "labelIds": [],
            "labelValues": [],
            "authType": "DEVICE_CORRESPONDS_TO_SECRET",
            "productName": item
        }
        print(payload)
        response = requests.post(url, json=payload, headers=headers)

        # 检查返回的状态
        if response.status_code == 200:
            print(f"成功调用API，返回数据: {response.json()}")
        else:
            print(f"调用失败，状态码: {response.status_code}")

if __name__ == '__main__':
    product()
