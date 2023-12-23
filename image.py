from tkinter import *
from PIL import ImageTk , Image
root = Tk()
root.configure(background = "black")

# funtions for buttons
def next(index):
    global nextbtn
    global prevbtn
    label.grid_forget()
    showImage(index)
    if index == 7:
        nextbtn = Button(root, text= "<", state = "disabled")
    else:
        nextbtn = Button(root, text = ">", command= lambda: next(index+1))

    prevbtn = Button(root, text = "<", command= lambda: prev(index-1))

    prevbtn.grid(row=0,column=0)
    nextbtn.grid(row=0,column=2)
        


def prev(index):
    label.grid_forget()
    showImage(index)

    if (index == 0):
        prevbtn = Button(root, text = ">", state = "disabled")
    else:
        prevbtn = Button(root, text ="<", command= lambda: prev(index-1))

    nextbtn = Button(root, text =">", command= lambda: prev(index+1))
    prevbtn.grid(row=0,column=0)
    nextbtn.grid(row=0,column=2)

        

i1 = Image.open("C:/Users/Dell/OneDrive/Pictures/next.jpeg")
i2 = Image.open("C:/Users/Dell/OneDrive/Pictures/1.jpg")
i3 = Image.open("C:/Users/Dell/OneDrive/Pictures/2.png")
i4 = Image.open("C:/Users/Dell/OneDrive/Pictures/3.png")
i5 = Image.open("C:/Users/Dell/OneDrive/Pictures/4.png")
i6 = Image.open("C:/Users/Dell/OneDrive/Pictures/5.png")
i7 = Image.open("C:/Users/Dell/OneDrive/Pictures/6.jpg")
i8 = Image.open("C:/Users/Dell/OneDrive/Pictures/7.jpg")

images = [i1, i2, i3, i4, i5, i6, i7, i8]

def showImage(index):
    global label
    test = ImageTk.PhotoImage(images[index])
    label = Label(root,image= test)
    label.image = test
    label.grid(row=0, column =1)
    

showImage(0)

#button
prevbtn = Button(root, text = "<", padx=20, pady=10, state= "disabled")
nextbtn = Button(root, text = ">", padx=20, pady=10, command = lambda: next(1))

prevbtn.grid(row=0,column=0)
nextbtn.grid(row=0,column=2)


root.mainloop()
