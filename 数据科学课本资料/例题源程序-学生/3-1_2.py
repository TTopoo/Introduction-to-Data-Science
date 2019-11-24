import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#例3-1：创建5名篮球运动员身高的Series结构对象height，值是身高，索引为球衣号码。

height=Series([187,190,185,178,185],index=['13','14','7','2','9'])   #index为字符串
print("1:\n",height)
#也可以采用字典创建
#height1=Series({'13':187,'14':190,'7':185,'2':178,'9':185})
#print("2:\n",height1)

#例3-2：实现球员数据的查询、增加、删除和修改。

# 1. 球员身高查询
print(height['13']  )
print(height[ ['13','2','7'] ] )
print(height[1:3] )
print(height[ height.values>=186 ])

# 2. 球员身高修改
height['13'] = 188
print(height['13'])
height[1:3] = 160
print(height)

#3. 增加新球员
a = Series([190,187], index=['23','5'])
newheight = height.append( a )
print(newheight)
print(height)

#4. 删除离队球员
newheight = height.drop( ['13','9'] ) 
print(newheight)

#5. 更改球员球衣号码
height.index=[1,2,3,4,5]
print(height)

#数字索引，基于位置的访问
height=Series([187,190,185,178,185],index=[13,14,7,2,9])
print(height )
print(height[ [14,7] ])  #使用索引访问
print(height.iloc[0])   #基于位置的访问
