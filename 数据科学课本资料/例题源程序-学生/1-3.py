#1.3.3 函数和方法库

#3种方式导入库
import math
print('1',math.sqrt(5))

from math import sqrt
print('2',sqrt(5) )

from math import sqrt as sq
print('3',sq(5) )

#自定义函数
def say(message, times = 1):
    print(message * times)
say( 'Hello' ) 
say( 'World', 5 )
