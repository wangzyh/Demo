from tkinter import *

button = Button(text="wangButton", padx=10, pady=10)
button.config(cursor='gumby')
button.config(bd=8, relief=RAISED)
button.config(bg='green', fg='yellow')
button.config(font=("Helvetica", 10, 'bold italic'))

button.pack()
button.mainloop()
