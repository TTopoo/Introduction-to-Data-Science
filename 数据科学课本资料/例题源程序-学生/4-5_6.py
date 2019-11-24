import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

##例4-5：绘制散点图观察学生身高和体重之间的关系。
import pandas as pd
stdata = pd.read_csv('data\students.csv')      #读文件
stdata.plot(kind='scatter',x='Height',y='Weight',title='Students Body Shape', marker='*',grid=True, xlim=[150,200], ylim=[40,80], label='(Height,Weight)')    #绘图
plt.show()

#将数据按性别分组，分别绘制散点图
#将数据按男生和女生分组
data1= stdata[stdata['Gender'] == 'male']  #筛选出男生
data2= stdata[stdata['Gender'] == 'female']  #筛选出女生
#分组绘制男生、女生的散点图
plt.figure()
plt.scatter(data1['Height'],data1['Weight'],c='r',marker='s',label='Male')   
plt.scatter(data2['Height'],data2['Weight'],c='b',marker='^',label='Female') 
plt.xlim(150,200)                 #x轴范围
plt.ylim(40,80)              #y轴范围
plt.title('Student Body')    #标题
plt.xlabel('Weight')             #x轴标题
plt.ylabel('Height')             #y轴标题
plt.grid()                         #网格线
plt.legend(loc='upper right')  #图例显示位置
plt.show()

#例4-6: 绘制散点图矩阵观察学生各项信息
data = stdata[['Height', 'Weight','Age','Score']]  #准备数据
pd.plotting.scatter_matrix(data,diagonal='kde',color='k')  #绘图
plt.show()
