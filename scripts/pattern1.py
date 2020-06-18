# s="0123456789"
# print(s[2:0:-1])
l1 = [10, 20, 30, 20, 20, 30, 40,  50, -20, 60, 60, -20, -20, 10]
size = len(l1)
duplicate=[]
for i in range (size):
    k = i + 1
    for j in range (k, size):
        if l1[i]==l1[j] and l1[i] not in duplicate:
            duplicate.append(l1[i])
print(duplicate)

final_list=[]
for x in l1:
    if x not in final_list:
        final_list.append(x)
print(final_list)