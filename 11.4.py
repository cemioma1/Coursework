
employees =[[2,4,3,5,6],
            [2,4,30,5,6],
            [10,4,3,5,6]]

sumOfHours = []
for i in range(0, len(employees)):
    s = sum(employees[i])
    sumOfHours.append([s,"employee" + str(i)])
sumOfHours.sort(reverse =True)

for elem in sumOfHours:
    print(elem[1],"worked", elem[0])