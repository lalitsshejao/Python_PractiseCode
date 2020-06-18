''' Variable Length Arguments'''
def sum(*n):
    result=0
    for x in n:
        result=result + x
    print("Sum of the data is :", result)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)

def add(*n, name):
    result=0
    for x in n:
        result=result + x
    print("Sum of the data is :", result)

add(name="abcd")
add(10, name="xyz")
add(10,20,40,name="pqr")
