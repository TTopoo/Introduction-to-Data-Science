import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-13：对“成绩”进行排序分析
#值排序
stu = pd.read_excel('data\studentsInfo.xlsx','Group3',index_col=0)  #导入excel数据
print( stu.sort_values(by='成绩', ascending=False) )           #按成绩降序排列
print( stu.sort_values(by=['身高','体重'], ascending=True) )

#例3-14：对成绩数据降序排名，增加“成绩排名”列
#排名
stu['成绩排名'] = stu['成绩'].rank(method='min', ascending=False) 
print( stu )
