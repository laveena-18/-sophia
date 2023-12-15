from tkinter import *
root = Tk()

#forming a label
Label(root, text = "Hello World!!", padx =50, pady =10).pack()

def enterlabel():
    Label(root, text = "button clicked").pack()

Button(root,text= "Click me",padx=50, pady=10, command = enterlabel).pack()

root.mainloop()