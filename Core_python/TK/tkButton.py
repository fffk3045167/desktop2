from tkinter import *

# 顶层窗口(根窗口)
top = Tk()

quit = Button(top, text='Hello World!', command=quit)
quit.pack()

# 运行
top.mainloop()
