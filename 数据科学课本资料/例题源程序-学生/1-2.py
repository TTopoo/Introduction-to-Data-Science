#1.3.2 流程控制

# indent
from random import random
from math import sqrt

DARTS = 1000
hits = 0
for i in range(1,DARTS):
    x, y = random(), random()
    distance = sqrt(x**2 + y**2)
    if distance <= 1.0:
        hits += 1
pi = 4 *(hits/DARTS)
print("Pi = ", pi )

#This is the comment
"""
This is a multiline comment
In Python
"""

#格式化输入输出
s = input("姓名和年龄: ")
name,age = s.split(",")  #切分字符串
print(name,age)   #屏幕输出
print("name:{}, age:{}".format(name,age))   #格式化输出

#select structure
t = eval(input("输入通话时间：") )
if t>100:
    s = 20 + 0.4*(t-100)
elif t>50:
    s = 10 + 0.2*(t-50)
else:
    s = 10
print("费用: ",s)

# Loop structure: for
s = 0
for i in [1,3,5,7,9]:
    s += i
print( s )

#range function
for i in range(0, 10, 2):
    print(i)


# Loop structure: while
sum = 0
x = input("Input a number (<Enter> '' to quit): ") 
while x != "":
    sum = sum + eval(x)
    x = input("Input a number (<Enter> '' to quit): ")
print ("The sum is", sum )


