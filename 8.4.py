def count(s, ch):
    total = 0
    for c in s:
        if c == ch:
            total += 1
    return total
string = input("Enter a string: ")
char = input("Enter a character to count: ")

occurences = count(string,char)

print(f"The character '{char}' appears '{occurences}' times in the string.")