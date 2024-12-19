import random
import string
import requests
import json
import pandas as pd

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

""" 
0
: 
{id: "1826450454825472002", name: "1层", code: "1826450454829666304", img: null,…}
1
: 
{id: "1826450454825472003", name: "2层", code: "1826450454829666305", img: null,…}
2
: 
{id: "1826450454825472004", name: "3层", code: "1826450454829666306", img: null,…}
3
: 
{id: "1826450454829666306", name: "4层", code: "1826450454829666307", img: null,…}
4
: 
{id: "1826450454829666307", name: "5层", code: "1826450454829666308", img: null,…}
"""
def add(name,code):
    url = "https://zhyd.hdu.edu.cn/api/bios/ibms-basic/basic/space"
    payload = json.dumps({
        "insertLocationMethod": 0,
        "label": [],
        "name": str(name),
        "code": str(code),
        "type": "8",
        "parentId": "1826450454829666307"
        #教室的type用8，，，，实验室用1826185207904538625
    })
    headers = {
        'bios-app-id': '1826178625062150146',
        'token': '4f7c068e-36f8-4afa-902c-d9574e8eab88',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"Response for {name}: {response.text}")

def main():
    # 加载Excel文件
    df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/room.xlsx',sheet_name="data")  # 将'data.xlsx'替换为你的Excel文件路径

    # 遍历Excel文件中的每一行
    for index, row in df.iterrows():
        name = row['name']  # 假设Excel文件中有一个名为'name'的列
        code = row['code']
        add(name,code)


if __name__ == '__main__':
    main()
