import numpy as np
np.set_printoptions( precision = 4)   #只显示4位小数

#利用随机函数生成随机游走方向
rndwlk = np.random.randint(0, 2, size = (2,10))
rndwlk = np.where( rndwlk>0, 1, -1 )
print(rndwlk)

#计算每步后坐标
position = rndwlk.cumsum(axis = 1)
print (position)

#计算每步离原点的距离
dists = np.sqrt(position[0]**2 + position[1]**2)
print(dists)


#为轨迹序列增加起始原点
x = np.append(0, position[0])
y = np.append(0, position[1])

#绘制图形
import matplotlib.pyplot as plt
plt.plot(x,y, c='g',marker='*')     #画折线图
plt.scatter(0,0,c='r',marker='o')   #画原点
plt.text(.1, -.1, 'origin')   #添加原点说明文字
plt.scatter(x[-1],y[-1], c='r', marker='o')  #单独画终点
plt.text(x[-1]+.1, y[-1]-.1, 'stop')   #添加终点说明文字
plt.title('Plotting: The trajectory of a random walk') #添加图题
plt.show()   #显示图



