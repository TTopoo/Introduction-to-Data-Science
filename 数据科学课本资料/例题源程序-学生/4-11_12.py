import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

#例4-11：绘制各类广告投入的箱须图

data = pd.read_csv('data\Advertising.csv')
advdata = data[['TV','Weibo','WeChat']]
advdata.plot(kind='box', figsize=(6,6), title='Advertising Expenditure')
plt.show()

#按性别绘制学生体重的箱须图
stdata = pd.read_csv('data\students.csv')
stdata1 = stdata[['Gender','Score']]
stdata1.boxplot(by='Gender',figsize=(6,6))
plt.show()
