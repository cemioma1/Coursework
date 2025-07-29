#scores=eval(input("Enter scores:"))
#l1 =  scores.split()
#l2=[int (x) for x in l1]
#print(l2)

l2= [int(x) for x in input("Enter scores:").split()]

best=max(l2)
for i in range (len(l2)):
        if l2[i] >= best - 10:
            print(f"Student {i} score is {l2[i]} and grade is A")
        elif l2[i] >= best - 20:
            print()