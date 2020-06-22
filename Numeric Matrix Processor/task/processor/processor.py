# processor.py
# by Natasha Graham


def take_matrix_input(row):
    matrix = []
    for _a in range(int(row)):
        matrix.append(input().split())
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=" ")
    return


def matrix_sum(rows, columns, A, B):
    result = []
    for m in range(int(rows)):
        row_totals = []
        for n in range(int(columns)):
            row_totals.append(float(A[m][n]) + float(B[m][n]))
        result.append(row_totals)
    return result


def scalar_mult(rows, columns, A, c):
    result = []
    for m in range(int(rows)):
        row_totals = []
        for n in range(int(columns)):
            row_totals.append(c * float(A[m][n]))
        result.append(row_totals)
    return result


def matrix_mult(rA, cA, cB, mA, mB):
    result = []
    for m in range(int(rA)):
        row_totals = []
        for n in range(int(cB)):
            row_totals.append(0)
        result.append(row_totals)

    for m in range(int(rA)):
        for n in range(int(cB)):
            for k in range(int(cA)):
                result[m][n] += float(mA[m][k]) * float(mB[k][n])
    return result

while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice:"))

    if choice == 1:
        rowA, columnA = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        matrix_A = take_matrix_input(rowA)
        rowB, columnB = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        matrix_B = take_matrix_input(rowB)

        if rowA == rowB and columnA == columnB:
            new = matrix_sum(rowA, columnA, matrix_A, matrix_B)
            print("The result is:")
            print_matrix(new)
        else:
            print("The operation cannot be performed.")
    elif choice == 2:
        rowA, columnA = input("Enter size of matrix:").split()
        print("Enter matrix:")
        matrix_A = take_matrix_input(rowA)
        constant = float(input("Enter constant:"))
        new = scalar_mult(rowA, columnA, matrix_A, constant)
        print("The result is:")
        print_matrix(new)
    elif choice == 3:
        rowA, columnA = input("Enter size of first matrix:").split()
        print("Enter first matrix:")
        matrix_A = take_matrix_input(rowA)
        rowB, columnB = input("Enter size of second matrix:").split()
        print("Enter second matrix:")
        matrix_B = take_matrix_input(rowB)

        if columnA == rowB:
            new = matrix_mult(rowA, columnA, columnB, matrix_A, matrix_B)
            print("The result is:")
            print_matrix(new)
        else:
            print("The operation cannot be performed.")
    elif choice == 0:
        break
