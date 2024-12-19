# -*- coding: utf-8 -*-
# import pandas as pd
# from pypinyin import lazy_pinyin

from flask import Flask, jsonify
from datetime import datetime, timedelta
import random
import time

#
# def data():
#     # 读取 Excel 文件
#     df = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/data.xlsx')
#
#     # 提取拼音首字母的函数
#     def get_first_letters(chinese_word):
#         # 如果输入不是字符串类型，直接返回空字符串
#         if not isinstance(chinese_word, str):
#             return ''
#
#         first_letters = ''
#         for char in chinese_word:
#             # 如果是中文字符，获取拼音首字母
#             if '\u4e00' <= char <= '\u9fa5':
#                 pinyin = lazy_pinyin(char)
#                 first_letters += pinyin[0][0].upper() if pinyin else ''
#             # 如果是字母、数字或符号，直接保留
#             else:
#                 first_letters += char
#         return first_letters
#
#     # 应用函数到 Excel 列
#     df['拼音首字母'] = df['首字母'].apply(get_first_letters)
#
#     # 将结果保存到新的 Excel 文件
#     df.to_excel('output.xlsx', index=False)
#
#


app = Flask(__name__)


def generate_data():
    data = []
    now = datetime.now()
    for i in range(12):
        hour = (now - timedelta(hours=11 - i)).hour
        time_str = (now - timedelta(hours=11 - i)).strftime('%H')  # 生成过去12小时的每个小时，按照从最早到最近排序
        if i in {10, 11, 12, 13, 14}:
            in_num = random.randint(40, 60)
            out_num= random.randint(40, 60)
        elif i in {23, 24, 00, 1, 2, 3, 4, 5}:
            in_num = random.randint(20 , 30)
            out_num = random.randint(20, 30)
            if i ==00:
                time_str="24"
        else:
            in_num = random.randint(30, 40)
            out_num = random.randint(30, 40)

        data.append({
            "name": time_str + "时",
            "category1": in_num,
            "category2": out_num

        })
    return data

def generate_data1():
    data = []
    now = datetime.now()
    for i in range(12):
        hour = (now - timedelta(hours=11 - i)).hour
        time_str = (now - timedelta(hours=11 - i)).strftime('%H')  # 生成过去12小时的每个小时，按照从最早到最近排序
        if i in {10, 11, 12, 13, 14}:
            in_num = random.randint(40, 60)
            out_num= random.randint(40, 60)
        elif i in {23, 24, 00, 1, 2, 3, 4, 5}:
            in_num = random.randint(20 , 30)
            out_num = random.randint(20, 30)
            if i ==00:
                time_str="24"
        else:
            in_num = random.randint(30, 40)
            out_num = random.randint(30, 40)

        data.append({
            "name": time_str + "时",
            "category1": in_num,
            "category2": out_num

        })
    return data


@app.route('/get_numbers', methods=['GET'])
def generate_car_data():
    # 获取当前时间
    now = datetime.now()

    # 计算自0点以来的分钟数
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes_since_midnight = int((now - midnight).total_seconds() / 60)

    # 计算四个数
    num1 = minutes_since_midnight * 5
    num2 = minutes_since_midnight * 6
    num3 = int(minutes_since_midnight * 4.6)
    num4 = int(minutes_since_midnight * 1.3)
    # 计算总和
    total = num1 + num2 + num3 + num4

    # 拆分为十万、万、千、百、十、个
    digits = [0] * 6
    str_total = str(total).zfill(6)  # 确保至少6位，用0填充

    for i in range(6):
        digits[i] = int(str_total[i])

    # 返回JSON响应
    return jsonify({
        '客车': num1,
        '货车': num2,
        '大型客车': num3,
        '急化品车': num4,
        '百万位': digits[0],
        '万位': digits[1],
        '千': digits[2],
        '百': digits[3],
        '十': digits[4],
        '个': digits[5]
    })


def split_value_into_three(value):
    # 生成两个随机点，用于分割原始值
    point1 = int(random.uniform(0, value))
    point2 = int(random.uniform(0, value))

    # 确保 point1 和 point2 按大小顺序排列
    if point1 > point2:
        point1, point2 = point2, point1

    # 将原始值分成三份
    part1 = point1 / value
    part2 = point2 - point1
    part3 = value - point2

    return [part1, part2, part3]


@app.route('/traffic', methods=['GET'])
def get_traffic():
    status = random.choice(["畅通", "拥堵"])
    average_speed_sc = random.randint(50, 70)
    average_speed_bc = random.randint(40, 50)

    big_car = random.randint(5, 15)
    small_car = random.randint(15, 25)
    carcount = big_car + small_car
    if status != "拥堵":
        safe = random.randint(1, 2)
    else:
        safe = 3
    parts = split_value_into_three(big_car)
    now = datetime.now()
    # 格式化时间
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
    # 返回JSON格式的时间

    data = {
        "status": status,
        "average_speed": average_speed_sc,
        "average_speed_bc": average_speed_bc,
        "safe": safe,
        "big_car": big_car,
        "small_car": small_car,
        "carcount": carcount,
        "time": formatted_time,
        "car": [
            {"value": '%.2f' % (parts[0] / carcount), "name": "货车"},
            {"value": '%.2f' % (parts[1] / carcount), "name": "危化品车"},
            {"value": '%.2f' % (parts[2] / carcount), "name": "大型客车"},
            {"value": '%.2f' % (small_car / carcount), "name": "客车"}
        ],
        "average_speed_sc1": [
            {
                "value": average_speed_sc
            }
        ],
        "average_speed_bc1": [
            {
                "value": average_speed_bc
            }
        ]

    }
    return jsonify(data)


@app.route('/status', methods=['GET'])
def get_status():
    total = 1200

    # 生成在线总数在1100-1250浮动
    online_fluctuating = random.randint(1100, 1150)

    # 计算离线总数，使得在线总数和离线总数之和等于1200
    offline_fluctuating = total - online_fluctuating

    # 生成故障数在10-20浮动
    faults = random.randint(10, 20)

    data = [
        {
            "name": "设备总数",
            "category1": total
        },
        {
            "name": "在线设备",
            "category1": online_fluctuating
        },
        {
            "name": "离线设备",
            "category1": offline_fluctuating
        },
        {
            "name": "故障设备",
            "category1": faults
        }
    ]

    return jsonify(data)


def generate_random_time_sequence(n):
    """
    生成包含 n 个随机时间的列表，这些时间在当天并且顺序排列
    """
    now = datetime.now()
    today_start = datetime(now.year, now.month, now.day)

    times = [today_start + timedelta(seconds=random.randint(0, int((now - today_start).total_seconds()))) for _ in
             range(n)]
    times.sort()  # 将时间排序
    return times


def generate_random_camera_name():
    """
    生成随机摄像机名称
    """
    camera_prefixes = ["摄像机A", "摄像机B", "摄像机C", "摄像机D", "摄像机E"]
    camera_number = random.randint(1, 20)  # 随机生成1到20之间的数字
    return f"{random.choice(camera_prefixes)}-{camera_number}"


def generate_alerts(num_alerts):
    alert_types = ["运动检测", "声音检测", "异常行为"]
    handling_statuses = ["已处理", "未处理"]

    # 生成按时间顺序排列的随机时间
    alert_times = generate_random_time_sequence(num_alerts)

    alerts = []
    for i in range(num_alerts):
        alert = {
            "dev_name": generate_random_camera_name(),  # 随机生成摄像头名称
            "event_info": "出现报警，请及时查看",
            "告警类型": random.choice(alert_types),
            "告警时间": alert_times[i].strftime('%Y-%m-%d %H:%M:%S'),
            "处理情况": random.choice(handling_statuses)
        }
        alerts.append(alert)

    return alerts


@app.route('/alerts', methods=['GET'])
def get_alerts():
    num_alerts = 10  # 生成 10 条告警信息
    alerts = generate_alerts(num_alerts)
    return jsonify(alerts)


@app.route('/data', methods=['GET'])
def get_data():
    data = generate_data()
    return jsonify(data)

@app.route('/data1', methods=['GET'])
def get_data1():
    data = generate_data1()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9799)
