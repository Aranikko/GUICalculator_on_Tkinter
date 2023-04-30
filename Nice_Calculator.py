from tkinter import *
c = 0
root = Tk()
root["bg"] = "#6900ad"
txt_1 = Label(text="Первое значение", padx=10, pady=10, bg = '#b94dff') # текст 1
txt_2 = Label(text="Второе значение", padx=10, pady=10, bg = '#b94dff') # текст 2
txt_3 = Label(text="Считаем...", padx=10, pady=10, bg = '#b94dff') # текст 3
ent_1 = Entry() # ввод 1
ent_2 = Entry() # ввод 2
def sum(): # функция для подсчета суммы с ввведеных чисел
    global c
    c = int(ent_1.get()) + int(ent_2.get())
summ = Button(text="+", padx=15, pady=15, command=sum, bg = '#e1b3ff', activebackground='#6a00ad') # кнопка +
def min(): # функция для подсчета вычитания с введеных чисел
    global c
    c = int(ent_1.get()) - int(ent_2.get())
minus = Button(text="-", padx=15, pady=15, command=min, bg = '#e1b3ff', activebackground='#6a00ad') # кнопка -
def mnojj(): # функция для подсчета умножения с введеных чисел
    global c
    c = int(ent_1.get()) * int(ent_2.get())
mnoj = Button(text="*", padx=15, pady=15, command=mnojj, bg = '#e1b3ff', activebackground='#6a00ad') # кнопка *
def dele(): # функция для подсчета деления с введеных чисел
    global c
    c = int(ent_1.get()) / int(ent_2.get())
delen = Button(text="/", padx=15, pady=15, command=dele, bg = '#e1b3ff', activebackground='#6a00ad') # кнопка /
def enrr(): # вывод подсчета
    global  c
    txt_3.configure(text=c)
enr = Button(text="=", padx=15, pady=15, command=enrr, bg = '#e1b3ff', activebackground='#6a00ad') # кнопка =
def button(): # функция со всем кнопками (для разгрузки кнопок)
    enr.pack(side=BOTTOM)
    summ.pack(side=RIGHT)
    minus.pack(side=RIGHT)
    mnoj.pack(side=LEFT)
    delen.pack(side=LEFT)
    txt_1.pack(side=LEFT)
    txt_2.pack(side=RIGHT)
    txt_3.pack(side=BOTTOM)
    ent_1.pack(side=LEFT)
    ent_2.pack(side=RIGHT)
    pass
button() # выводит на экран кнопки(выполнение функции button)
root.mainloop()