from tkinter import *

def callback():
    print("callback the menu")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=callback) # 命令
filemenu.add_command(label='Open', command=callback)
filemenu.add_separator() # 分割线
filemenu.add_command(label='Exit', command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu) # 子菜单
helpmenu.add_command(label='About..', command=callback())

root.mainloop()
