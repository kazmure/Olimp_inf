import numpy as np

def enterTable():
    n = int(input("Введіть кількість рівнянь: "))
    A = np.zeros((n,n))
    b = np.zeros(n)
    for i in range(n):
        row = input(f"Введіть коефіцієнти {i+1} рядка, розділені пробілом: ")
        row_list = row.split()
        for j in range(n):
            A[i,j] = float(row_list[j])
        b[i] = float(row_list[n])
    return A, b

def writeTable(A, b):
    n = len(b)
    for i in range(n):
        row = ""
        for j in range(n):
            row += f"{A[i,j]:.2f}x{j+1} + "
        row = row[:-3]
        row += f"= {b[i]:.2f}"
        print(row)

def existSolve(A, b):
    n = len(b)
    if np.linalg.matrix_rank(A) != np.linalg.matrix_rank(np.c_[A,b]):
        return 0
    elif np.linalg.matrix_rank(A) == n:
        return 1
    else:
        return 2

def solve(A, b):
    return np.linalg.solve(A, b)

# Приклад використання функцій:
A, b = enterTable()
writeTable(A, b)
if existSolve(A, b) == 1:
    x = solve(A, b)
    print(f"Розв'язок: {x}")
elif existSolve(A, b) == 0:
    print("Система не має розв'язків.")
else:
    print("Система має безліч розв'язків.")
