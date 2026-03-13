import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x220")
window.configure(bg="pink")

def add():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result = n1 + n2
    result_label.config(text=f"The sum of {n1} + {n2} is {result}")

def subtract():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result = n1 - n2
    result_label.config(text=f"The difference of {n1} - {n2} is {result}")

def multiply():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result = n1 * n2
    result_label.config(text=f"The product of {n1} * {n2} is {result}")

def divide():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    if n2 != 0:
        result = n1 / n2
        result_label.config(text=f"The division of {n1} / {n2} is {result}")
    else:
        result_label.config(text="Cannot divide by zero")

result_label = tk.Label(window, text="Simple Calculator")
result_label.grid(row=0, column=1, columnspan=10, pady=0)

label1 = tk.Label(window, text="Enter 1st Number:")
label1.grid(row=1, column=0)

label2 = tk.Label(window, text="Enter 2nd Number:")
label2.grid(row=2, column=0)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=1)

entry2 = tk.Entry(window)
entry2.grid(row=2, column=1)

add_btn = tk.Button(window, text="Add", command=add)
add_btn.grid(row=3, column=0, pady=5)

sub_btn = tk.Button(window, text="Subtract", command=subtract)
sub_btn.grid(row=3, column=1, pady=5)

mul_btn = tk.Button(window, text="Multiply", command=multiply)
mul_btn.grid(row=4, column=0, pady=5)

div_btn = tk.Button(window, text="Division", command=divide)
div_btn.grid(row=4, column=1, pady=5)

window.mainloop()
