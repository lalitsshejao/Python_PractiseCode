'''
Various Places to declare static Variable
1. within class directly
2. Inside constructor using Class Name
3. Inside Instance Mentho by using Class Name
4. Inside classmethod by using cls variable or Class Name
5. Inside static method by using class name
6. from outside of the class by using classname

'''

class Test:
    a=10    # 1
    def __init__(self):
        b=20
        Test.c=30   #2

    def m1 (self):
        self.d = 40
        Test.e = 50     #3

    #4
    @classmethod
    def m2(cls):
        cls.f = 60
        Test.g = 70

    #5
    @staticmethod
    def m3():
        Test.h = 80

t=Test()
t.m1()
Test.m2()
Test.m3()
Test.i = 90     #6
print(Test.__dict__)
print()
print(t.a,t.c,t.e,t.f,t.g,t.h,t.i)
print(Test.a,Test.c,Test.e,Test.f,Test.g,Test.h,Test.i)