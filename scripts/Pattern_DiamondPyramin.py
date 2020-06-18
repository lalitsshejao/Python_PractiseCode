def diamondPyramid(n):
    k = 2* n -2
    for i in range (0, n):
        for j in range (0, k):
            print(end=" ")
        k = k - 1
        for j in range (0, i+1):
            print("* ", end="")
        print("\r")
    k = n - 2
    for i in range(n, -1, -1):
        for j in range(k, 0 , -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


diamondPyramid(10)

def diamondStar(n):
    for i in range (0, n):
        for j in range (0, n):
            if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
                print("*", end= "")
            else:
                print(end=" ")
        print()

diamondStar(5)