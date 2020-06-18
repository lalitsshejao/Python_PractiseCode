'''
Enter the String: a7f5c8k4
o/p : aaaaaaafffffcccccccckkkk
'''

s=input("Enter the String: ")
output=''
for i in s:
    if i.isalpha():
        output = output + i
        previous = i
    else:
        output = output + previous * (int(i) - 1)
print(output)
