from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import *
from tkinter import messagebox as mb, filedialog
import tkinter.ttk as ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.messagebox import *

def open_file():
    text.delete(1.0, END)
    file = askopenfile()
    for i in file:
        text.insert(END, i)
    file_name['text'] = file.name

def save_as_file():
    file = asksaveasfile(defaultextension=".txt")
    file.write(Text.get(1.0, END))
    file_name['text'] = file.name

def save_file():
    file = file_name['text']
    if file not in ["Здесь будет имя открытого файла", None, '']:
        with open(file, "w") as f:
            f.write(text.get(1.0, END))






root = Tk()
root.title('Matewriter')
root.geometry("1920x1080")
#верхнее меню
mainmenu = Menu(root)
root.config(menu=mainmenu)
text = Text(root)

def new_file():
   text.pack(fill=BOTH, expand=True)

#файл меню
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=open_file)
filemenu.add_command(label="Новый", command=new_file)
filemenu.add_command(label="Сохранить...",command=save_file)
filemenu.add_command(label='Сохранить как...',command=save_as_file)

filemenu.add_separator()
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

#scrollbar text
scroll = Scrollbar(root)
scroll.pack(side='right', fill='y')
scroll['command'] = text.yview
text['yscrollcommand'] = scroll.set
file_name = Label(root, text="")
file_name.pack()
scroll.pack(side='right', fill='y')

#scrollbar text///
root.mainloop()


