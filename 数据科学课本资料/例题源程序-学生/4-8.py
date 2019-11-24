import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
import numpy as np

##例4-8：绘制国民经济生产总值GDP和居民人均可支配收入Income的折线图

data = pd.read_csv('data\GDP.csv', index_col = 'Year')   
data.plot(title='GDP & Income',LineWidth=2,marker='o',linestyle='dashed', grid=True,use_index=True) #折线图
plt.show()
data.plot(logy=True,LineWidth=2,marker='o',linestyle='dashed',color='G') #半对数折线图
plt.show()

