'''(Sum elements column by column) Write a function that returns the sum of all the
elements in a specified column in a matrix using the following header:
def sumColumn(m, columnIndex):
Write a test program that reads a matrix and displays the sum of each col-
umn. Here is a sample run:
3 * 4
Enter a 3-by-4 matrix row for row 0:
Enter a 3-by-4 matrix row for row 1:
Enter a 3-by-4 matrix row for row 2:
Sum of the elements for column 0 is 16.5
9.5 1 3 1
5.5 6 7 8
1.5 2 3 4'''

def sumColumn(m, columnIndex):
    total = 0
    for row in m:
        total += row[columnIndex]
    return total
def main ():
    rows = 3
    columns = 4
    matrix = []

    for i in range(rows):
        rowInput = input(f"Enter a 3-by-4 matrix row for row{i}: ")
        row = [float(num) for num in rowInput.split()]
        matrix.append(row)

    for column in range(columns):
        print(f"Sum of the elements for column {column} is {sumColumn(matrix, column)} ")
main()