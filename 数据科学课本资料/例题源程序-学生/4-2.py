import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

#matplotlib 精细绘图
plt.figure()   #创建绘图对象  
GDPdata=[41.3,48.9,54.0,59.5,64.4,68.9,74.4]    #准备绘图的序列数据
plt.plot(GDPdata,color="red",linewidth=2,linestyle='dashed',marker='o',label='GDP')    #绘图
#精细设置图元
plt.title('2010~2016 GDP: Trillion')
plt.xlim(0,6)          #x轴绘图范围
plt.ylim(35,75)      #y轴绘图范围
plt.xticks(range(0,7),('2010','2011','2012','2013','2014','2015','2016')) #将x轴刻度映射为字符串
plt.legend(loc='upper right')      #在右上角显示图例说明
plt.grid()       #显示网格线
plt.show()

#例4-2：多子图绘制
from pandas import Series
data=Series([41.3,48.9,54.0,59.5,64.4,68.9,74.4], 
index=['2010','2011','2012','2013','2014','2015','2016'])
fig=plt.figure(figsize=(8,6)) #figsize定义图形大小
ax1=fig.add_subplot(2,1,1)   #创建子图1 
ax1.plot(data)               #用AxesSubplot绘制折线图
ax2=fig.add_subplot(2,2,3)   #创建子图2 
data.plot(kind='bar',use_index=True,fontsize='small',ax=ax2)#用andas绘柱状图
ax3=fig.add_subplot(2,2,4)   #创建子图3 
data.plot(kind='box',fontsize='small',xticks=[],ax=ax3) #用pandas绘柱状图

#将绘制图形保存到文件
plt.savefig('2010-2016GDP.jpg',dpi=400,bbox_inches='tight')
plt.show()  #注意保存文件需在显示之前

