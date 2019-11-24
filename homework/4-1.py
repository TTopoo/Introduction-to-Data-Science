import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

# 例4-1：pandas 绘图
from pandas import DataFrame

gdp = [1.47,1.62,1.78,1.94,2.38,2.60]
data = DataFrame({'Income':gdp}, index=['2012','2013','2014','2015','2016','2017'])

# pandas绘图参数设置
data.plot(title='Income chart',LineWidth=2, marker='o', linestyle='dashed',color='k', grid=True,alpha=0.9,use_index=True,yticks=[0.5,1.0,1.5,2.0,2.5,3.0])
plt.xlabel('Year',fontsize=12)
plt.ylabel('Income(RMB Ten Thousand)',fontsize=12)
plt.annotate('Largest!',xy=(5,2.60),xytext=(3,2.60),arrowprops=dict(arrowstyle='->'))
plt.show()
plt.savefig('1.png',dpi=400,bbox_inches='tight')

