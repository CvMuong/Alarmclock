from numpy import random
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import time as tm

spc = Tk()
spc.title("Stone paper scissors")
spc.geometry("400x500")
spc.config(background="black")
title = Label(spc, text="Play Game", fg="blue", bg="black", font="Arian 30 bold").pack()
Label(spc, text='You choose', fg='white', bg='black', font='Arian 15'). place(x=45, y=50)

# stone
stone_image = Image.open("q.png")
stone_image = stone_image.resize((100, 100), Image.LANCZOS)
stone = ImageTk.PhotoImage(stone_image)
# label1 = Label(image=stone)
# label1.pack()

# paper
paper_image = Image.open("tải xuống.png")
paper_image = paper_image.resize((100, 100), Image.LANCZOS)

# scissors
scissors_image = Image.open("tải xuống (1).png")
scissors_image = scissors_image.resize((100, 100), Image.LANCZOS)
    
frame = Frame(spc)
frame.pack()

you = StringVar(spc)
menu = ('None', 'Stone', 'Paper', 'Scissors')
you.set(menu[0])
choose = OptionMenu(frame, you, *menu)
choose.pack(side='left')

def Process():
    you_choose = f"{you.get()}"
    bot = random.choice(["Stone", "Paper", "Scissors"])
    if (bot == you_choose):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="DRAW", font="Arian 20 bold", fg="cyan", bg="black").place(x=160, y=185)
    elif (bot == "Scissors" and you_choose == "Paper"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU LOSE", font="Arian 20 bold", fg="red", bg="black").place(x=160, y=185)
    elif (bot == "Scissors" and you_choose == "Stone"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU WIN", font="Arian 20 bold", fg="green", bg="black").place(x=160, y=185)
    elif (bot == "Stone" and you_choose == "Scissors"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU LOSE", font="Arian 20 bold", fg="red", bg="black").place(x=160, y=185)
    elif (bot == "Stone" and you_choose == "Paper"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU WIN", font="Arian 20 bold", fg="green", bg="black").place(x=160, y=185)
    elif (bot == "Paper" and you_choose == "Stone"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU LOSE", font="Arian 20 bold", fg="red", bg="black").place(x=160, y=185)
    elif (bot == "Paper" and you_choose == "Scissors"):
        bot_choose = Label(spc, text='Bot choose:', fg='white', bg='black', font='Arian 15'). place(x=45, y=150)
        Label(spc, text=f"{bot}", fg='blue', bg='black', font='Arian 20').place(x=160, y=147)
        Label(spc, text='Result:', fg='white', bg='black', font='Arian 15').place(x=45, y=185)
        Label(spc, text="YOU WIN", font="Arian 20 bold", fg="green", bg="black").place(x=160, y=185)

Button(spc, text='Play', fg='black', bg='white', font='Arian 15', command=Process).place(x=170, y=100)
spc.mainloop()
