from tkinter import *

root = Tk()

label = Label(root, text='Hello World')
# 鼠标进入区域样式改变
label.config(cursor='gumby')
label.config(width=80, height=10, fg='yellow', bg='dark green')
label.config(font=('times', '28', 'bold'))
label.pack()

root.mainloop()
