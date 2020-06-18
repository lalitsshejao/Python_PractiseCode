import random
n = 40
is_present = int(n * random.random()) + 1
guess = 0
while guess != is_present:
    guess = int(input("New Number : "))
    if guess > 0:
        if guess > is_present:
            print("Number is too Large")
        elif guess < is_present:
            print("Number is too Small")
    else:
        print("Dont Give up")
        break
else:
    print("Congratulation you made it: ")
