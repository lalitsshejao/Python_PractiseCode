import pickEmp, pickle

f = open("empNew.csv","wb")
n= int(input("Enter no of Empoloyee: "))
for i in range (n):
    eno=int(input("Enter Emp no: "))
    ename=input("Enter Emp name: ")
    esal=int(input("Enter Emp sal: "))
    eaddr=input("Enter Emp address: ")
    e=pickEmp.Employee(eno, ename, esal, eaddr)
    pickle.dump(e,f)

