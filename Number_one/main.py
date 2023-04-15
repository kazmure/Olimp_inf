import tkinter as tk

def f(x):
    if x <= 0:
        return (-0.5 * x) + 3
    elif x > 0 and x <= 4:
        return ((x ** 3) - (7 * (x ** 2)) + (15 * x) - 9) / (x - 3)
    else:
        return 1 / (12 * x)

def print_table():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        h = float(h_entry.get())
        x = a
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "x\tf(x)\n-------------------------\n")
        while x <= b:
            try:
                fx = f(x)
                result_text.insert(tk.END, "{:.3f}\t{:.3f}\n".format(x, fx))
            except:
                result_text.insert(tk.END, "{:.3f}\tне існує\n".format(x))
            x += h
    except:
        result_text.insert(tk.END, "Помилка: Значення не заповнені\n")

window = tk.Tk()
window.title("Таблиця значень функції f(x)")

a_label = tk.Label(text="Початкове значення (a): ")
a_entry = tk.Entry()
b_label = tk.Label(text="Кінцеве значення (b): ")
b_entry = tk.Entry()
h_label = tk.Label(text="Крок (h): ")
h_entry = tk.Entry()

print_button = tk.Button(text="Ввести в таблицю", command=print_table)

result_text = tk.Text(width=30, height=20)

a_label.grid(row=0, column=0)
a_entry.grid(row=0, column=1)
b_label.grid(row=1, column=0)
b_entry.grid(row=1, column=1)
h_label.grid(row=2, column=0)
h_entry.grid(row=2, column=1)
print_button.grid(row=3, column=0, columnspan=2)
result_text.grid(row=4, column=0, columnspan=2)

window.mainloop()