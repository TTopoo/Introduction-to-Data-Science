import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
from pandas import Series

data=Series([1.47,1.62,1.78,1.94,2.38,2.60],index=['2012','2013','2014','2015','2016','2017'])
fig=plt.figure(figsize=(6,6)) #figsize定义图形大小
ax1=fig.add_subplot(2,2,1)   #创建子图1
#ax1.plot(data)               #用AxesSubplot绘制折线图
data.plot(title='Income chart',ax=ax1)
plt.xlabel('Year',fontsize=10)
plt.ylabel('Income',fontsize=10)
plt.xlim(0.6)
plt.ylim(1.5,2.5)

ax2=fig.add_subplot(2,2,2)   #创建子图2
data.plot(title='box-whisker plot',kind='box',fontsize='small',xticks=[],ax=ax2) #用pandas绘盒型
plt.xlabel('2012-2017',fontsize=10)
plt.ylabel('Income',fontsize=10)

ax3=fig.add_subplot(2,1,2)   #创建子图3
data.plot(title='bar chart',kind='bar',use_index=True,fontsize='small',ax=ax3)#用pandas绘柱状图
plt.xlabel('Year',fontsize=10)
plt.ylabel('Income',fontsize=10)
plt.legend(['Income'],loc='upper left')
plt.subplots_adjust(wspace=0.5,hspace=0.3)

plt.show()
