from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Roll the Dice")
root.geometry("400x400")
root.configure(bg="black")

dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
dice_img = Image.open(random.choice(dice))
dice_img = dice_img.resize((100, 100), Image.LANCZOS)
dice_image = ImageTk.PhotoImage(dice_img)
label1 = dice_image


def rolling():
    dice_img = Image.open(random.choice(dice))
    dice_img = dice_img.resize((100, 100), Image.LANCZOS)
    dice_image = ImageTk.PhotoImage(dice_img)
    label1 = Label(root, image=dice_image).place(x=150, y=50)
    label1.config(image=dice_image)

Button(root, text="Roll", font="Arian 15", command=rolling).place(x=180, y=170)
root.mainloop()
