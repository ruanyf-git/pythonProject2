import json
import time

import pandas as pd
import requests

def get_extra():
    excel_file = '/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/yunzhou.xlsx'  # 你的Excel文件名
    sheet_name = '设备列表'  # Excel工作表的名称或索引
    data = pd.read_excel(excel_file, sheet_name=sheet_name)
    # 假设设备ID在名为'device_id'的列中
    device_ids = data['*设备ID']
    # 遍历设备ID并生成对应的URL
    for device_id in device_ids:
        url = "http://218.75.77.234:38080/api/device/dmc/device/" + device_id
        payload = {}
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://218.75.77.234:38080/os/device-manage?date=1720083558039',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
            'isc-api-version': '2.0',
            'token': '728c6b36-0504-4151-8877-fcf417480649'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        extra_bak = json_data.get("data").get("extra")
        devId = json_data.get("data").get("devId")
        devName = json_data.get("data").get("devName")
        secret = json_data.get("data").get("secret")
        json1 = {
            "extra": extra_bak,
            "groupId": "1807985321959256066",
            "devId": devId,
            "devName": devName,
            "secret": secret,
            "parentId": "wangguan",
            "rentalId": "1",
            "tenantId": "system",
            "groupName": "手报"
        }
        # 将extra字段的JSON字符串解析为字典
        extra_data = json.loads(json1['extra'])
        # 将解析后的字典转换为JSON字符串并进行转义
        escaped_extra_data = json.dumps(extra_data, ensure_ascii=False).replace('\\', '\"').replace("人工派单","手动派单").replace("系统派单","手动派单")
        # 将转义后的JSON字符串放回原字典的extra字段中
        json1['extra'] = escaped_extra_data
        # 将整个字典转换为JSON字符串并格式化输出
        formatted_output = json.dumps(json1, indent=4, ensure_ascii=False)
        # print(formatted_output)
        url = "http://218.75.77.234:38080/api/device/dmc/device"
        headers = {
            'token': '728c6b36-0504-4151-8877-fcf417480649',
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, json=json1)
        time.sleep(0.5)
        print(response.text)


if __name__ == '__main__':
    get_extra()
