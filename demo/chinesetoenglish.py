import time

import pandas as pd
from pypinyin import lazy_pinyin
import json


def data():
    # 读取 Excel 文件
    df = pd.read_excel("/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/output.xlsx")

    # 提取拼音首字母的函数
    def get_first_letters(chinese_word):
        # 如果输入不是字符串类型，直接返回空字符串
        if not isinstance(chinese_word, str):
            return ''

        first_letters = ''
        for char in chinese_word:
            # 如果是中文字符，获取拼音首字母
            if '\u4e00' <= char <= '\u9fa5':
                pinyin = lazy_pinyin(char)
                first_letters += pinyin[0][0].upper() if pinyin else ''
            # 如果是字母、数字或符号，直接保留
            else:
                first_letters += char
        # 检查是否存在重复值，如果有重复，则在末尾加上 1
        # while first_letters in df['拼音首字母'].values:
        #     first_letters += '1'
        first_letters=first_letters.replace('#', '_')

        return first_letters.replace('-', '_')

    # 应用函数到 Excel 列,前面是输入列，后面是被转字符串列
    df['拼音首字母'] = df['点名'].apply(get_first_letters)

    # 将结果保存到新的 Excel 文件
    df.to_excel('output.xlsx', index=False)


def identifier():
    # 读取Excel文件
    df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/output.xlsx')

    # 创建一个空列表来存储JSON对象
    json_list = []

    # 遍历每一行数据
    for index, row in df.iterrows():
        if row['type']=="INT":
            step=1
        if row['type']=="FLOAT":
            step=0.1
        json_obj = {
            "identifier": row['拼音首字母'],
            "name": row['点名'],
            "response": True,
            "accessMode":  row['accessMode'],
            "content": {
                "type": row['type'],
                "step": step,
                "max": 999999,
                "min": -999999,
                'unit': row['unit']
            },
            "remark": None
        }
        json_list.append(json_obj)

    # 将列表转换为JSON格式字符串
    json_output = json.dumps(json_list, indent=4, ensure_ascii=False)
    # 将JSON字符串写入文件
    with open('output.json', 'w') as f:
        f.write(json_output)


if __name__ == '__main__':
    data()
    time.sleep(1)
    identifier()
