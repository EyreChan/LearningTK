import tkinter as tk
from tkinter import *       #如果没有这一行，往pack()传参会出错

window = tk.Tk()

window.title('LabelButton')

#设置成窗口大小
win_wid = window.winfo_screenwidth()
win_heig = window.winfo_screenheight()
window.geometry('%dx%d'%(win_wid,win_heig))

#自动刷新的字符串变量
var = tk.StringVar()
#Label(根对象, [属性列表])
l = tk.Label(window, textvariable = var, bg = 'green', font = ('Arial', 12),
             width = 50,height = 20)
l.pack(side = RIGHT)

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text = 'hit me', width = 15,
              height = 2, command = hit_me)
b.pack(side = RIGHT)

window.mainloop()