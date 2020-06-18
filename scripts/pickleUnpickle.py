import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal,"\t", self.eaddr)

with open("emp.dat","wb") as f:
    e=Employee(100, "Lalit", 1000, "PUNE")
    pickle.dump(e,f)    #Emoployee object "e" is created and stoared in file "f"
    print("Saving Object Using Pickling")

with open("emp.dat","rb") as f:
    eobj=pickle.load(f)     #Employee object "e" is retrived and stoared in "eobj"
    print("Retriveing Object Using Unpickling")
    eobj.display()