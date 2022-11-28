from tkinter import *
from PIL import Image
import pygame
from random import *

root = Tk()
root.title('4 Лабораторная')
root.geometry('540x310')
root.resizable(True, True)
file = "209473.gif"

info = Image.open(file)
frames = info.n_frames  # Считывание количества кадров гиф изображения

im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
slovo = StringVar()

count = 0
anim = None
pygame.mixer.init()
up = 35


def parol():  # Функция создания ключа
    S = 'A B C D E F J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'.split()
    password = ''
    for i in range(3):
        x = ''
        d = 4
        for i in range(4):
            c = randrange(up - d)
            if i == 0: d= 0
            x += S[c]
            d += c
        password += x + '-'
    login = Label(root, text= password[:-1:])
    login.place(x=100, y=230, width=300, height=30)
    Again = Button(root, text="try again", command=lambda: try_again(login))
    Again.place(x=220, y=270, width=50, height=30)


def play():  # Функция запуска песни
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(loops=10)


def stop_music():  # Функция остановки песни
    pygame.mixer.music.stop()


def animation(count):  # Функция запуска гифки
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(130, lambda: animation(count))


def stop_animation():  # Функция остановки гифки
    global anim
    root.after_cancel(anim)


def change_button():  # Замена кнопки старт на кнопку стоп
    start.destroy()
    stop = Button(root, text="stop", command=lambda: [stop_animation(), stop_music(), change_second_button()])
    stop.place(x=480, y=280, width=50, height=30)


def change_second_button():  # Замена кнопки стоп на кнопку старт
    stop.destroy()
    start = Button(root, text="start", command=lambda: [animation(count), play(), change_button()])
    start.place(x=480, y=280, width=50, height=30)


def new_button():  # Создание кнопки активации программы
    Click = Button(root, text="click", command=lambda: parol())
    Click.place(x=20, y=280, width=50, height=30)


def try_again(login):  # Удаление сгенерируемого кода и кнопки повтора, создание кнпоки начала алгоритма
    login.destroy()
    Again.destroy()
    Click = Button(root, text="click", command=lambda: parol())
    Click.place(x=20, y=280, width=50, height=30)


gif_label = Label(root, image="")  # Открытие гифки
gif_label.pack()

start = Button(root, text="start", command=lambda: [animation(count), play(), change_button(), new_button()])
start.place(x=250, y=150, width=50, height=30)
Click = Button(root, text="click", command=lambda: parol())
Again = Button(root, text="try again", command=lambda: try_again(login))
stop = Button(root, text="stop", command=lambda: [stop_animation(), stop_music(), change_second_button()])
login = Label(root, text='')

root.mainloop()