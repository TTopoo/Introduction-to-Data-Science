import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd
from pandas import Series

data=Series([41.3,48.9,54.0,59.5,64.4,68.9,74.4], index=['2010','2011','2012','2013','2014','2015','2016'])

#例4-3 pandas绘图，matplotlib添加图元
data.plot(title='2010~2016 GDP',LineWidth=2, marker='o', linestyle='dashed',color='r',grid=True,alpha=0.9)
plt.annotate('turning point',xy=(1,48.5),xytext=(1.8,42), arrowprops=dict(arrowstyle='->'))
plt.text(1.8,70,'GDP keeps booming!',fontsize='larger')
plt.xlabel('Year',fontsize=12)
plt.ylabel('GDP: Trillion',fontsize=12)

#将绘制图形保存到文件
plt.savefig("2010-2016GDP.png",dpi=200,bbox_inches='tight')

plt.show()  #注意保存文件需在显示之前
