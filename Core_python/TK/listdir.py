import os
from time import sleep
from tkinter import *


class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()


        # 模块1，显示版本信息
        self.label = Label(self.top, text='Directory Lister v1.0')
        self.label.pack()

        # 模块2，显示当前路径
        # 使用StringVar 用于跟踪变量的值的变化，以保证值的变更可以随时显示在界面上
        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()


        # 模块3，显示目录内容
        self.dirfm = Frame(self.top)

        self.dirsb = Scrollbar(self.dirfm)  # Scrollbar 滚动条
        # RIGHT: 将滚动条放在右边，Y: 竖直方向填充
        self.dirsb.pack(side=RIGHT, fill=Y)

        # 指定Listbox的yscrollcommand的回调函数为Scrollbar.set()
        self.dirs = Listbox(self.dirfm, height=15, width=50,
                            yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        # 指定Scrollbar的command的回调函数为Listbox.yview()
        self.dirsb.config(command=self.dirs.yview)
        # LEFT: 指定Listbox的内容靠左, BOTH: 水平和竖直方向填充
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50,
                          textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()



        # 模块4，按钮
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                          activeforeground='white', activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS,
                         activeforeground='white', activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
                         activeforeground='white', activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)

        self.bfm.pack()


        if initdir:
            # cwd.set() 设置模块2显示的路径
            # os.curdir 获取当前执行Python文件的文件夹
            self.cwd.set(os.curdir)

            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())

        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cwd.set('FETCHING DIGECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)

        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)

        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()