from functools import reduce
#linear Equation
s= lambda a : a**2
print(s(4))

#3x+4y
s= lambda x,y : 3*x+4*y
print(s(10,5))

#quadratic equation
# (a+b)^2
x= lambda a,b : (a+b)**2
print(x(3,4))


#Filter() with map()
c=map(lambda x: x*x, filter(lambda x:x>3, [2,3,4,5,6]))
print (tuple(c))

#map() with filter()
d=filter(lambda x:x>8,map(lambda x: x*x,[2,3,4,5,6]))
print (tuple (d))

#map() and filter() within reduce()
r= reduce(lambda x,y: x+y, map(lambda x: x+x, filter (lambda x: x<=4, [2,3,4,5,6])))
print (r)
#step1, first filter function wll return 2,3,4 from list
#Step2, map function will returm 4,6,8
#Step3, reduce function will add them to give o/p as 18