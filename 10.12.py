list = [6, 12, 24, 6]
def gcdof2(num1, num2):
    gcd = 1
    for i in range(2, min(num1,num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        return gcd

def gcd(numbers):
    if len(numbers)== 1:

        return numbers[0]
    else:
        while len(numbers)>1:
            num1 = numbers.pop()
            num2 = numbers.pop()
            gcdresult=  gcdof2(num1,num2)
            numbers.append(gcdresult)

        return numbers [0]
print(gcd([6, 12,24, 24, 36]))