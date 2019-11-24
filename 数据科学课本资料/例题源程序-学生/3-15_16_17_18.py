import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-15：BMI指数分析
stu = pd.read_excel('data\studentsInfo.xlsx','Group3',index_col=0)  #导入excel数据
print(stu[ :2])
stu['BMI'] = stu['体重'] / ( np.square(stu['身高']/100) ) 
print(stu[ :3])

#例3-16：对“成绩”、“月生活费”进行统计分析
print(stu['成绩'].mean())
print(stu['月生活费'].quantile( [.25, .75] )  )
print(stu[['身高','体重','成绩']].describe() )

#例3-17:对“身高”、“月生活费”按“性别”进行分组统计
grouped = stu.groupby(['性别', '年龄']) 
print( grouped.aggregate( {'身高':np.mean, '月生活费':np.max } ) )

#类似Excel交叉表crosstab
print( pd.crosstab( stu['性别'], stu['月生活费']) )

#例3-18：学生“身高”、“体重”与“成绩”之间的相关性分析
print(stu['身高'].corr( stu['体重'] ) )
print(stu[['身高','体重','成绩'] ].corr() )
