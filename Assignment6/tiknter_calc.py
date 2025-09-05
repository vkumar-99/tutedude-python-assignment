from tkinter import *
# Window
window = Tk()
window.geometry("300x320")
window.title("Tiknter Calculator")
#Entry box
entry_box = Entry(window, width=45, borderwidth=5)
entry_box.place(x=10, y=20)
#Number Buttons
def click(num):
    n1 = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0, str(n1)+str(num))

Button(window, text=1, width=5, command=lambda: click(1)).place(x=10, y=80)
Button(window, text=2, width=5, command=lambda: click(2)).place(x=60, y=80)
Button(window, text=3, width=5, command=lambda: click(3)).place(x=110, y=80)
Button(window, text=4, width=5, command=lambda: click(4)).place(x=10, y=130)
Button(window, text=5, width=5, command=lambda: click(5)).place(x=60, y=130)
Button(window, text=6, width=5, command=lambda: click(6)).place(x=110, y=130)
Button(window, text=7, width=5, command=lambda: click(7)).place(x=10, y=180)
Button(window, text=8, width=5, command=lambda: click(8)).place(x=60, y=180)
Button(window, text=9, width=5, command=lambda: click(9)).place(x=110, y=180)
Button(window, text=0, width=5, command=lambda: click(0)).place(x=60, y=230)
# Operands Button
def add():
    n1 = entry_box.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry_box.delete(0, END)
def subtract():
    n1 = entry_box.get()
    global math
    math = "substraction"
    global i
    i = int(n1)
    entry_box.delete(0, END)
def multiply():
    n1 = entry_box.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    entry_box.delete(0, END)
def div():
    n1 = entry_box.get()
    global math
    math = "divison"
    global i
    i = int(n1)
    entry_box.delete(0, END)
def result():
    n2 = entry_box.get()
    entry_box.delete(0, END)
    if math == "addition":
        entry_box.insert(0, str(i + int(n2)))
    elif math == "substraction":
        entry_box.insert(0, str(i - int(n2)))
    elif math == "multiplication":
        entry_box.insert(0, str(i * int(n2)))
    elif math == "divison":
        entry_box.insert(0, str(i / int(n2)))
def clear():
    entry_box.delete(0, END)

btn_add = Button(window, text="+", width=5, command=add)
btn_add.place(x=180, y=80)
btn_sub = Button(window, text="-", width=5, command=subtract)
btn_sub.place(x=230, y=80)
btn_multiply = Button(window, text="*", width=5, command=multiply)
btn_multiply.place(x=180, y=130)
btn_div = Button(window, text="/", width=5, command=div)
btn_div.place(x=230, y=130)
btn_result = Button(window, text="=", width=5, command=result)
btn_result.place(x=180, y=180)
btn_clear = Button(window, text="Clear", width=5,command=clear)
btn_clear.place(x=230, y=180)
# Main loop
mainloop()