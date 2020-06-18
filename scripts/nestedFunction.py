def outer():
    print("Hello")
    def inner():
        print("Inside inner")
    print("Bye")
    return inner

f1=outer()
print("*"*10)
f1()