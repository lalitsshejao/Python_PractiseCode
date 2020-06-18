from functools import reduce    #import functools  or  from functools import *
#lambda argument : expression

x= lambda a : a*a
print(x(4))

#Lambda within User defined function

def a(x):
    return (lambda y : x + y )

t= a(8)
print (t(7))
u = a(10)
print(u(10))

#Lambda within filter()
#filter(function, iterables)
# Values present in the iterable are send to the function,
# the value which satisfies the function only that value from the iterable is returned.

mylist= [1, 2, 3, 4, 5, 6, 7, 8, 9]
newlist= list(filter(lambda a:(a%3 ==2),mylist))
list2= list(filter(lambda var:var%2 == 1, range(0, 10)))
print(newlist)
print ("Filter Funct List2 :", list2 )

#Lambda within map()
#map(function, iterable)
# Values present in the iterable are send to the function,
# the function is executed using that value as input and the output of the function is returned as output of map function.

mylist=[2,3,4,5,6,7,8,9,10]
newlist = list(map(lambda a: (a/3 == 2),mylist))
list2= list(map(lambda var:var*2, range(1, 10)))
print(newlist)
print("List2 Map Function : ", list2)

# Map takes all objects in a list and allows you to apply a function to it whereas
# Filter takes all objects in a list and runs that through a function to
# create a new list with all objects that return True in that function

#Lambda within reduce()
#reduce(function, sequence)
a= reduce(lambda a,b: a+b, range(1, 10))
print(a)


def new(a,b):
    return a*b

x= map(new, [1,2,3,4,5],[2,5,7,9,10])
#print(list(x))
print(tuple(x))

lst=[2,4,6,8,10,12]
y = list(map(lambda a: a*3,lst))
z = tuple(map(lambda a: a*3,lst))
print(y)
print(z)