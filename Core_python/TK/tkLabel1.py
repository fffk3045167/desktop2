from tkinter import *

top = Tk()

label = Label(top, text='Hello World!')
# 使用Packer来管理和显示控件
label.pack()

# 运行
top.mainloop()
