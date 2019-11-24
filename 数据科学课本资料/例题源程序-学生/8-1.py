#例8-1：绘制股票收盘价的时序图，并提取该时序数据的常用特征值。
import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif'] = ['SimHei']  #设置中文字体
#设置usecols，从文件中只读取指定列
df = pd.read_csv('data/stockPrice.csv', index_col = 0, usecols=[0,1])
print(df.describe())
#绘制时序图，并添加图元
df.plot(title='2017年某公司股票价格变化图', grid=True)
plt.xlabel('时间（天）')
plt.ylabel('股价 (美元)')
plt.show()  
