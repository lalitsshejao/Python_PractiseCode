import scipy
from scipy import cluster
from scipy import special
from scipy import integrate

a= special.exp10(2)
print(a)

b= special.exp2(2)
print (b)

c= special.sindg(90)
print(c)

print(special.cosdg(0))

print(scipy.integrate.quad(lambda x:special.exp10(x),0,1))

