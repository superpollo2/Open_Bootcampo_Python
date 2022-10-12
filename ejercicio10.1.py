from ast import Str
from tkinter import *


    
    
root = Tk()
var = BooleanVar(root)
radioB1 = Radiobutton(root, text ="opcion 1", variable= var, value=1)
radioB1.pack(anchor = W)

radioB2 = Radiobutton(root, text ="opcion 2", variable= var, value=2)
radioB2.pack(anchor = W)

label = Label(root)
message =   f"has seleccionado la opcion {var.get()} "
print (var.get())
label.config(text= message)

label.pack()
root.mainloop()