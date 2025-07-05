from tkinter import *
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
window = Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)
expression = ""
equation = StringVar()
entry = Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14,
              borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]
for (text, row, col) in buttons:
    if text == '=':
        Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        Button(window, text=text, padx=90, pady=20, font=('Arial', 14), command=clear).grid(row=row, column=col, columnspan=4)
    else:
        Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: press(t)).grid(row=row, column=col)

window.mainloop()