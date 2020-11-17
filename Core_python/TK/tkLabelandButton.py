from tkinter import *

# 顶层窗口(根窗口)
top = Tk()

hello = Label(top, text='Hello World!')
hello.pack()

Q = Button(top, text='QUIT', command=quit,
              bg='red', fg='white')
Q.pack(fill=X, expand=1)

# 运行
top.mainloop()
