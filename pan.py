import re
import sys
from dataclasses import replace

import pandas as pd
import json
import numpy as np
import requests

def fix_devname():

    excel_file_path = "/Users/ruanyunfeng/PycharmProjects/pythonProject2/device.xlsx"
    host = "http://www.jkywfm.com:8089"
    token="1269004f-2289-4ca8-841e-0a8d34105700"
    api_url = host+"/api/device/dmc/device"
    headers = {
        'Pragma': 'no-cache',
        'isc-api-version': '2.0',
        'token': token,
        'Content-Type': 'application/json'
    }
    df = pd.read_excel(excel_file_path)
    for index, row in df.iterrows():
        # 将每一行数据转换为字典
        json_data = {col: row[col] for col in row.index if pd.notna(row[col])}

        # 处理 detail 字段中的多余单引号，将其转换为字典
        if 'detail' in json_data:
            detail_str = json_data['detail']
            # 去除字符串两侧的单引号
            detail_str = detail_str.strip("'")
            # 将字符串中的单引号替换为双引号
            detail_str = detail_str.replace("'", '"')

            # 使用正则表达式替换 JSON 字符串中的 Unicode 编码
            detail_str = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), detail_str)

            try:
                # 将处理后的字符串转换为字典
                detail_dict = json.loads(detail_str)
                # 更新 JSON 数据中的 detail 字段为字典格式
                json_data['detail'] = detail_dict
            except json.JSONDecodeError as e:
                print(f"Failed to parse 'detail' field: {e}")

        # 自定义 JSONEncoder 类，用于处理中文字符不转义
        class MyEncoder(json.JSONEncoder):
            def __init__(self, **kwargs):
                kwargs['ensure_ascii'] = False  # 禁止转义非 ASCII 字符
                super().__init__(**kwargs)


        print(json_data)
        response = requests.put(api_url, json=json_data, headers=headers)
        # 检查请求是否成功
        if response.status_code == 200:
            print(f'行 {index + 1} 请求成功！{response.text}')
        else:
            print(f'行 {index + 1} 请求失败，信息: {response.text}')


def fix_devname1():

    excel_file_path = "/Users/ruanyunfeng/PycharmProjects/pythonProject2/jinshui.xlsx"
    host = "http://10.60.250.30:38080"
    token="53d75046-baff-4fdb-bf50-a804798149f4"
    api_url = host+"/api/device/dmc/device"
    headers = {
        'Pragma': 'no-cache',
        'isc-api-version': '2.0',
        'token': token,
        'Content-Type': 'application/json'
    }
    df = pd.read_excel(excel_file_path)
    for index, row in df.iterrows():
        # 将每一行数据转换为字典
        json_data = {col: row[col] for col in row.index if pd.notna(row[col])}


        print(json_data)
        response = requests.put(api_url, json=json_data, headers=headers)
        # 检查请求是否成功
        if response.status_code == 200:
            print(f'行 {index + 1} 请求成功！{response.text}')
        else:
            print(f'行 {index + 1} 请求失败，信息: {response.text}')

if __name__ == '__main__':
    fix_devname1()
