import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create and place the buttons
buttons = [
    ('7', 1, 0, 'light gray'), ('8', 1, 1, 'light gray'), ('9', 1, 2, 'light gray'), ('/', 1, 3, 'orange'),
    ('4', 2, 0, 'light gray'), ('5', 2, 1, 'light gray'), ('6', 2, 2, 'light gray'), ('*', 2, 3, 'orange'),
    ('1', 3, 0, 'light gray'), ('2', 3, 1, 'light gray'), ('3', 3, 2, 'light gray'), ('-', 3, 3, 'orange'),
    ('0', 4, 0, 'light gray'), ('.', 4, 1, 'light gray'), ('+', 4, 2, 'orange'), ('=', 4, 3, 'green'),
]

for (text, row, col, color) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, bg=color, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, bg=color, command=lambda t=text: click_button(t)).grid(row=row, column=col)

tk.Button(root, text="Clear", padx=20, pady=20, bg='red', command=clear_entry).grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
