import numpy as np

C=np.array(["大润发","沃尔玛","好德","农工商"])
S=np.array(["苹果","香蕉","橘子","芒果"])

x=np.random.uniform(4,10,[4,4])
print(x)

print(x[C=="大润发",S=="苹果"])
print(x[C=="好德",S=="香蕉"])

x[C=="大润发",S=="苹果"]=x[C=="大润发",S=="苹果"]+1
x[C=="好德",S=="香蕉"]=x[C=="好德",S=="香蕉"]+1

print(x)

x[C=="农工商",:]=x[C=="农工商",:]-2

print(x)
print('\n')
print(np.mean(x[:,S=="苹果"],axis=0))
print(np.mean(x[:,S=="芒果"],axis=0))
print('\n')

print(S[np.argmax(x[:,S=="橘子"],axis=0)])
