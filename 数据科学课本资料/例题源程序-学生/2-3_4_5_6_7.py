#导入numpy
import numpy as np

#创建一维数组
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
#创建二维数组
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])


#例2-3：为所有同学的所有课程成绩增加5分
print( scores + 5 )

#例2-4：为各科目增加不同的基础分
bonus = np.array([3,4,5,3,6,7,2])
print( scores + bonus )

print( scores[names == '肖良英', subjects == 'English'])
print(scores[names == '肖良英', subjects == 'English'] + 5)

#例2-5: 将同学的考试成绩转换成整数形式的十分制分数
print( np.floor(scores/10) )


#例2-6：使用subtract函数为每个同学的分数减去3分
print( np.subtract(scores, 3) )

#例2-7：按照分析目标使用聚集函数进行统计
print( scores.sum(axis = 0) )
print( scores[names == '王微'].mean() )
print( names[ scores[:,subjects == 'English'].argmax() ] )
