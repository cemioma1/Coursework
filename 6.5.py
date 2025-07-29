num1 = eval(input("Enter a number:"))
num2 = eval(input("Enter a number:"))
num3 = eval(input("Enter a number:"))

def displaySortedNumbers(num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        if num2<=num3:
            print (num1,num2,num3)
        else:
            print (num1,num3,num2)
    elif num2 <= num1 and num2 <= num3:
        if num1 <=num3:
            print (num2, num2, num3)
        else:
            print (num2, num3, num1)
    else:
        if num1 <= num2:
            print (num3, num1, num2)
        else:
            print ( num3, num2, num1)
displaySortedNumbers(num1, num2, num3)


'''Chapter06: 1,4,5,10,12,18
Chapter07: 1,2,3,4
Chapter08: 1, 4, 6, 11, 13
Chapter10: 1, 2, 4, 7, 10, 12
Chapter11: 1, 2, 4, 5, 10, 13
Chapter14: 2, 8, 10, 11
'''