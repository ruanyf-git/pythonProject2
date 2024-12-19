import time

import pandas as pd
import requests
import json

def dev():
    df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/devicemodif.xlsx')
    url = "http://111.203.152.160:38080/api/device/dmc/device"
    # 创建一个空列表来存储JSON对象
    headers = {
       'Accept': 'application/json',
       'isc-api-version': '2.0',
       'token': '98a1b5a5-5f09-482f-a3fe-7c6e8d68e86d',
       'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
       'Content-Type': 'application/json'
    }
    for index, row in df.iterrows():

        json_object=json.dumps({
           "detail": {
              "devId": row['devId'],
              "operator": row['operator'],
           },
           "extra": row['extra'],
           "groupId": row['groupId'],
           "devId": row['devId'],
           "devName": row['devName'],
           "secret": row['secret'],
           "parentId": row['parentId'],
        })
        response = requests.request("PUT", url, headers=headers, data=json_object)
        print(response.text)
        time.sleep(0.5)






if __name__ == '__main__':
    dev()