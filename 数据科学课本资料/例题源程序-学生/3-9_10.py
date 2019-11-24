import pandas as pd
import numpy as np
from pandas import Series, DataFrame


#例3-9：滤除部分缺失数据，填充部分缺失数据。
stu = pd.read_excel('data\studentsInfo.xlsx','Group1',index_col=0) 
print( stu )

# 1. 缺失数据滤除
print(stu.dropna())
print(stu.dropna(thresh=8) )
# 2. 缺失数据填充
print( stu.fillna({'年龄':20, '体重':stu['体重'].mean()} ) )
print(stu.fillna(method='ffill') )           #每个空值用上一行同列的值填充

#例3-10：去除重复数据
stu = pd.read_excel('data\studentsInfo.xlsx','Group1',index_col=0)
print(stu.drop_duplicates() )


