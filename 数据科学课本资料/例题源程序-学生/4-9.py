import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd


#例4-9：绘制学生成绩分布直方图
stdata = pd.read_csv('data\students.csv')      #读文件
stdata['Height'].plot(kind='hist',bins=6,title='Students Height Dstribution') #绘图
plt.show()

#6. 密度图（Kernel Density Estimate）
stdata['Height'].plot(kind='hist',bins=6,normed=True,title='Students Age Dstribution') #绘图
stdata['Height'].plot(kind='kde',title='Students Height Dstribution', xlim=[155,185],
style = 'k--')   #绘制密度图
plt.show()
