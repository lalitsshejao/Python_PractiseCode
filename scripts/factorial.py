num = int(input("Enter number : "))
fact =1
if num < 0:
    print("Number must be positive")
elif num == 0:
    print("Factorial = 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
        print(i,  fact)
print(fact)

'''
Recursive functions
'''
print("*" * 10)

def factorial(n):
    if n==0:
        result =1
    else:
        result= n * factorial(n-1)
    return result

print(factorial(5))