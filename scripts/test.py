intDigits= 12345
dict = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 4, 8: 7, 9: 6, 0: 6}
lst = [int(i) for i in str(intDigits)]
total = 0
for item in lst:
    print(item, end=" ")
    numb= (dict.get (item))
    total= total + numb
    print(total)
print(total)