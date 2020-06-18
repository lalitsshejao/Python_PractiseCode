f=range(6)
print ("List Comprehension", end=" :")
q=[x+2 for x in f]
print(q)
print ("Generator exp", end=" :")
r=(x+2 for x in f)
print(r)
for i in r:
    print(i)


#Fibonacci Series
print("<------ Fibonacci Series  ------>")
def fib():
    f,s =0,1
    while True:
        yield f
        f,s =s, f+s

for x in fib():
    if (x>=50):
        break
    print(x, end=" ")

#Number Stream
print("\r")
print ("<----- Number Stream ----->")
a= range (2,100,4)
b =(x for x in a)
print(b)
for y in b:
    print(y)

#SineWave
print("\r")
print ("<----- SineWave ----->")

import numpy as np
from matplotlib import pyplot as pt
import seaborn as sb

def s(flip=2):
    x= np.linspace(0,14,100)
    for i in range (1,10):
        yield(pt.plot (x, np.sin(x+i * .5)* (7-i)*flip))
        # pt.plot (x, np.sin(x+i * .5)* (7-i)*flip)

sb.set()
ss=s()
# s()
pt.show()

for y in ss:
    print (y)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
