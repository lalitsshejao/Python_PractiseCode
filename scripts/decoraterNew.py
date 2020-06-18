def deco(func):
    def inner(name):
        if name == "Sunny":
            print("Hello Sunny Go To Bed....")
        else:
            func(name)
    return inner
'''
@decor  - if used then whenever wish function is called then it will be executed as decor function.
So if we want to execute the wish function as it is and ececute the decorated function some times then 
remove @deco and 
decorefunc=deco(wish)
decorefunc("Sunny")
'''
# @deco
# def wish (name):
#     print("Hello", name, "Good Morning")

def wish (name):
    print("Hello", name, "Good Morning")

decorefunc=deco(wish)

decorefunc("Sunny")
wish("Sunny")
wish("AIM")
wish("ABCD")
print(" *" * 20)
#************************************

def smrtdivison(func):
    def inner(x,y):
        if y==0:
            print("its a wrong operation")
        else:
            return func(x,y)
    return inner

@smrtdivison
def division(a,b):
    return a/b

print(division(10,5))
print(division(10,0))
print(division(10,2))