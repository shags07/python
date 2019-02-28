import tkinter
root = tkinter.Tk()

def ShowText():
   tkinter.messagebox.showinfo( "Show Text", "Welcome to capgemini")

showtext = tkinter.Button(root, text ="Show Text", command = ShowText)
def ShowImage():
    tkinter.PhotoImage( "Show image",file="C:\downloads\capgeminilogo1.png")
showimage = tkinter.Button(root, text="Show image", command = ShowImage)
exitbutton = tkinter.Button(root, text='Exit', command=root.destroy)

showtext.pack()
showimage.pack()
exitbutton.pack()
root.mainloop()

