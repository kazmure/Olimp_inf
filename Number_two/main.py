import math
import tkinter as tk
from tkinter import filedialog
import os


def solve_equations():
    initialdir = os.path.abspath(os.path.dirname(__file__))
    file_path = filedialog.askopenfilename(initialdir=initialdir, initialfile='data.txt')
    if not file_path:
        return

    with open(file_path, "r") as file:
        lines = file.readlines()

    output_text = ""
    for line in lines:
        coeffs = line.strip().split()
        a, b, c = float(coeffs[0]), float(coeffs[1]), float(coeffs[2])

        discr = b ** 2 - 4 * a * c

        if discr < 0:
            output_text += "{} {} {} не має розв'язків, x Є {}\n".format(a, b, c, {})
        elif discr == 0:
            x = -b / (2 * a)
            output_text += "{} {} {} є один розв'язок, x = {:.3f}\n".format(a, b, c, x)
        else:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            if math.isinf(x1) or math.isinf(x2):
                output_text += "{} {} {} існує безліч розв'язків, x Є R\n".format(a, b, c)
            else:
                output_text += "{} {} {} є два розв'язки, x1 = {:.3f}, x2 = {:.3f}\n".format(a, b, c, x1, x2)

    output.insert(tk.END, output_text)


root = tk.Tk()

title_label = tk.Label(root, text="Розв'язування квадратних рівнянь")
title_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

browse_button = tk.Button(button_frame, text="Обрати data.txs", command=solve_equations)
browse_button.pack(side=tk.LEFT)

quit_button = tk.Button(button_frame, text="Вихід", command=root.quit)
quit_button.pack(side=tk.RIGHT)

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()
