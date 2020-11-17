from functools import partial as pto
from tkinter import Tk, Button, X, messagebox


WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55/nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

critCB = lambda : messagebox.showerror('Error', 'Error Button Pressed!')
warnCB = lambda : messagebox.showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda : messagebox.showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')

Button(top, text='QUIT', command=quit, bg='red', fg='white').pack()
# 第一阶偏函数，MyButton回调用Button
MyButton = pto(Button, top)
# 第二阶偏函数，使用第一阶偏函数，并对其进行模版化
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()'
    )
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值
    eval(cmd)

top.mainloop()