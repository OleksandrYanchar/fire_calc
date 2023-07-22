import tkinter as tk
import math
# Counting function

def calculate(operation):
    global formula

    if operation == "C":
        formula = ""
    elif operation == "del":
        formula = formula[0:-1]
    elif operation == "=":
        formula = str(eval(formula))
    elif operation == "√":
        formula = str((eval(formula)) ** 0.5)
    elif operation == "∛":
        formula = str((eval(formula)) ** 0.333333333334)
    elif operation == "∜":
        formula = str((eval(formula)) ** 0.25)
    elif operation == "5√":
        formula = str((eval(formula)) ** 0.2)
    elif operation == "%":
        formula = str((eval(formula)) / 100)
    elif operation == "^2":
        formula = str((eval(formula)) ** 2)
    elif operation == "^3":
        formula = str((eval(formula)) ** 3)
    elif operation == "^4":
        formula = str((eval(formula)) ** 4)
    elif operation == "^5":
        formula = str((eval(formula)) ** 5)
    elif operation == "π":
        formula = str(eval("math.pi"))
    elif operation == "e":
        formula = str(eval("math.e"))
    else:
        if formula == "0":
            formula = ""
        formula += operation
    label_text.configure(text=formula)


# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("500x805")
    root.iconbitmap("calculatorico.ico")
    root.resizable(False, False)
    root.wm_attributes("-topmost", 1)
    root.configure(bg="black")
    return root


def create_display(root):
    global formula
    formula = "0"
    label_text = tk.Label(
        root, text=formula, font=("Roboto", 30, "bold"), bg="black", fg="white"
    )
    label_text.place(x=11, y=50)
    return label_text


def create_button(root, text, x, y):
    def get_label():
        calculate(text)

    tk.Button(
        root, text=text, bg="green", fg="white", font=("Roboto", 20), command=get_label
    ).place(x=x, y=y, width=115, height=79)


# Buttons
buttons = [
    "C",
    "del",
    "%",
    "=",
    "7",
    "8",
    "9",
    "-",
    "4",
    "5",
    "6",
    "+",
    "1",
    "2",
    "3",
    "/",
    "0",
    "-",
    ".",
    "*",
    "^2",
    "^3",
    "^4",
    "^5",
    "√",
    "∛",
    "∜",
    "5√",
    "π",
    "(",
    ")",
    "e",
]


def create_buttons(root):
    x, y = 18, 140
    for button in buttons:
        create_button(root, button, x, y)
        x += 117

        # Creating a new line of buttons if the previous one is full
        if x > 400:
            x = 18
            y += 81


if __name__ == "__main__":
    root = create_gui()
    label_text = create_display(root)
    create_buttons(root)
    root.mainloop()