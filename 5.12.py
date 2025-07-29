'''Write a program the displays, ten numbers
per line, all numbers from 100 to 1000 that are diviasible by 5 and 6. the numbers are seperated by exactly one space'''

count = 0
for i in range(100,1000):
    if i % 5==0 and i % 6 == 0:
        print(i, end=" ")
        count+=1
        if count % 10 ==0:
            print()
