__author__ = "Linhai"

import urllib3.connection
from urllib import request
import threading
import time
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
# from tkinter.dialog import *
from tkinter.filedialog import *
import os
from tkinter.font import *
import tkinter.ttk as ttk
from tkinter.ttk import *

from tab_control import *

root = Tk()

root.geometry("1250x900")
# Style().theme_use('vista') # ('aqua', 'clam', 'alt', 'default', 'classic')
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# 最底下一拦 显示整体状态
frame_buttom = Frame(root)
frame_buttom.grid(row=1, column=0, sticky="e")

frame_base = Frame(root)
frame_base.grid(row=0)

frame0 = Frame(frame_base)
frame0.grid(row=0, column=0, sticky='news')



listbox01 = Listbox(frame0)
listbox01.grid(row=0, column=0, padx=10, pady=10)
for x in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            listbox01.insert(END, x)

for x in range(20):
    b = Button(frame0, text="--{}--".format(x))
    b.grid(row=x + 1, column=0 )

# 中间一大片
frame1 = Frame(frame_base)
frame1.grid(row=0, column=1, )

# 右边一大列
frame2 = Frame(frame_base, )
frame2.grid(row=0, column=2)

listbox02= Listbox(frame2)
listbox02.configure(height=10)
listbox02.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
listbox02.configure(width=10)
for x in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            listbox02.insert(END, x)

# buttom

statusbar = tk.Label(frame_buttom, bd=0, text="LN20: --", relief=RIDGE, anchor='se')
statusbar.grid(row=0, column=0, sticky="s")
statusbar1 = tk.Label(frame_buttom, bd=0, text="Time: --", relief=RIDGE, anchor='se', padx=10)
statusbar1.grid(row=0, column=1, sticky="s")
# statusbar.configure(width=110)
# statusbar.place(relx=0, relwidth=1)
# statusbar.pack(fill=X, side=BOTTOM, expand=1)

# statusbar = tk.Label(frame_buttom, text="LN20ghjklkdjhgd", bd=1, relief=RIDGE, anchor='se', width=100)
# # statusbar.pack(side=BOTTOM, fill=X)
# statusbar.place(relx=0, rely=0, relwidth=1, relheight=1)
# # statusbar.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

# 最上面
frame10 = Frame(frame1, )
frame10.grid(row=0, column=0, )



# url
frame11 = Frame(frame1, )
frame11.grid(row=1, column=0, sticky='newe')



# 请求参数选项卡
frame12 = Frame(frame1)
frame12.grid(row=2, column=0,  columnspan=2,  pady=50, padx=80, )
# frame.grid_columnconfigure(1, weight=1)
# frame.grid_rowconfigure(1, weight=1)
# 进度条 先不用
frame13 = Frame(frame1, )
frame13.grid(row=3, column=0,  columnspan=2)
# response标题
frame14 = Frame(frame1, )
frame14.grid(row=4, column=0,  sticky='W', )
# frame14.configure(foreground="#748734")
# response状态
frame15 = Frame(frame1)
frame15.grid(row=5, column=0,  sticky="w")

response_frame = Frame(frame11)
response_frame.grid(row=6, column=0, sticky="news")


var1 = StringVar()
var1.set("HHHH")

# cv = Canvas(root, background='white')
# cv.grid(row=0, column=0, rowspan=700, columnspan=1)
# tang = cv.create_rectangle(0, 0, 10, 100, fill='red')

font_type = "Consolas"
font_fav = Font(frame11, font=((font_type, 16, NORMAL)))

entry = Entry(frame11, textvariable=var1, text="Open", show=None,
              background='#DDDED4',
              width=50, font=font_fav,
              foreground="#874387")
#                highlightcolor='red', selectbackground='red')#exportselection
# 设置字体后自动改变窗体大小哈
# fg selectborderwidth selectforeground
# 文字颜色。值为颜色或为颜色代码，如：'red','#ff0000'
#默认情况下，你如果在输入框中选中文本，默认会复制到粘贴板，如果要忽略这个功能刻工艺设置 exportselection=0。
entry.grid(row=0, column=1, sticky='nwse', padx=10, pady=15)
# scroll01 = Scrollbar(root, orient=HORIZONTAL)
# entry.config(xscrollcommand=scroll01.set, state='normal')
# scroll01.config(command=entry.xview)
# scroll01.grid(row=1, sticky='ne', padx=10, pady=10)

entry.insert(0, var1.get())
entry.focus()

# 先用frame划分 很牛皮！！！

# Entry(root).grid(row=10, column=5)
# Label(root, text="First", width=50, height=20).grid(row=1, column=10, )
# Label(root, text="Second").grid(row=2, column=10, sticky=E, columnspan=10)


var2 = StringVar()
request_com = ttk.Combobox(frame11, textvariable=var2, width=8,state='readonly',
                           font=Font(root, font=((font_type, 13, ROMAN))))
request_com['value'] = ["67890", "POST"]
# request_com.set("GET") == 下一句
# var2.set("GET") # == 下一句
request_com.current(0)

request_com.grid(row=0, column=0, sticky='news', padx=10, pady=15)

x0, y0, x1, y1= 0, 0, 40, 40
cv = Canvas(frame11, height=40, width=40)
cv.grid(row=0, column=2)
cv.create_arc(x0+10, y0+10, x1+10, y1+10, start=0, extent=180)  #创建一个扇形
line = cv.create_line(x0, y0, x1, y1)

def r(a, b, c):
    for _ in range(20):
        for x in range(100):
            print("-", a, end="|\n")
            entry.delete(0, END)
            entry.insert(0, a[0] + str(x))
            var3.set(100-x)
            time.sleep(0.003)

def r1(a, b, c):
    for _ in range(20):
        for x in range(100):
            print("*", end="!\n")
            res_process_var.set(x)
            time.sleep(0.03)



def send_request():
    tmp = var1.get()
    t1 = threading.Thread(target=r, args=(tmp, 2, 3))
    t2 = threading.Thread(target=r1, args=(1, 2, 3))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()

class ___(object):

    def __init__(self, process_bar, method, url, headers, data, json):
        self.process_bar = process_bar
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.json = json
        self.request_status = "sending"


    def send_request(self):
        if self.request_status is "sending":
            self.t1 = threading.Thread(target=r, args=(self.process_bar))
            self.t2 = threading.Thread(target=r1, args=(self.method, self.url, self.headers, self.data, self.json))
            self.t1.setDaemon(True)
            self.t2.setDaemon(True)
            self.t1.start()
            self.t2.start()
            self.request_status = "cancal"
        else:
            self.t1._stop()
            self.t2._stop()


import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


class TestThread(threading.Thread):
    def run(self):
        print
        "begin"
        while True:
            time.sleep(0.1)
        print
        "end"


if __name__ == "__main__":
    t = TestThread()
    t.start()
    time.sleep(1)
    stop_thread(t)
    print
    "stoped"



send_but = Button(cv,  text="Send", command=send_request)
send_but.grid(row=0, column=1)

def moveit(rect): # 参数，目标组件
    cv.move(rect, 0, 2)


# sp01 = Spinbox(frame1)
# sp01.grid(row=0, column=2)


var3 = StringVar()
pro_bar = Progressbar(frame13, variable=var3)
pro_bar.grid(row=0, column=0, sticky='news', padx=10, pady=10)
for x in range(50):
    var3.set(x)


# style.configure('lefttab.TNotebook', tabposition='ns')
# style.configure('TNotebook.tabposition', 'w')
# style.configure('TNotebook.Tab', font=('URW Gothic L','11','bold') )
base_tab = Notebook(frame12, )

print(ttk.Style(base_tab).layout("TNotebook"))


base_tab.grid(row=0, column=0, padx=10, pady=10, ipady=6)
tabs = TabControl(base_tab)

# notebook.grid_columnconfigure(1, weight=1)
# notebook.grid_rowconfigure(1, weight=1)

res_button = Label(frame14, text="response", foreground='green')
res_button.grid(row=0, column=0, sticky="news", padx=10)

# 相应 进度条
res_process_var = IntVar()
res_process_bar = Progressbar(frame14, value=0, variable=res_process_var)
res_process_bar.grid(row=0, column=1, sticky="e", )
res_process_var.set(20)

#
status_label = Label(frame14, text="Status: ")
status_label.grid(row=1, column=1, sticky="w", padx=10)

response_var = StringVar()
status_string = Label(frame14, textvariable=response_var)
status_string.grid(row=1, column=2, sticky="w", padx=10)
response_var.set("0------0")






if __name__ == "__main__":
    root.mainloop()
