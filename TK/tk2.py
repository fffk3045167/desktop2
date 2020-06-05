from tkinter import *

root = Tk()
root.title('title')
lb = Label(root, text='event',
           bg='#d3fbfb',
           fg='red',
           font=('华文新魏', 32),
           width=20,
           height=2,
           relief=RAISED)
lb.pack()
root.mainloop()
