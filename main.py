import tkinter as tk
from tkinter import *


#head

root = Tk()
root.title('calculator')
root.geometry('500x805')
root.iconbitmap('calculatorico.ico')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)
root.configure(bg='black')

#counting function

def calculate(operation):
    global formula

    if operation == 'C':
        formula = ''
    elif operation =='del':
        formula = formula[0:-1]
    elif operation == '=':
        formula = str(eval(formula))
    elif operation == '√':
        formula =str((eval(formula)) ** .5)
    elif operation == '∛':
        formula =str((eval(formula)) ** .333333333334)
    elif operation == '∜':
        formula =str((eval(formula)) ** .25)
    elif operation == '5√':
        formula =str((eval(formula)) ** .2)         
    elif operation == '%':
        formula =str((eval(formula)) /100) 
   
    else:
        if formula == '0':
            formula = ''
        formula += operation
    Label_text.configure(text=formula)



#display window

formula = '0'
Label_text=tk.Label(text=formula,font=('Roboto',30,'bold'), bg='black', fg='white')
Label_text.place(x = 11, y = 50)





#buttons

buttons = [ 'C','del','%' ,'=', '7', '8', '9', '-', '4', '5', '6' , '+' , '1', '2', '3', '/' , '0' , '-','.', '*' , '^2','^3' ,  '^4', '^5', '√', '∛', '∜', '5√', '3.14','(',')']


x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    Button(text=button,bg='green',fg='white',font=('Roboto', 20), command = get_lbl).place(x = x, y = y, width = 115, height = 79)
    x += 117

    if x>400:
        x = 18
        y += 81





root.mainloop()