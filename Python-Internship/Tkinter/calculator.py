import tkinter as tk

def button_click(value):
    entry.insert(tk.END, value)
def calculate():
    exp=entry.get()
    result = eval(exp)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
def clear():
    entry.delete(0, tk.END)    

screen = tk.Tk()
screen.title("Calculator")
screen.configure(bg='black')


entry = tk.Entry(width=20,bg='White',fg="Black", font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('*', 4, 1), ('/', 4, 2)
]

for label, row, col in buttons:
    button = tk.Button(text=label,bg='black',fg="White", padx=20, pady=20, font=('Arial', 20), command=lambda label=label: button_click(label))
    button.grid(row=row, column=col)
    
calculate = tk.Button(text='=', padx=20, pady=20,bg='White',fg="black", font=('Arial', 20), command=calculate)
calculate.grid(row=4, column=3)
clear = tk.Button(text='C', padx=18, pady=20,bg='Red',fg="White", font=('Arial', 20), command=clear)
clear.grid(row=3, column=3)
screen.mainloop()
