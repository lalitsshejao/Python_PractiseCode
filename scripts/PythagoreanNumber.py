from math import sqrt
n = int (input("Max number : "))
for a in range(1, n+1):
    for b in range(a, n):
        c_sqrt = a**2 + b**2
        c = int (sqrt(c_sqrt))
        if ((c_sqrt - c**2) == 0):
            print(a, b, c)