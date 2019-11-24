# 第三章 案例：学生调查反馈数据分析

#导入所需的方法库
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#从Excel文件的5张表中读取数据
df1 = pd.read_excel('data\studentsInfo.xlsx','Group1',index_col=0)  
df2 = pd.read_excel('data\studentsInfo.xlsx','Group2',index_col=0)  
df3 = pd.read_excel('data\studentsInfo.xlsx','Group3',index_col=0)  
df4 = pd.read_excel('data\studentsInfo.xlsx','Group4',index_col=0)  
df5 = pd.read_excel('data\studentsInfo.xlsx','Group5',index_col=0)
#按行追加形式，拼接数据集
stu = pd.concat([df1,df2,df3,df4,df5], axis = 0)
print( 'Data Size:', stu.shape )

#去除重复行，且更新数据集
stu.drop_duplicates(inplace = True)
#删除有两个及以上缺失数据的行
stu.dropna(thresh=8,inplace = True )
print( 'Data Size after drop:', stu.shape )
#查看哪些列还有缺失数据
print( "Nan Columns:\n",stu.isnull().any() )

#填充缺失值
stu.fillna({'年龄':20, '成绩':stu['成绩'].mean()}, inplace=True )
print( "Nan Columns:\n",stu.isnull().any() )

#按照成绩排序
stu_grade = stu.sort_values(by='成绩', ascending=False)
#统计优秀和不及格人数
ex = (stu_grade['成绩']>=90 ).sum()   
fail = (stu_grade['成绩']<60 ).sum()
print("Excellent: {}, Fail: {}".format(ex,fail))

#计算全体成绩与课程兴趣平均值
ex_mean = stu_grade[0:9][['成绩','课程兴趣']].mean()
#计算优秀学生成绩与课程兴趣平均值
total_mean = stu_grade[['成绩','课程兴趣']].mean()
#计算不合格学生成绩与课程兴趣平均值
fail_mean = stu_grade[-4:][['成绩','课程兴趣']].mean()
print("ex_mean:\n", ex_mean, "\ntotal_mean\n",total_mean, "\nfail_mean\n", fail_mean)

#按照性别分组
sex_grouped = stu.groupby(['性别'])
#统计每个分组的行数
sex_counts = sex_grouped.count()
#分组统计成绩平均值
sex_mean = stu.groupby(['性别']).aggregate( {'成绩':np.mean } )
print(sex_counts, '\n', sex_mean)
pro_counts = stu.groupby(['省份']).count()
pro_mean = stu.groupby(['省份']).aggregate( {'成绩':np.mean } )
print(pro_counts, '\n', pro_mean)

#新增BMI列
stu['BMI'] = stu['体重'] / ( np.square(stu['身高']/100) )
print( stu['BMI'].quantile( [.25,0.5,.75] ) )
print('BMI>28 肥胖人数:',  (stu['BMI']>=28 ).sum() ) 

