def locateLargest(a):
    maxValue = a[0][0]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a [i][j]>=maxValue:
                maxValue = a[i][j]
                maxPosition = [i, j]
    return maxPosition

def main():
    rows = int(input("Enter the number of rows in the list: "))
    matrix = []

    for i in range (rows):
        rowInput = input(f"Enter row {i} :")
        row = [float(num) for num in rowInput.split()]
        matrix.append(row)
        location = locateLargest(matrix)

        print(f"The location of the largest element is at ({location[0]}, {location[1]})")

main()