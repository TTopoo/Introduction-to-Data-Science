import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-11：追加新行
#行数据合并
colName = ['学号', '姓名', '专业' ]      #列索引
data1 = [ ['202003101','赵成','软件工程'], ['202005114','李斌丽','机械制造'], ['202009111','孙武一','工业设计'] ]      #值列表
stu1 = DataFrame( data1, columns=colName )  #行索引自动生成
data2 = [ ['202003103','王芳','软件工程'], ['202005116','袁一凡','工业设计'] ]
stu2 = DataFrame( data2, columns=colName )
newstu = pd.concat([stu1,stu2], axis=0)   #axis=0，表示按行进行数据追加
print(newstu)

#例3-12 合并列
cardcol = ['ID','刷卡地点','刷卡时间','消费金额']
#data3 = [ ['202003101','一食堂',17], ['202003101','教育超市',25.2], ['202005113','图书馆'] ]
data3 = [ ['202003101','一食堂','20180305 1145',14.2], ['104574','教育超市','20180307 1730',25.2],['202003103','图书馆','20180311 1823'],['202005116','图书馆','20180312 0832'],['202005114','二食堂','20180312 1708',12.5],['202003101','图书馆','20180314 1345']]
card = DataFrame( data3, columns=cardcol )   #创建一卡通数据对象
print( pd.merge(newstu,card, how='left',left_on='学号',right_on='ID') ) #左连接

