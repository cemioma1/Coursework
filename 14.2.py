'''(Count occurrences of numbers) Write a program that reads an unspecified num-
ber of integers and finds the ones that have the most occurrences. For example, if
you enter 2 3 40 3 5 4 –3 3 3 2 0, the number 3 occurs most often. Enter all num-
bers in one line. If not one but several numbers have the most occurrences, all of
them should be reported. For example, since 9 and 3 appear twice in the list 9 30
3 9 3 2 4, both occurrences should be reported.
'''

textfile = input("Enter a text string:")

text =[t for t in textfile.split(" ")]

noDupes = {}

for elem in text:
    if elem not in noDupes:
        noDupes[elem] = 1
    else:
        noDupes.pop(elem)
sorted = []
for i in noDupes.items():
    sorted.append(i[0])
sorted.sort()

print(sorted)