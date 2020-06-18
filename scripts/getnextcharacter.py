'''
Enter the String: a3g4x2
o/p: adgkxz (a3 = bcd so d, g4 = hijk so k ....)

Enter the String: q3d7
o/p: qtdk

Enter the String: f1345
o/p: fgijk
'''
s=input("Enter the String: ")
output=''
for i in s:
    if i.isalpha():
        output = output + i
        previous = i
    else:
        newchar = chr (ord(previous) + int(i))
        output = output + newchar
print(output)