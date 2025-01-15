import pandas as pd
from scipy.spatial.distance import cdist
def dddtest():
    import pandas as pd

    # 读取第一个Excel文件（设备中文名、X轴、Y轴）
    df1 = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/device_cmd_logo.xlsx')

    # 读取第二个Excel文件（设备ID、X轴、Y轴）
    df2 = pd.read_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/device_cmd_id.xlsx')

    # 初始化一个新的DataFrame用于存储匹配结果
    result_df = pd.DataFrame(columns=['设备类型名称', '设备ID', 'x轴', 'y轴'])

    # 计算两个数据框之间的距离矩阵
    distances = cdist(df1[['x轴', 'y轴']], df2[['x轴', 'y轴']])

    # 遍历第一个Excel的每一行
    for index, row in df1.iterrows():
        # 找到距离相等的所有索引
        equal_distance_indices = (distances[index] == distances[index].min()).nonzero()[0]

        # 在相等距离中选择 x 更接近的匹配项
        min_distance_index = min(equal_distance_indices, key=lambda i: abs(df2.iloc[i]['x轴'] - row['x轴']))

        # 将匹配结果添加到结果DataFrame
        result_df = pd.concat([result_df, pd.DataFrame({
            '设备类型名称': [row['设备类型名称']],
            '设备ID': [df2.iloc[min_distance_index]['设备ID']],
            'x轴': [row['x轴']],
            'y轴': [row['y轴']],
        })], ignore_index=True)


    # 将结果写入第三个Excel文件
    result_df.to_excel('/Users/ruanyunfeng/PycharmProjects/pythonProject2/device_cmd.xlsx', index=False)

if __name__ == '__main__':
    dddtest()
