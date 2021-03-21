from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog
from tkinter import messagebox as mb
import tkinter.ttk as ttk
from tkinter import simpledialog





root = Tk()
root.geometry("1920x1080")
#верхнее меню
mainmenu = Menu(root)
root.config(menu=mainmenu)
#файл меню
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход", )
#файл меню///
#Хэлп меню
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь")
helpmenu.add_command(label="О программе")
#Хэлп меню///
mainmenu.add_cascade(label="Файл",menu=filemenu)
mainmenu.add_cascade(label="Справка",menu=helpmenu)
#верхнее меню///
text = Text(root)
#scrollbar text
scroll = Scrollbar(root)
scroll.pack(side='right', fill='y')
scroll['command'] = text.yview
text['yscrollcommand'] = scroll.set
scroll.pack(side='right', fill='y')
text.pack(fill=BOTH, expand=True)
#scrollbar text///
root.mainloop()


