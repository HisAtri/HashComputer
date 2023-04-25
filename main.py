import base64
import ctypes
import os
from tkinter import *
from tkinter.ttk import *

from icon import img
from cohash import *

global textshow
textshow = ""
#ui
#使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

root=Tk()
root.tk.call('tk', 'scaling', ScaleFactor/68)
root.title("HashComputer")
root.geometry('960x580')
root.resizable(False, False)
tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

style = Style()

varhash = ["md5", "sha1", "sha244", "sha256", "sha384", "sha512"]
strhash = StringVar(root)
strhash.set(varhash[0])

strann = Label(root,text="输入待转换的文本")
strann.place(relx=0.05,rely=0.025)

strentry = Text(root)
strentry.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)

textcomb = Combobox(root, state="readonly", values = varhash, textvariable = strhash)
textcomb.place(relx=0.05,rely=0.4,relwidth=0.2)

hashshow = Text(root)
hashshow.configure(state=DISABLED)
hashshow.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.45)


# 创建一个按钮
def on_button_click():
    # 从输入框和下拉框中获取值
    instr = str(strentry.get("1.0","end-1c"))
    intype = str(textcomb.get())
    global textshow

    # 将这两个值传递给需要执行的函数
    textshow = compute(instr, intype)
    #在文本框中显示内容
    hashshow.config(state=NORMAL)   #恢复可编辑
    hashshow.delete('1.0',END)      #清空
    hashshow.insert('1.0',textshow) #插入内容
    hashshow.config(state=DISABLED) #禁止编辑


button = Button(root, text='执行', command=on_button_click)
button.place(relx=0.55,rely=0.4)

root.mainloop()