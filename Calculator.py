from tkinter import *

# Main window setup
app = Tk()
app.title("Neon Dark Calculator")
app.config(bg="#121212")
app.resizable(False, False)

# Global variables
expression = ""
operation = ""
last_operation = ""

# Functionality
def click(num):
    entry_field.insert(END, str(num))

def add(): calculate("add")
def subtract(): calculate("subtract")
def multiply(): calculate("multiply")
def divide(): calculate("divide")

def calculate(op):
    global expression, operation
    expression = entry_field.get()
    operation = op
    entry_field.delete(0, END)
    update_history(f"{expression} {op_symbols[op]}")

def equal():
    global expression, operation
    try:
        second = entry_field.get()
        result = 0
        first_num = float(expression)
        second_num = float(second)

        if operation == "add":
            result = first_num + second_num
        elif operation == "subtract":
            result = first_num - second_num
        elif operation == "multiply":
            result = first_num * second_num
        elif operation == "divide":
            if second_num == 0:
                entry_field.delete(0, END)
                entry_field.insert(0, "Error: Div by 0")
                return
            result = first_num / second_num

        entry_field.delete(0, END)
        entry_field.insert(0, int(result) if result.is_integer() else round(result, 5))
        update_history(f"{expression} {op_symbols[operation]} {second} = {result}")

    except:
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")
        update_history("Error")

def clear():
    entry_field.delete(0, END)
    update_history("")

def backspace():
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, current[:-1])

def dot():
    current = entry_field.get()
    if '.' not in current:
        entry_field.insert(END, '.')

def update_history(text):
    history_label.config(text=text)

# Keyboard Bindings
def keypress(event):
    key = event.char
    if key.isdigit():
        click(key)
    elif key == '+': add()
    elif key == '-': subtract()
    elif key == '*': multiply()
    elif key == '/': divide()
    elif key == '.': dot()
    elif key == '\r': equal()
    elif key == '\x08': backspace()

# Operator symbols
op_symbols = {"add": "+", "subtract": "-", "multiply": "×", "divide": "÷"}

# Entry field
entry_field = Entry(app, width=25, justify="right", font=("Consolas", 22, 'bold'),
                    borderwidth=4, bg="#1E1E1E", fg="lime", insertbackground="white")
entry_field.grid(row=0, column=0, columnspan=4, padx=12, pady=10)

# History label
history_label = Label(app, text="", bg="#121212", fg="#AAAAAA", anchor="e",
                      font=("Consolas", 11))
history_label.grid(row=1, column=0, columnspan=4, sticky="we")

# Button style
def neon_button(master, text, command, bg="#222", fg="#00FFEF", col_span=1):
    return Button(
        master, text=text, command=command, width=6 * col_span, height=2,
        font=("Consolas", 14, "bold"), bg=bg, fg=fg, activebackground="#00FFD1",
        activeforeground="black", border=0, highlightthickness=1,
        highlightcolor="#00FFD1"
    )

# Buttons configuration
buttons = [
    ('7', lambda: click(7)), ('8', lambda: click(8)), ('9', lambda: click(9)), ('←', backspace),
    ('4', lambda: click(4)), ('5', lambda: click(5)), ('6', lambda: click(6)), ('+', add),
    ('1', lambda: click(1)), ('2', lambda: click(2)), ('3', lambda: click(3)), ('-', subtract),
    ('0', lambda: click(0)), ('.', dot), ('=', equal), ('×', multiply),
    ('C', clear), ('÷', divide)
]

# Button layout
row = 2
col = 0
for text, cmd in buttons:
    if text == 'C':
        neon_button(app, text, cmd, bg="#FF4C4C", fg="white", col_span=4).grid(
            row=row, column=col, columnspan=4, pady=5, padx=5, sticky="we"
        )
        row += 1
        col = 0
        continue

    neon_button(app, text, cmd).grid(row=row, column=col, pady=5, padx=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Bind keyboard
app.bind("<Key>", keypress)

# Run GUI
app.mainloop()
