def isPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

for i in range(2,10000):
    if isPrime(i):
        print(i,end = ' ')