'''
#Print sum of values
d=eval(input("Enter dictionary data: "))
s=sum(d.values())
print(s)
'''
"""
'''
Occurance of each letter present in string
'''
word=input("Enter string: ")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print("{} occurs {} times".format(k,v))
print()
print("Count of Vowels present in the String")
vov = {'a','e','i','o','u'}
v={}
for i in word:
    if i in vov:
        v[i]=v.get(i,0)+1
for k,v in sorted(v.items()):
    print("{} vowel appears {} times".format(k,v))
    
"""
#Enter Student details and Search for it...
n = int(input("Enter no of Students: "))
q={}
for i in range(n):
    name=input("Enter Student name: ")
    marks= int(input("Enter Students Marks: "))
    q[name]=marks
print(q)
while True:
    name=input("Enter student name to find: ")
    marks=q.get(name, -1)
    if marks== -1:
        print("Student Not Found")
    else:
        print("Student {} has {} marks".format(name,marks))
    opt=input("Do you want to search another student (Yes|No)")
    if opt=="No":
        print("Thanks")
        break
