import pandas as pd
import numpy as np
from pandas import Series, DataFrame

def Get_info():
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    # 1.1读取数据
    print("1.1-读取数据")
    stu = pd.read_excel('studentsInfo.xlsx', 'Group1', index_col=0)
    print(stu)
    # 1.2案例教学这一列全部变成NaN
    print("1.2-案例教学这一列全部变成NaN")
    stu["案例教学"] = np.nan
    print(stu)
    # 1.3滤除缺失三列以上
    print("1.3-滤除缺失三列以上")
    print(stu.dropna(thresh=(10 - 3)))
    # 1.4滤除全部为NaN的列
    print("1.4-滤除全部为NaN的列")
    print(stu.dropna(axis=1, how="all"))

    # 2.1使用练习1的数据
    # stu = pd.read_excel('studentsInfo.xlsx','Group1',index_col=0)
    print("2.1-继承练习1的结果")
    print(stu)

    # 2.2使用列的平均值填充 体重 和 成绩 列的NaN数据
    print("2.2-使用列的平均值填充 体重 和 成绩 列的NaN数据")
    print(stu.fillna({'体重': stu['体重'].mean(), '成绩': stu['成绩'].mean()}, inplace=True))

    # 2.3使用上一行数据填充 年龄 列的NaN数据
    print("2.3-使用上一行数据填充 年龄 列的NaN数据")
    stu['年龄'].fillna(method='ffill', inplace=True)
    print(stu)

    # 2.4使用中位数填充 生活费用 列的NaN数据
    print("2.4-使用中位数填充 生活费用 列的NaN数据")
    print(stu.fillna({'月生活费': stu['月生活费'].median()}))
