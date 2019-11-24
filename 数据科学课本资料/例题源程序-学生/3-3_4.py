import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-3：创建DataFrame对象
data = [[19,170,68],[20,165,65],[18,175,65]]
students = DataFrame(data, index=[1,2,3], columns=['age','height','weight'])  
print(students)

#例3-4：实现学生信息的查询、增加、删除和修改
#1. 学生信息查询
print(students.loc[ 1, 'age'])
print(students.loc[[1,3], ['height','weight']] )
print(students.iloc[[0,2],[0,1]])
print( students.loc[ : , ['height','weight']] )
print(students[['height','weight']])
print(students.iloc[1:, 0:2])
print(students[1:3 ] )

#筛选身高大于168的同学，显示其身高和体重值
mask = students['height']>=168
print( students.loc[ mask, ['height','weight'] ] )

#2. 增加学生信息
students['expense'] = [1500,1600,1200]
print(students)

#3. 修改学生信息
students['expense'] = 1000
print(students)
students.loc[1, :] = [21,188,70,20]
print(students)
students.loc[students['expense']<500, 'expense' ] = 1200
print(students)

#4. 删除学生信息
print( students.drop(1, axis=0) )
print( students.drop('expense', axis=1) )
print( students.drop([1, 2], axis=0) )
students.drop(['age','weight'], axis=1, inplace=True)
print(students)
