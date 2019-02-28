from tkinter import *
 
def Calci(source, side):
    Obj = Frame(source, borderwidth=8, bd=2, bg="black")
    Obj.pack(side=side, expand =YES, fill=BOTH)
    return Obj
 
def button(source, side, text, command=None):
    Obj = Button(source, text=text, command=command)
    Obj.pack(side=side, expand = YES, fill=BOTH)
    return Obj
 
class calciapp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 12 italic')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Mine Calculator')
 
        display = StringVar()
        Entry(self, relief=FLAT, textvariable=display,justify='right'
          , bd=15, bg="White").pack(side=TOP,expand=YES, fill=BOTH)
 
        for clearButton in (["C"]):
            erase = Calci(self, TOP)
            for i in clearButton:
                button(erase, LEFT, i, lambda
                       Obj=display, q=i: Obj.set(''))
 
        for numButton in ("987*", "654/", "321-", ".0+"):
         FunctionNum = Calci(self, TOP)
         for i in numButton:
            button(FunctionNum, LEFT, i, lambda
                   Obj=display, q=i: Obj.set(Obj.get() + q))
 
        EqualButton = Calci(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btn_iEquals = button(EqualButton, LEFT, iEquals)
                btn_iEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                Obj=display: s.calc(Obj), '+')
 
 
            else:
                btn_iEquals = button(EqualButton, LEFT, iEquals,
                                    lambda Obj=display, s=' %s ' % iEquals:Obj.set (Obj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 calciapp().mainloop()
