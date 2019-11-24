#导入numpy
import numpy as np

#例2-8：生成由10个随机整数组成的一维数组
print( np.random.randint(0,6,10) )
# #生成5×6的二维随机整数
rdm = np.random.randint(0, 2, size = (5,6))
print( rdm )

#例2-9：生成服从均值为0、方差为1的服从正态分布的4×5二维数组
rdm = np.random.normal( 0,1, size = (4,5) )
print( rdm )
