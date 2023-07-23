import tkinter as tk
import math
from calculator import calculate
from consts import buttons


# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("850x805")
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
        global formula
        formula = calculate(text, formula)
        label_text.configure(text=formula)

    tk.Button(
        root, text=text, bg="green", fg="white", font=("Roboto", 20), command=get_label
    ).place(x=x, y=y, width=115, height=79)


def create_buttons(root):
    x, y = 18, 140
    for button in buttons:
        create_button(root, button, x, y)
        x += 117

        # Creating a new line of buttons if the previous one is full
        if x > 800:
            x = 18
            y += 81


if __name__ == "__main__":
    root = create_gui()
    label_text = create_display(root)
    create_buttons(root)
    root.mainloop()
