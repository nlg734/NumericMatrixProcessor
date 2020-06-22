# processor.py
# by Natasha Graham


def matrix_sum(rows, columns, A, B):
    result = []
    for m in range(int(rows)):
        row_totals = []
        for n in range(int(columns)):
            row_totals.append(int(A[m][n]) + int(B[m][n]))
        result.append(row_totals)
    return result


def scalar_mult(rows, columns, A, c):
    result = []
    for m in range(int(rows)):
        row_totals = []
        for n in range(int(columns)):
            row_totals.append(c * int(A[m][n]))
        result.append(row_totals)
    return result


rowA, columnA = input().split()
matrix_A = []
for _a in range(int(rowA)):
    matrix_A.append(input().split())

'''rowB, columnB = input().split()
matrix_B = []
for _b in range(int(rowB)):
    matrix_B.append(input().split())

if rowA == rowB and columnA == columnB:
    new = matrix_sum(rowA, columnA, matrix_A, matrix_B)
    for row in new:
        print(*row, sep=" ")
else:
    print("ERROR")'''

mult = int(input())

new = scalar_mult(rowA, columnA, matrix_A, mult)
for row in new:
    print(*row, sep=" ")
