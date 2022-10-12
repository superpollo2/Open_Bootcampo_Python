from tkinter import *

root = Tk()

var1 = IntVar()
Checkbutton(root, text="Hombre", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text="Mujer", variable=var2).grid(row=2, sticky=W)



message =   "selecciona una opción"
Label(root, text= message).grid(row=0,sticky=W)


mainloop()


