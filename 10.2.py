'''Reverse the numbers entered) Write a program that reads a list of integers and
displays them in the reverse order in which they were read.'''

numbers = [int(x)for (x) in input("Enter numbers: ").split()]

print("Numbers in reverse order:")
for n in reversed(numbers):
    print(n, end= " ")
