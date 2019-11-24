import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
import numpy as np
data = pd.read_csv('High-speed rail.csv',index_col ='Country')
data1 = data['Operation']
data2 = data['Under-construction']
data3 = data['Planning']
data4 = data[['Operation','Under-construction','Planning']]
data5 = data[['Latitude','Longitude']]

#1.各国运营里程对比柱状图，标记China为"Longest！"
fig = plt.figure(figsize = (20,20))
plt.subplots_adjust(wspace = 0.6)
ax1 = fig.add_subplot(3, 2, 1)
data1.plot(title='Operation Mileage',kind='bar',use_index=True,
           yticks=[0,5000,10000,15000,20000],ax=ax1)
plt.xlabel('Country',fontsize=12)
plt.ylabel('Mileage(km)',fontsize=12)
plt.annotate('Longest!',xy=(0,20000),xytext=(2,20000),arrowprops=dict(arrowstyle='->'))
#2.各国运营里程现状和发展堆叠柱状图
ax2 = fig.add_subplot(3, 2, 2)
data4.plot(title='Global trends of high-speed rail',kind='barh',stacked=True,use_index=True,
           ax=ax2)
plt.xlabel('Mileage(km)',fontsize=12)
plt.ylabel('Country',fontsize=12)
#3.各国运营里程占比饼图，China扇形离开中心点
ax3=fig.add_subplot(3,1,2)   #创建子图3
data1.plot(title='Opeartion Mileage',kind='pie',explode=[0.1,0,0,0,0,0],figsize=(6,6),shadow=True,
          startangle=60,autopct='%1.1f%%',ax=ax3)
plt.subplots_adjust(wspace=1,hspace=1)
plt.xlabel('',fontsize=12)
plt.ylabel('',fontsize=12)

plt.show()