import random

generateMatrix =[]

for i in range(0,4):
    generateMatrix.append([])
    for j in range(0,4):
        generateMatrix[i].append(random.randint(0,1))


print(generateMatrix)


s = sum(generateMatrix[0])
largestSum = 0
for i in range (0,4):
    if sum(generateMatrix[i]):
        s= sum(generateMatrix[i])
        largestSum = i

print(largestSum)

s = (generateMatrix[0][0]) + generateMatrix[1][0] + generateMatrix[2][0] + generateMatrix[3][0]
k = 0
s2 = 0
for i in range (0,4):
    for j in range(0,4):
        s2 += generateMatrix[j][i]
    if s2 > s:
        s = s2
        k = i

print (k)


