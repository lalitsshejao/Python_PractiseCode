class student:
    def __init__(self,name,age,marks):
        ''' (A) Instance veriable are mostly declared in constructor'''
        self.sname=name
        self.sage=age
        self.smarks=marks

    def talk(self):
        """(B) If needed instance variable can be declared in Instance Method also """
        self.ab=222
        self.cd=333
        print("My name is ",self.sname)
        print("My age is: ", self.sage)
        print("My marks are: ", self.smarks)

s1=student("Sunny", 30,94) # at this point only variables present in (A) will be available
                            # as method is not initialized

print(s1.__dict__)  #this will print the complete information obout the Instance Varibales
                    # present in that object along with the corresponding value

s1.talk() # as method is initialized so Instance Variables defined in the method will be available

print(s1.__dict__) #Now both (A) and (B) instance variable will be available
print()
s2=student("XXX", 20,45)
print(s2.__dict__)
s2.talk()
print(s2.__dict__)
print(" *" *20)
print(s1.__dict__)
print(s2.__dict__)