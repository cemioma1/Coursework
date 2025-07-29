
'''Chapter06: 1,4,5,10,12,18
Chapter07: 1,2,3,4
Chapter08: 1, 4, 6, 11, 13
Chapter10: 1, 2, 4, 7, 10, 12
Chapter11: 1, 2, 4, 5, 10, 13
Chapter14: 2, 8, 10, 11
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line'''
#6.1

def getPentagonalNumber(n):
    result = int(n * (3 * n - 1)// 2)
    return result
def main ():
    for n in range (1,101):
        print(getPentagonalNumber(n))
    else:
        print(getPentagonalNumber(n), " ", end= " ")
main()




