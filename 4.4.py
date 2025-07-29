import random
num1 = random.randint(0,99)
num2 = random.randint(0,99)
answer = num1 + num2
guess = eval(input("Enter sum of two integers:"))
if guess == answer:
    print ("True")
else:
    print ("False")
