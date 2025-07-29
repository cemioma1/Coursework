
vowels ={'A','E','I','O','U','a','e','i','o','u'}

userString = input("Enter a string:")

vowelCount = 0
consonantCount = 0

for char in userString:
    if char in vowels:
        vowelCount += 1
    else:
        consonantCount +=1
print (f"The number of vowels in string is: {vowelCount}")
print (f"The number of consonants in string is : {consonantCount}")
