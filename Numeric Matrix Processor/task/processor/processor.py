# processor.py
# by Natasha Graham
import copy

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


def actual_transpose(row, column, matrix):
    result = []
    for m in range(int(column)):
        row_total = []
        for n in range(int(row)):
            row_total.append(0)
        result.append(row_total)

    for m in range(int(row)):
        for n in range(int(column)):
            result[n][m] = matrix[m][n]

    return result


def side_transpose(row, column, matrix):
    result = horizontal_transpose(matrix)
    result = vertical_transpose(result)
    result = actual_transpose(row, column, result)
    return result


def vertical_transpose(matrix):
    result = matrix

    for i in range(len(result)):
        result[i].reverse()

    return result


def horizontal_transpose(matrix):
    result = matrix

    for i in range(len(result) // 2):
        temp = result[i]
        result[i] = result[len(result) - i - 1]
        result[len(result) - i - 1] = temp

    return result


def transpose_matrices():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = int(input("Your choice:"))
    row, column = input("Enter matrix size:").split()
    print("Enter matrix:")
    matrix = take_matrix_input(row)

    new = []

    if choice == 1:
        new = actual_transpose(row, column, matrix)
    elif choice == 2:
        new = side_transpose(row, column, matrix)
    elif choice == 3:
        new = vertical_transpose(matrix)
    elif choice == 4:
        new = horizontal_transpose(matrix)

    print("The result is:")
    print_matrix(new)


def get_det(row, matrix):
    total = 0
    if int(row) == 1:
        return matrix[0][0]
    if int(row) == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
    for i in range(int(row)):
        sub_matrix = copy.deepcopy(matrix[1:])
        for line in sub_matrix:
            line.pop(i)
        total += pow(-1,i) * float(matrix[0][i]) * get_det(int(row) - 1, sub_matrix)
    return total


def get_cofactors(row, matrix):
    cofactors = []
    for i in range(int(row)):
        temp_row = []
        for j in range(int(row)):
            sub_matrix = copy.deepcopy(matrix)
            sub_matrix.pop(i)
            for line in sub_matrix:
                line.pop(j)
            temp_row.append(pow(-1, i + j) * get_det(int(row) - 1, sub_matrix))
        cofactors.append(temp_row)
    return cofactors


def inverse_matrix(row, matrix):
    det = get_det(row, matrix)
    if det == 0:
        print("This matrix doesn't have an inverse")
        return False
    cofactors = get_cofactors(row, matrix)
    inverse = scalar_mult(row, row, actual_transpose(row, row, cofactors), 1 / det)
    print("The result is:")
    print_matrix(inverse)
    return True


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
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
    elif choice == 4:
        transpose_matrices()
    elif choice == 5:
        row, column = input("Enter matrix size:").split()
        if row == column:
            print("Enter matrix:")
            matrix = take_matrix_input(row)
            det = get_det(row, matrix)
            print("The result is:\n" + str(det))
        else:
            print("The operation cannot be performed.")
    elif choice == 6:
        row, column = input("Enter matrix size:").split()
        if row == column:
            print("Enter matrix:")
            matrix = take_matrix_input(row)
            inverse_matrix(row, matrix)
        else:
            print("The operation cannot be performed.")
    elif choice == 0:
        break
