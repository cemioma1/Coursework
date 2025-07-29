def sumMajorDiagonal(m):
      total = 0
      for i in range(len(m)):
            total +=m[i][i]
      return total
l1 = [int(x) for x in input("Enter a 4-by-4 row for row 1: ").split()]
l2 = [int(x) for x in input("Enter a 4-by-4 row for row 2: ").split()]
l3 = [int(x) for x in input("Enter a 4-by-4 row for row 3: ").split()]
l4 = [int(x) for x in input("Enter a 4-by-4 row for row 4: ").split()]

matrix = [l1, l2, l3, l4]

print("Sum of the elements in the major diagonal is", sumMajorDiagonal(matrix))

