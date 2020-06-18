import numpy as np
import time
import sys

#Numpy consume less Space compare to list
s = range(1000)
print(sys.getsizeof(5) * len(s))

D = np.arange(1000)
print(D.size * D.itemsize)
print ("<--->"*10)

#Numpy are faster than list while processing the data
Size = 1000000
L1= range(Size)
L2= range(Size)

A1= np.arange(Size)
A2= np.arange(Size)

start = time.time()
result = [(x,y) for x,y in zip (L1,L2)]
print((time.time()-start)*1000)

start = time.time()
result = A1+A2
print((time.time()-start)*1000)
print ("<--->"*10)

#find the diamention of the array
#get item size
aa=np.array([1,2,3])
print("diamention of the array : ", aa.ndim)
print("Get Item size", aa.itemsize)
print("Data Type", aa.dtype)
print("Size", aa.size)
print("Shape", aa.shape)
print ("<--->"*10)


aa=np.array([(1,2,3,4,5,6),(4,5,6,3,2,4),(7,9,8,7,3,12)])
print("diamention of the array : ",aa.ndim)
print("Get Item size", aa.itemsize)
print("Data Type", aa.dtype)
print("Size", aa.size)
print("Shape", aa.shape)
print("Current Arrary Shape : \n",aa)
print("Reshape the Array : \n", aa.reshape(6,3))
print("1. Slicing : \n", aa[0,3])
print("2. Slicing : \n", aa[0:,3]) #3rd column value ineach row
print("3. Slicing : \n", aa[0:2,3]) #3rd column value ineach row
print("Linespacing : \n", np.linspace(1,4,6)) #it will devide the range (1,4) in equal spaces (6)
print("Max Element in the array : \n",aa.max())
print("Min Element in the array : \n",aa.min())
print("Sum of the array Element : \n",aa.sum())
print("Sum of the array Element axis=0 i.e Row sum : \n",aa.sum(axis=0))
print("Sum of the array Element axis=1 i.e Column sum : \n",aa.sum(axis=1))
print("Find the Square root of Each Element : \n",np.sqrt(aa))
print("Find the Standard Deviation of Each Element : \n",np.std(aa))

print ("<--->"*10)

#Arithmatic Operations

qq=np.array([(1,3,5,7), (2,4,6,8)])
rr=np.array([(1,3,5,7), (2,4,6,8)])
print("Addition of array Element : \n",qq+rr)
print("Substration of array Element : \n",qq-rr)
print("Multiplication of array Element : \n",qq*rr)
print("Divisition of array Element : \n",qq/rr)
print("Vartical Stacking of array Element : \n",np.vstack((qq,rr)))
print("Horizontal Stacking of array Element : \n",np.hstack((qq,rr)))
print("Convert array into single column : \n",qq.ravel())

print("Find the expenontial value : \n",np.exp(qq))
print("Find the Natural Log : \n",np.log(qq)) #log base e
print("Find the Log : \n",np.log10(qq))
