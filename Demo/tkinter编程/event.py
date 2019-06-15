from tkinter import *
from tkinter import messagebox

root = Tk()


def callback(event):
    frame.focus_set()
    # 输出点击的坐标
    print("clicked at:%s,%s" % (event.x, event.y))


def key(event):
    # 输出键盘敲击的按键
    print("pressed", repr(event.char))

# 退出询问模块
def closeWindow():
    if messagebox.askokcancel('Quit', "Do you want to exit"):
        root.destroy()

frame = Frame(root, width=100, height=100)
frame.bind('<Button-1>', callback)# 绑定鼠标左键点击
frame.bind('<Key>', key) # 绑定键盘
frame.pack()

root.protocol('WM_DELETE_WINDOW', closeWindow)

root.mainloop()
