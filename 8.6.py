'''Write a function that counts the number of letters in
a string using the following header:
def countLetters(s):
Write a test program that prompts the user to enter a string and displays the num-
ber of letters in the string'''
def countLetters(s):
    count= 0
    for char in s:
        if char.isalpha():
            count += 1
    return count

user_input = input("Enter a string:")
print("The number of letters in the string is:", countLetters(user_input))