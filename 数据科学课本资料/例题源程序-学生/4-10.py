import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

#例4-10：绘制各类广告投入占比的饼图
#准备数据（各类广告投入费用汇总）
data = pd.read_csv('data/advertising.csv')
piedata = data[['TV','Weibo','WeChat']]
datasum = piedata.sum()  
print(datasum)
#绘制饼图
datasum.plot( kind='pie', figsize=(6,6), title='Advertising Expenditure',fontsize=14,explode=[0,0.2,0],shadow=True,startangle=60, autopct='%1.1f%%')
plt.show()
