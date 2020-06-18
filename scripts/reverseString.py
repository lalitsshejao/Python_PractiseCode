# string=input("Enter String :")
# n=len(string)
# i=0
# print("String In Forward Direction :")
# while i<n:
#     print(string[i],end="")
#     i=i+1
# print()
# print("String In Reverse Direction :")
# i=n-1
# while i>=0:
#     print(string[i], end="")
#     i = i - 1
#
# print()
# print("String In Reverse Direction :")
# i = -1
# while i >= -n:
#     print(string[i], end="")
#     i = i - 1
# print()


def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = words [:: -1]
    return reverse_sentence

if __name__ == "__main__":
    input = 'Hello world abcd qwerty dfghj xyz'
    print (rev_sentence(input))