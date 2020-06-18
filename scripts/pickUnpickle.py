import pickEmp, pickle

f = open("empNew.csv","rb")
print("Employee Details: ")
while True:
    try:
        eobj=pickle.load(f)
        eobj.display()
    except EOFError:
        print("All Employee records completed")
        break
f.close()