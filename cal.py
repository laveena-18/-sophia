import tkinter as tk
from tkinter import ttk ,font
root = tk.Tk()


root.title("Calcultor")
e = ttk.Entry(root)
e.grid(sticky='we',columnspan=4)


def click(num):
    newInsert = e.get() +str(num)
    e.delete(0, tk.END)
    e.insert(0, newInsert)

def clear():
    e.delete(0, tk.END)

def handleOperation(opr):
    global Firstnum
    global operation

    Firstnum = e.get()
    e.delete(0,tk.END)
    operation = opr

def handleCalculation():
    currnum = e.get()
    e.delete(0,tk.END)
    if(operation == "+"):
        e.insert(0,int(float(Firstnum))+ int(float(currnum)))
    elif(operation == "-"):
        e.insert(0,int(float(Firstnum)) - int(float(currnum)))
    elif(operation == "*"):
        e.insert(0,int(float(Firstnum)) * int(float(currnum)))
    elif(operation == "/"):
        e.insert(0,int(float(Firstnum))/ int(float(currnum)))

# styleing
style = ttk.Style(root)
style.configure('TButton', forground='orange', background='purple',font= ("times new roman",16))
#style = ttk.Style()
#style.map("TButton",
 #   foreground=[('pressed', 'white'), ('active', 'blue')],
  #  background=[('pressed', 'black'), ('active', 'white')]
   # )


# numbers
b1 = ttk.Button(root, text="1",width=8,style = 'TButton',command = lambda: click(1))
b1.grid(row=3, column=0)

b2 = ttk.Button(root, text="2",width=8, style= 'TButton', command = lambda: click(2))
b2.grid(row=3, column=1)

b3 = ttk.Button(root, text="3",width=8, style='TButton', command = lambda: click(3))
b3.grid(row=3, column=2)

b4 = ttk.Button(root, text="4", width=8, style='TButton', command= lambda: click(4))
b4.grid(row=2, column=0)

b5 = ttk.Button(root, text="5", width=8, style='TButton', command = lambda: click(5))
b5.grid(row=2, column=1)

b6 = ttk.Button(root, text="6", width=8, style='TButton', command= lambda: click(6))
b6.grid(row=2, column=2)

b7 = ttk.Button(root, text="7", width=8, style='TButton', command= lambda: click(7))
b7.grid(row=1, column=0)

b8 = ttk.Button(root, text="8", width=8, style='TButton', command= lambda: click(8))
b8.grid(row=1, column=1)

b9 = ttk.Button(root, text="9", width=8, style='TButton', command= lambda: click(9))
b9.grid(row=1, column=2)

b0 = ttk.Button(root, text="0", width=8, style='TButton', command= lambda: click(0))
b0.grid(row=4, column=0)

# operations

bclr = ttk.Button(root, text="C", width=8, command= clear)
bclr.grid(row=1, column=3)

ba = ttk.Button(root, text="+", width=8, command = lambda: handleOperation("+"))
ba.grid(row=2, column=3)

bs = ttk.Button(root, text="-", width=8, command = lambda: handleOperation("-"))
bs.grid(row=3, column=3)

bm = ttk.Button(root, text="*", width=8, command = lambda: handleOperation("*"))
bm.grid(row=4, column=1)

bd = ttk.Button(root, text="/", width=8, command = lambda: handleOperation("/"))
bd.grid(row=4, column=2)

beq = ttk.Button(root, text="=", width=8, command= handleCalculation)
beq.grid(row=4, column=3)

root.mainloop()







