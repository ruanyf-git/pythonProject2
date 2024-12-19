import time

import pandas as pd
import json
import requests

def device_link_video():
    df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/device_link_video.xlsx', skiprows=0)
    api_url = "http://111.203.152.160:38080/api/bios/ibms-basic/acc/video/device"
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'http://111.203.152.160:38080',
        'Referer': 'http://111.203.152.160:38080/app/show',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'bios-app-id': '1',
        'isc-api-version': '2.0',
        'project-id': '-1',
        'token': '2513f07b-a6f7-47ea-803c-3192f95a28fa',
        'Content-Type': 'application/json'
    }
    # 遍历每一行
    for index, row in df.iterrows():
        # 获取第一列和第二列的数据
        col1_data = row[0]
        col2_data = row[1]
        params = {"deviceId":f"{col1_data}","videoDevices":[{"videoDeviceIds":[f"{col2_data}"],"cameraType":"NORMAL"}]}

        # sql=f"INSERT INTO report_rule_device_relation ( rule_id, device_id, project_id) VALUES ( 1748229335961796610, '{col1_data}', 1745407341231165442);"
        # formatted_json = json.dumps(params, indent=4)
        # print(formatted_json)
        js=json.dumps(params)

        response = requests.post(api_url, json=params, headers=headers)
        # 检查请求是否成功
        print(index,response.text)
        time.sleep(0.5)

if __name__ == '__main__':
    device_link_video()
