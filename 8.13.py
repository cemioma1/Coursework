def prefix(s1,s2):
    pre = ""
    for i in range(min(len(s1),len(s2))):
        if s1[i] == s2 [i]:
            pre += s1[i]
        else:
            break
    return pre
def main():
        s1=input("Enter a string:")
        s2=input("Enter a string:")

        answer= prefix(s1, s2)
        print(answer)

main()
