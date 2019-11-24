import matplotlib.pyplot as plt #导入matplotlib.pyplot
import pandas as pd

#例4-4 绘制函数图

import numpy as np                    #导入numpy
#生成x数组
x = np.linspace(0,6.28,50)   #start, end, num-points
y=np.sin(x)                     #计算y=sin(x)数组
plt.plot(x,y, color='r')      #用红色绘图y=sin(x)
plt.plot(x,np.exp(-x),c='b')  #用蓝色绘图y=exp(-x)
plt.show()


