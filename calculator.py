from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Calculator')
root.configure(background='#ffffff')
root.geometry('500x500')

style = Style()
style.configure("number.TButton", foreground="#fff", background="#666")
style.configure("op.TButton", foreground="#fff", background="#fe9727")

equation = StringVar()

entry = Entry(root, textvariable=equation).grid(row=0, columnspan=4, sticky='nswe')

btn7 = Button(root, text = " 7 ", style="number.TButton").grid(row=1, column=0, sticky='nswe')
btn8 = Button(root, text = " 8 ", style="number.TButton").grid(row=1, column=1, sticky='nswe')
btn9 = Button(root, text = " 9 ", style="number.TButton").grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text = " 4 ", style="number.TButton").grid(row=2, column=0, sticky='nswe')
btn5 = Button(root, text = " 5 ", style="number.TButton").grid(row=2, column=1, sticky='nswe')
btn6 = Button(root, text = " 6 ", style="number.TButton").grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text = " 1 ", style="number.TButton").grid(row=3, column=0, sticky='nswe')
btn2 = Button(root, text = " 2 ", style="number.TButton").grid(row=3, column=1, sticky='nswe')
btn3 = Button(root, text = " 3 ", style="number.TButton").grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text = " 0 ", style="number.TButton").grid(row=4, column=0, sticky='nswe', columnspan=2)
decimal = Button(root, text = " . ", style="number.TButton").grid(row=4, column=2, sticky='nswe')

plus = Button(root, text = " + ", style="op.TButton").grid(row=1, column=3, sticky='nswe')
minus = Button(root, text = " - ", style="op.TButton").grid(row=2, column=3, sticky='nswe')
multiply = Button(root, text = " * ", style="op.TButton").grid(row=3, column=3, sticky='nswe')
divide = Button(root, text = " / ", style="op.TButton").grid(row=4, column=3, sticky='nswe')

root.mainloop()
