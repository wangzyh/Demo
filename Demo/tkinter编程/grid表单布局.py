
from tkinter import *

root = Tk()
Label(root, text='First').grid(row=0)
Label(root, text='Second').grid(row=1)
en1 = Entry(root)
en2 = Entry(root)

en1.grid(row=0, column=1)
en2.grid(row=1, column=1)

Button(root, text='OK').grid(row=2)

root.mainloop()
