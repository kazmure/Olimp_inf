import tkinter as tk
import numpy as np

def enterTable():
    n = int(entry_n.get())
    A = np.zeros((n,n))
    b = np.zeros(n)
    for i in range(n):
        row = entry_rows[i].get()
        row_list = row.split()
        for j in range(n):
            A[i,j] = float(row_list[j])
        b[i] = float(row_list[n])
    return A, b

def writeTable(A, b):
    n = len(b)
    table = tk.Label(window, text="")
    for i in range(n):
        row = ""
        for j in range(n):
            row += f"{A[i,j]:.2f}x{j+1} + "
        row = row[:-3]
        row += f"= {b[i]:.2f}"
        table.config(text=f"{table['text']}\n{row}")
    table.pack()

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

def solve_system():
    A, b = enterTable()
    writeTable(A, b)
    if existSolve(A, b) == 1:
        x = solve(A, b)
        solution.config(text=f"Розв'язок: {x}")
    elif existSolve(A, b) == 0:
        solution.config(text="Система не має розв'язків.")
    else:
        solution.config(text="Система має безліч розв'язків.")

window = tk.Tk()
window.title("Розв'язування системи лінійних рівнянь")

frame_n = tk.Frame(master=window)
label_n = tk.Label(master=frame_n, text="Кількість рівнянь:")
entry_n = tk.Entry(master=frame_n)
label_n.pack(side=tk.LEFT)
entry_n.pack(side=tk.LEFT)
frame_n.pack()

frame_rows = tk.Frame(master=window)
label_rows = tk.Label(master=frame_rows, text="Коефіцієнти (4 числа):")
label_rows.pack(side=tk.LEFT)
entry_rows = []
n = 10
for i in range(n):
    row = tk.Entry(master=frame_rows)
    row.pack()
    entry_rows.append(row)
frame_rows.pack()

button_solve = tk.Button(master=window, text="Розв'язати", command=solve_system)
button_solve.pack()

solution = tk.Label(master=window, text="")
solution.pack()

window.mainloop()