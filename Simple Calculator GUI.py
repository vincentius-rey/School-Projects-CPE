from tkinter import *
from typing import Match

root = Tk()
root.title("Simple Calculator")
root.config(bg='purple')

textBox = Entry(root, font=('ds-digital', 36, 'bold'), borderwidth=10, width=8)
textBox.pack()
textBox.insert(0, '0')
textBox.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

def buttonClick(num):
    if textBox.get() == '0':
        textBox.delete(0, END)
    elif textBox.get() == '+':
        textBox.delete(0, END)
    elif textBox.get() == '-':
        textBox.delete(0, END)
    elif textBox.get() == '×':
        textBox.delete(0, END)
    elif textBox.get() == '÷':
        textBox.delete(0, END)
    c = textBox.get()
    textBox.delete(0, END)
    textBox.insert(0, str(c) + str(num))
    return

def buttonAdd():
    num = textBox.get()
    global number
    global math 
    math = "Addition"
    number = float(num)
    textBox.delete(0, END)
    textBox.insert(0, '+')

def buttonSub():
    num = textBox.get()
    global number
    global math 
    math = "Subtraction"
    number = float(num)
    textBox.delete(0, END)
    textBox.insert(0, '-')

def buttonMul():
    num = textBox.get()
    global number
    global math 
    math = "Multiplication"
    number = float(num)
    textBox.delete(0, END)
    textBox.insert(0, '×')

def buttonDiv():
    num = textBox.get()
    global number
    global math 
    math = "Division"
    number = float(num)
    textBox.delete(0, END)
    textBox.insert(0, '÷')

def buttonClear():
    textBox.delete(0, END)
    textBox.insert(0, '0')
    return
    
def buttonDelete():
        num = int(textBox.get())
        dnum = num // 10
        textBox.delete(0, END)
        textBox.insert(0, dnum)

def buttonEqual():
    sNum = textBox.get()
    textBox.delete(0, END)
    if math == "Addition":
        textBox.insert(0, number + float(sNum))
    if math == "Subtraction":
        textBox.insert(0, number - float(sNum))
    if math == "Multiplication":
        textBox.insert(0, number * float(sNum))
    if math == "Division":
        textBox.insert(0, number / float(sNum))
        
head = Label(root, text="CALC-U", font=('phosphate', 20, 'bold'), bg='black', fg='white', bd=10).grid(row=0, column=1, columnspan=2)
label = Button(root, text="DEMO", font=('ds-digital', 25, 'bold'), bg='red', fg='white', padx=35, pady=35, bd=5, command=DISABLED).grid(row=2, column=0, columnspan=2)

num1 = Button(root, text="1", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(1)).grid(row=5, column=0)
num2 = Button(root, text="2", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(2)).grid(row=5, column=1)
num3 = Button(root, text="3", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(3)).grid(row=5, column=2)
num4 = Button(root, text="4", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(4)).grid(row=4, column=0)
num5 = Button(root, text="5", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(5)).grid(row=4, column=1)
num6 = Button(root, text="6", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(6)).grid(row=4, column=2)
num7 = Button(root, text="7", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(7)).grid(row=3, column=0)
num8 = Button(root, text="8", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(8)).grid(row=3, column=1)
num9 = Button(root, text="9", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(9)).grid(row=3, column=2)
num0 = Button(root, text="0", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonClick(0)).grid(row=6, column=0)
decimal = Button(root, text=".", font=('phosphate', 30, 'bold'), padx=67, pady=30, bd=5, command=lambda: buttonClick('.')).grid(row=6, column=1)

deleteButton = Button(root, text="→", font=('phosphate', 20, 'bold'), padx=46, pady=50, bd=5, command=buttonDelete).grid(row=2, column=2)
clearButton = Button(root, text="C", font=('phosphate', 30, 'bold'), padx=45, pady=26, bd=5, command=buttonClear).grid(row=2, column=3)
divideButton = Button(root, text="÷", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonDiv()).grid(row=3, column=3)
timesButton = Button(root, text="×", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonMul()).grid(row=4, column=3)
minusButton = Button(root, text="-", font=('phosphate', 30, 'bold'), padx=60, pady=30, bd=5, command=lambda: buttonSub()).grid(row=5, column=3)
plusButton = Button(root, text="+", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, command=lambda: buttonAdd()).grid(row=6, column=2)
equalButton = Button(root, text="=", font=('phosphate', 30, 'bold'), padx=50, pady=30, bd=5, bg="gold", command=lambda: buttonEqual()).grid(row=6, column=3)

root.mainloop()