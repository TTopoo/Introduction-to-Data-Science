#1.3.1 常用数据类型

#数值型
print(3+5 == 6)

# String
first = 'Python Programming'
second = 92.5
print(first + "：" + str(second) )

#Tuple
t = ( 'Lucy', ('Math', 90) )
print(t)
print(t[1][1])

#List
ls = []
ls.append(1)
ls.append('wang')
print(ls)
ls[0] = 2
print(ls)

#Dictonary
d = dict(name="Lucy",age=8,hobby=("bike","game"))
print(d)
print( d["hobby"] )

d["age"] = 9
d["gender"] = "F"
print(d)
del d['hobby']
print(d)
