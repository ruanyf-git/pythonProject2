import pandas as pd
import requests

def excel_test():
    # 读取Excel文件中的数据
    excel_file = '/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/yunzhou.xlsx'  # 你的Excel文件名
    sheet_name = '设备列表'  # Excel工作表的名称或索引
    data = pd.read_excel(excel_file, sheet_name=sheet_name)
    # 假设设备ID在名为'device_id'的列中
    device_ids = data['*设备ID']
    # 遍历设备ID并生成对应的URL
    for device_id in device_ids:
        print(device_id)


if __name__ == '__main__':
    excel_test()
