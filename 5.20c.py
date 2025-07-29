
for j in range(0,6):
    for i in range ( 6 - j - 1):
        print(" ", end = " ")
    i = j +1
    while i >= 1:
        print(i , end="")
        i-=1
    print()