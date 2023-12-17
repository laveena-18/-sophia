from tkinter import *
root = Tk()

root.title("Calcultor")
e = Entry(root)
e.grid(sticky='we',columnspan=4)


def click(num):
    newInsert = e.get() +str(num)
    e.delete(0, END)
    e.insert(0, newInsert)

def clear():
    e.delete(0, END)

def handleOperation(opr):
    global Firstnum
    global operation

    Firstnum = e.get()
    e.delete(0,END)
    operation = opr

def handleCalculation():
    currnum = e.get()
    e.delete(0,END)
    if(operation == "+"):
        e.insert(0,int(float(Firstnum))+ int(float(currnum)))
    elif(operation == "-"):
        e.insert(0,int(float(Firstnum)) - int(float(currnum)))
    elif(operation == "*"):
        e.insert(0,int(float(Firstnum)) * int(float(currnum)))
    elif(operation == "/"):
        e.insert(0,int(float(Firstnum))/ int(float(currnum)))




# numbers
b1 = Button(root, text="1",width=8, pady=10,command = lambda: click(1))
b1.grid(row=3, column=0)

b2 = Button(root, text="2",width=8, pady=10, command = lambda: click(2))
b2.grid(row=3, column=1)

b3 = Button(root, text="3",width=8, pady=10, command = lambda: click(3))
b3.grid(row=3, column=2)

b4 = Button(root, text="4", width=8, pady=10, command= lambda: click(4))
b4.grid(row=2, column=0)

b5 = Button(root, text="5", width=8, pady=10, command = lambda: click(5))
b5.grid(row=2, column=1)

b6 = Button(root, text="6", width=8, pady=10, command= lambda: click(6))
b6.grid(row=2, column=2)

b7 = Button(root, text="7", width=8, pady=10, command= lambda: click(7))
b7.grid(row=1, column=0)

b8 = Button(root, text="8", width=8, pady=10, command= lambda: click(8))
b8.grid(row=1, column=1)

b9 = Button(root, text="9", width=8, pady=10, command= lambda: click(9))
b9.grid(row=1, column=2)

b0 = Button(root, text="0", width=8, pady=10, command= lambda: click(0))
b0.grid(row=4, column=0)

# operations

bclr = Button(root, text="C", width=8, pady=10, command= clear)
bclr.grid(row=1, column=3)

ba = Button(root, text="+", width=8, pady=10,command = lambda: handleOperation("+"))
ba.grid(row=2, column=3)

bs = Button(root, text="-", width=8, pady=10, command = lambda: handleOperation("-"))
bs.grid(row=3, column=3)

bm = Button(root, text="*", width=8, pady=10, command = lambda: handleOperation("*"))
bm.grid(row=4, column=1)

bd = Button(root, text="/", width=8, pady=10,command = lambda: handleOperation("/"))
bd.grid(row=4, column=2)

beq = Button(root, text="=", width=8, pady=10 , command= handleCalculation)
beq.grid(row=4, column=3)

root.mainloop()







