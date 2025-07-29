number1 = int(input("Enter one integer:"))
number2 = int(input("Enter one integer:"))
number3 = int(input("Enter one integer:"))

if number1 < number2:
    smallest = number1
    middle = number2
    largest = number3

elif number2 > number3:
    middle = number2
    largest = number3
    smallest = number1

else:
    middle = number2
    largest = number3
    smallest= number1

print (smallest, middle, largest)
