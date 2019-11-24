#例2-1 创建一维数组分别保存学生姓名和考试科目，访问数组元素。


#导入numpy
import numpy as np

#创建一维数据
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
print(names)
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
print(subjects)


#1. 查看数组的属性
print(names.ndim)  #数组维度
print(names.size)  #数组元素个数
print(names.dtype)  #数组数据类型


#2. 单个数组元素访问
print(names[2])
print(subjects[-3])


#3. 数组切片（slicing）
print( subjects[ [0,2,4] ] )
print(names[ 1:4 ])
print(subjects[ : -1:2])


#4. 根据条件筛选数组元素
print( names[ (names == '王微') | (names== '钱易铭') ] )

