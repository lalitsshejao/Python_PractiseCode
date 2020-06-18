l=[]
for i in range (101):
    if i%10==0:
        l.append(i)
print(l)
l.append(200)
print(l.index(200))

l.insert(-15, 99)
l.insert(50, 777)
print(l.index(99))
print(l.index(777))

x=[[10,20,30],[40,50,60],[70,80,90]]
print (x)
for i in x:
    print(i)
print("Element in Matrix style")
for i in range (len(x)):
    for j in range (len(x[i])):
        print(x[i][j], end=" ")
    print()