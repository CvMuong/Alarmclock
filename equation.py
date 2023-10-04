from tkinter import *
import math
from threading import *

eq = Tk()

eq.title("Equation")
eq.configure(bg="black")
eq.geometry("400x400")

def Threading():
    t1 = Thread(target=Equation)
    t1.start()

def Equation():
    a = int(soa.get())
    b = int(sob.get())
    c = int(soc.get())
    Delta = (pow(b, 2) - (4*a*c))
    if Delta < 0:
        Label(eq, text=f"Phương trình có 2 nghiệm \n x1 = 2 \n x2 = 2", fg="black", bg="black", font="Arian 15").place(x=110, y=210)
        Label(eq, text="Phương trình vô nghiệm", fg = "green", bg="black", font="Arian 15").place(x=110, y=210)
    elif Delta == 0:
        x = (-b / (2*a))
        Label(eq, text=f"Phương trình có 2 nghiệm \n x1 = 2 \n x2 = 2", fg="black", bg="black", font="Arian 15").place(x=110, y=210)
        Label(eq, text=f"Phương trình có nghiệm kép \n x = {x}", fg="green", bg="black", font="Arian 15").place(x=110, y=210)
    else:
        Delta = math.sqrt(Delta)
        x1 = ((-b + Delta) / (2*a))
        x2 = ((-b - Delta) / (2*a))
        Label(eq, text=f"Phương trình có 2 nghiệm \n x1 = {x1} \n x2 = {x2}", fg="black", bg="black", font="Arian 15").place(x=110, y=210)
        Label(eq, text=f"Phương trình có 2 nghiệm \n x1 = {x1} \n x2 = {x2}", fg="green", bg="black", font="Arian 15").place(x=110, y=210)

soa = StringVar()
sob = StringVar()
soc = StringVar()

Label(eq, text="Giải Phương Trình Bậc 2", fg="cornflowerblue", bg="black", font="Arian 20").place(x=47, y=10)
Label(eq, text="Nhập a", fg="white", bg="black", font="Arian 15").place(x=30,y=60)
Entry(eq, textvariable=soa, width=10).place(x=30, y=90)
Label(eq, text="Nhập b", fg="white", bg="black", font="Arian 15").place(x=160,y=60)
Entry(eq, textvariable=sob, width=10).place(x=160, y=90)
Label(eq, text="Nhập c", fg="white", bg="black", font="Arian 15").place(x=305,y=60)
Entry(eq, textvariable=soc, width=10).place(x=305, y=90)
Button(eq, text="Giải", fg="black", bg="cyan", font="Arian 15", command=Threading).place(x=170, y=150)
Label(eq, text="Kết quả:", fg="cornflowerblue", bg="black", font="Arian 15").place(x=30, y=210)

eq.mainloop()