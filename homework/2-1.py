import numpy as np
#step=int(input("Enter steps:"))
step=4
#标准正态分布
rndwlk=np.random.normal(0,1,size=(3,step))
print(rndwlk)
#三维空间的位置
position=rndwlk.cumsum(axis=1)
print(position)
#到原点的距离
dists=np.sqrt(position[0]**2+position[1]**2+position[2]**2)
print(dists)
#设置显示位数
np.set_printoptions(precision=2)
print(dists)
#z轴上的距离
zposition=position[2]
zposition=abs(zposition)
print(zposition.max())
#原点最近值
print(abs(dists.min()))

