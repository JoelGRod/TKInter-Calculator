from tkinter import *
from tkinter.ttk import *
from tkmacosx import Button

root = Tk()
root.title('Calculator')
root.configure(background='#333333')
# root.geometry('500x500')

style = Style()
# style.configure("number.TButton", foreground="#fff", background="#666")
# style.configure("op.TButton", foreground="#fff", background="#fe9727")

equation = StringVar()

def entries(value):
    equation.set(equation.get() + str(value))

def calculate():
    try:
        equation.set(eval(equation.get()))
    except:
        equation.set('Invalid Calc')

def clear():
    equation.set('')

entry = Entry(root, textvariable=equation).grid(row=0, columnspan=4, sticky='nswe')

btn7 = Button(root, text = " 7 ", fg="#fff", bg="#666", command=lambda: entries(7)).grid(row=1, column=0, sticky='nswe')
btn8 = Button(root, text = " 8 ", fg="#fff", bg="#666", command=lambda: entries(8)).grid(row=1, column=1, sticky='nswe')
btn9 = Button(root, text = " 9 ", fg="#fff", bg="#666", command=lambda: entries(9)).grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text = " 4 ", fg="#fff", bg="#666", command=lambda: entries(4)).grid(row=2, column=0, sticky='nswe')
btn5 = Button(root, text = " 5 ", fg="#fff", bg="#666", command=lambda: entries(5)).grid(row=2, column=1, sticky='nswe')
btn6 = Button(root, text = " 6 ", fg="#fff", bg="#666", command=lambda: entries(6)).grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text = " 1 ", fg="#fff", bg="#666", command=lambda: entries(1)).grid(row=3, column=0, sticky='nswe')
btn2 = Button(root, text = " 2 ", fg="#fff", bg="#666", command=lambda: entries(2)).grid(row=3, column=1, sticky='nswe')
btn3 = Button(root, text = " 3 ", fg="#fff", bg="#666", command=lambda: entries(3)).grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text = " 0 ", fg="#fff", bg="#666", command=lambda: entries(0)).grid(row=4, column=0, sticky='nswe', columnspan=2)
decimal = Button(root, text = " . ", fg="#fff", bg="#666", command=lambda: entries('.')).grid(row=4, column=2, sticky='nswe')

plus = Button(root, text = " + ", fg="#fff", bg="#fe9727", command=lambda: entries('+')).grid(row=1, column=3, sticky='nswe')
minus = Button(root, text = " - ", fg="#fff", bg="#fe9727", command=lambda: entries('-')).grid(row=2, column=3, sticky='nswe')
multiply = Button(root, text = " * ", fg="#fff", bg="#fe9727", command=lambda: entries('*')).grid(row=3, column=3, sticky='nswe')
divide = Button(root, text = " / ", fg="#fff", bg="#fe9727", command=lambda: entries('/')).grid(row=4, column=3, sticky='nswe')

clear = Button(root, text = " Clear ", fg="#fff", bg="#666", command=clear).grid(row=5, column=2, sticky='nswe')
equal = Button(root, text = " = ", fg="#fff", bg="#fe9727", command=calculate).grid(row=5, column=3, sticky='nswe')

root.mainloop()
