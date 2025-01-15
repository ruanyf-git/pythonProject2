import time
import pandas as pd
from pypinyin import lazy_pinyin
import json


def get_first_letters(chinese_word):
    """
    提取中文字符串的拼音首字母，并保留字母、数字和符号。
    """
    if not isinstance(chinese_word, str):
        return ''
    first_letters = ''.join(
        lazy_pinyin(char)[0][0].upper() if '\u4e00' <= char <= '\u9fa5' else char
        for char in chinese_word
    )
    return first_letters.replace('#', '_').replace('-', '_')


def generate_excel_with_pinyin(input_path, output_path):
    """
    读取Excel文件，生成拼音首字母列并保存到新的Excel文件。
    """
    df = pd.read_excel(input_path)
    df['拼音首字母'] = df['点名'].apply(get_first_letters)
    df.to_excel(output_path, index=False)


def generate_json_from_excel(input_path, output_path):
    """
    根据Excel数据生成JSON文件。
    """
    type_to_step = {
        "INT": 1,
        "FLOAT": 0.1
    }

    df = pd.read_excel(input_path)
    attributes_list = []

    for _, row in df.iterrows():
        # 初始化JSON对象
        identifier = row['拼音首字母']
        # 检查是否重复，若重复则递增后缀数字
        original_identifier = identifier
        suffix = 1
        while any(attr['identifier'] == identifier for attr in attributes_list):
            identifier = f"{original_identifier}{suffix}"
            suffix += 1
        json_obj = {
            "identifier": row['拼音首字母'],
            "name": row['点名'],
            "response": True,
            "accessMode": row['accessMode'],
            "content": {
                "type": row['type']
            },
            "remark": None
        }

        # 根据类型处理不同的字段
        if row['type'] == "BOOL":
            json_obj['content']['trueValue'] = row.get('ttt', None)
            json_obj['content']['falseValue'] = row.get('fff', None)
        else:
            json_obj['content']['max'] = 999999
            json_obj['content']['min'] = -999999
            step = type_to_step.get(row['type'])
            if step is not None:
                json_obj['content']['step'] = step

        # 检查并添加 unit 字段
        unit = row.get('unit')
        if pd.notna(unit) and str(unit).strip():
            json_obj['content']['unit'] = str(unit).strip()

        attributes_list.append(json_obj)

    # 构造最终JSON结构
    final_json = {
        "profile": {
            "productKey": "Cp9CaOn8VcC",
            "modelId": "1876089854034149378",
            "modelName": "设备模型2025-01-06_10-14-14"
        },
        "attributes": attributes_list,
        "events": [],
        "services": []
    }

    # 写入JSON文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_json, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # 文件路径
    input_excel_path = "/Users/ruanyunfeng/PycharmProjects/pythonProject2/demo/output.xlsx"
    output_excel_path = "output.xlsx"
    output_json_path = "output.json"

    # 处理流程
    generate_excel_with_pinyin(input_excel_path, output_excel_path)
    time.sleep(1)  # 确保文件已保存
    generate_json_from_excel(output_excel_path, output_json_path)
