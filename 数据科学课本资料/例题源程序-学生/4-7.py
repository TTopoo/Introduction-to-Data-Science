import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
import numpy as np

#3. 柱状图 
#例4-7：绘制出生人口性别比较图

data = pd.read_csv('data\population.csv', index_col ='Year') 
data1 = data[['Boys','Girls']]
mean = np.mean(data1,axis=0)      #计算均值
std = np.std(data1,axis=0)        #计算标准差     
#创建图
fig = plt.figure(figsize = (6,2)) #设置图片大小
plt.subplots_adjust(wspace = 0.6) #设置两个图之间的纵向间隔
#绘制均值的垂直和水平柱状图，标准差使用误差线来表示
ax1 = fig.add_subplot(1, 2, 1)
mean.plot(kind='bar',yerr=std,color='cadetblue',title = 'Average of Births', rot=45, ax=ax1)
ax2 = fig.add_subplot(1, 2, 2)
mean.plot(kind='barh',xerr=std,color='cadetblue',title = 'Average of Births', ax=ax2)
plt.show()


#绘制复式柱状图和堆叠柱状图
data1.plot(kind='bar',title = 'Births of Boys & Girls')
data1.plot(kind='bar', stacked=True,title = 'Births of Boys & Girls')
plt.show()
