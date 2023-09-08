from numpy import random
import numpy as np

rp = 0

while rp == 0:
    bot = random.choice([0, 1, 2])
    if bot == 0:
        bot = "Keo"
    elif bot == 1:
        bot = "Bua"
    else:
        bot = "Bao"

    you = input("Enter your selection: ")

    print(f"Bot selected: {bot}")
    print(f"You selected: {you}")

    if (bot == you):
        print("Draw")
    elif (bot == "Keo" and you == "Bao"):
        print("You lose")
    elif (bot == "Keo" and you == "Bua"):
        print("You win")
    elif (bot == "Bua" and you == "Keo"):
        print("You lose")
    elif (bot == "Bua" and you == "Bao"):
        print("You win")
    elif (bot == "Bao" and you == "Bua"):
        print("You lose")
    elif (bot == "Bao" and you == "Keo"):
        print("You win")

    rp = input("\n0 = Continue \t 1 = Break: \nChoose 0 or 1: ")
    rp = int(rp)



