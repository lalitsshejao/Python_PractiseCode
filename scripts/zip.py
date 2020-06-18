list1 = [1,2,3,4,5]
list2= ["one", "two", "three", "four", "Five"]
list3 = ['abc','www','xxx,','zzz', 'ooo']
zipped = list(zip(list3, list2, list1))
# print(zipped)

unzipped = list(zip(*zipped))
# print(unzipped)

sentances=[]
for (l1, l2, l3) in zip(list1, list2, list3):
    l1, l2, l3 = str(l1), str(l2), str(l3)
    sentence = "Hello world " + l1 + ' ' + l2 + " how are you" 
    sentances.append(sentence)
    
print(sentances)