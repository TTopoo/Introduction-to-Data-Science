import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
import numpy as np
import scipy
from pandas.plotting import scatter_matrix
data = pd.read_csv('bankpep.csv',index_col ='id')
data1 = data['age']
data2 = data[['age','income','children']]

#'''请取消注释查看
#1.客户年龄分布的直方图和密度图
data1.plot(title='Customer Age',density=True,kind='hist',style='r-')
data1.plot(kind='kde',xlim=[0,80],style='r-')
plt.xlabel('Age',fontsize=12)
plt.ylabel('Density',fontsize=12)
#'''

'''
#2.客户年龄和收入关系的散点图
data.plot(title='Customer Income',kind='scatter',x='age',y='income',marker='s',xlim=[0,80],grid=True)
plt.xlabel('Age',fontsize=12)
plt.ylabel('Income',fontsize=12)
plt.legend(['(age,income)'],loc='upper left')
'''
'''
#3.绘制散点图观察账户(年龄、收入、孩子数)之间的关系，对角线显示直方图
pd.plotting.scatter_matrix(data2,diagonal='hist',color='k')
plt.xlabel('',fontsize=14)
plt.ylabel('',fontsize=14)
'''
'''
#4.按区域展示平均收入的柱状图，并显示标准差
std = data.groupby(['region'])['income'].std()
mean = data.groupby(['region'])['income'].mean()
mean.plot(title='Customer Income',kind='bar',x=data.groupby(['region']),yerr=std)
plt.xlabel('Region',fontsize=12)
plt.ylabel('Customer Income',fontsize=12)
print('pp')
'''
'''
#5.多子图绘制：账户中性别占比饼图，有车的性别占比饼图，按孩子数的账户占比饼图
fig = plt.figure(figsize = (6,6))
plt.subplots_adjust(wspace = 0.2)
ax1 = fig.add_subplot(2, 2, 1)
data['sex'].value_counts().plot(title='Customer Sex',kind='pie',explode=[0,0],figsize=(6,6),shadow=True,
                                startangle=60,autopct='%1.1f%%',ax=ax1)
plt.xlabel('',fontsize=12)
plt.ylabel('sex',fontsize=12)

ax2 = fig.add_subplot(2, 2, 2)
mask= data.loc[:,'car']=='YES'
data.loc[mask,:].groupby('sex')['car'].value_counts().plot(title='Customer Car Sex',kind='pie',explode=[0,0],
                                                           figsize=(6,6),shadow=True,startangle=60,autopct='%1.1f%%',ax=ax2)
plt.xlabel('',fontsize=12)
plt.ylabel('sex',fontsize=12)

ax3 = fig.add_subplot(2, 2, 3)
data['children'].value_counts().plot(title='Customer Children',kind='pie',explode=[0,0,0,0],figsize=(6,6),
                                     shadow=True,startangle=60,autopct='%1.1f%%',ax=ax3)
plt.xlabel('',fontsize=12)
plt.ylabel('Children',fontsize=12)
'''
'''
#6.各性别收入的箱型图
data[['sex','income']].boxplot(by='sex',figsize=(6,6))
'''
plt.show()