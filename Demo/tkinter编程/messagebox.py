from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()

def callback():
    # 消息窗体提醒
    if messagebox.askyesno('Wang', 'Hi sjaf'):
        print("Yes")
    else:
        print("No")

button = Button(root, text='Button1', command=callback)
button.pack()

root.mainloop()
