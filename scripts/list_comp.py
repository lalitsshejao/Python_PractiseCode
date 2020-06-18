# List Comprehension
'''
ex1
'''
name=["lalit", "sagar", "abcd", "xyz"]

l=[]
for person in name:
    l.append(person)
print(l)

print([person for person in name])

print([person + ' worked with me.' for person in name])

# Dictionary Comprehension

movies_and_rating = {"abc":3, "www": 5, "XXX": 8, "qqq": 9, "sss": 1}
print([movie for movie in movies_and_rating if movies_and_rating[movie] > 6])

print(" * " * 20)
l1=[x*x for x in range(1,21)]
l2=[x for x in l1 if x%2==0]
print(l1)
print(l2)
l3=[2**x for x in range(1,11)]
print(l3)

word = "the quick brown fox jumps over the lazy dog".split()
l5=[[w.upper(), len(w)] for w in word]
print(l5)