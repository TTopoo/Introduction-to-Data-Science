#例2-2：创建二维数组scores，记录 “names”中同学“subjects”的各门课程考试成绩。

#导入numpy
import numpy as np

names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])

#创建二维数组
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
print(scores)

#1. 查看数组属性
print(scores.ndim)  #数组维数
print(scores.size)  #数组元素总数，行×列
print(scores.shape)  #数组的行数和列数
print(scores.dtype)  #数组元素的类型

#2. 二维数组切片
print(scores[1,0])
print(scores[[1,3],[0,1]])
print(scores[[1,3]])
print(scores[: , [0,1]])
print(scores[ [0,3], 1:4 ])
print(scores[[1,3]][:,[0,1]])

#3. 条件筛选
print( scores[(names == '肖良英') | (names == '方绮雯'), :] )

print( scores[(names == '肖良英') | (names == '方绮雯')][:,(subjects == 'Math') | (subjects == 'Python')] )
