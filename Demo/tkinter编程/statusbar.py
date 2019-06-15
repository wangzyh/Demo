from tkinter import *

root = Tk()
# bd边界 relief浮雕效果 anchor对其效果
label = Label(root, text='new one', bd=1, relief=SUNKEN, anchor=W)
# side=BOTTOM下面 fill=X X轴填充
label.pack(side=BOTTOM, fill=X)
root.mainloop()
