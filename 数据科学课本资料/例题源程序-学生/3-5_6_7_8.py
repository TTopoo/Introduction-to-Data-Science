import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-5：从students1.csv文件读出数据
student = pd.read_csv( 'data\student1.csv ')
print(student[-3:])                 #显示最后3条数据
student = pd.read_csv( 'data\student1.csv ', index_col = 0 )   #将文件中的学生序号导入为行索引
print(student[:3])


#例3-6：从student2.txt文件中读取数据
colNames = ['性别','年龄','身高','体重','省份','成绩']
student = pd.read_csv('data\student2.txt', sep='\t', index_col=0, header=None, names= colNames ) 
print(student[:2])  #显示前面两条数据

#例3-7：将数据保存到out.csv文件
data = [[19,68,170],[20,65,165],[18,65,175]]
student = DataFrame(data,index=[1,2,3],columns=['age','weight','height']) 
student.to_csv('out.csv', mode='w', header=True, index=False)  #不包括行索引

#例3-8：从student3. xlsx文件名为“Group1”的页中读取数据
#将序号列作为index，跳过前3行
student = pd.read_excel( 'data\student3.xlsx', 'Group1', index_col=0, skiprows=3 )
print( student[:2])
