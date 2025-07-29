'''(Display nonduplicate words in ascending order) Write a program that prompts
the user to enter a text file, reads words from the file, and displays all the nondu-
plicate words in ascending order'''

l1 = []
text = input("Enter text: ").split()
for word in text:
    if text.count(word) == 1:
        l1.append(word)

l1.sort()
for elem in l1:
    print(elem)