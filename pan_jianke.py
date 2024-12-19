import sys

import pandas as pd
import json
import numpy as np
import requests

def fix_devname():

    # 获取文件地址
    excel_file_path = "/Users/ruanyunfeng/PycharmProjects/pythonProject2/jinshui.xlsx"

    token="f8ecdad3-f96e-4f13-8ce4-ae8fefb79c57"
    api_url = "http://183.246.178.123:38080/api/model/data/prod/insert/749165894/psf"
    headers = {
        'Pragma': 'no-cache',
        'isc-api-version': '2.0',
        'token': token,
        'Content-Type': 'application/json'
    }
    df = pd.read_excel(excel_file_path)
    for index, row in df.iterrows():
        # 将每一行数据转换为字典
        row_dict = {col: row[col] for col in row.index if pd.notna(row[col])}
        print(row_dict)
        response = requests.post(api_url, json=row_dict, headers=headers)
        # 检查请求是否成功
        if response.status_code == 200:
            print(f'行 {index + 1} 请求成功！')
        else:
            print(f'行 {index + 1} 请求失败，信息: {response.text}')
def fx():

    # 读取Excel文件
    df = pd.read_excel("/Users/ruanyunfeng/PycharmProjects/pythonProject2/jinshui.xlsx")

    # 提取一列数据
    column_data = df['drainage_valve_id']

    # 将数据转换成列表
    data_list = column_data.tolist()

    # 将列表转换成字符串并去除空格和换行符
    data_str = ','.join(map(str, data_list))

    # 将字符串格式化成需要的形式
    result = '' + data_str + ''

    print(result)


if __name__ == '__main__':
    fx()
