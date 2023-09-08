from tkinter import *
import datetime
import time as tm
import winsound

def alarm(set_alarm_timer):
    while True:
        current_time = datetime.datetime.now()
        tm.sleep(10)
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

def time():
    current_time = datetime.datetime.now()
    string = current_time.strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

clock.title("DataFlair Alarm Clock")
clock.geometry("370x200")
clock.configure(background="black")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=150)
# addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 150)
addTime_hour = Label(clock, text = "Hour", bg = "black", fg = "white", font = 20).place(y=50)
addTIme_min = Label(clock, text = "Min", bg = "black", fg = "white", font = 20).place(x=120,y=50)
addTime_sec = Label(clock, text = "Sec", bg = "black", fg = "white", font = 20).place(x=230,y=50)
# setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",10,"bold")).place(x=110, y=10)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue", bg = "black", font = 20).place(x=90, y=15)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
current_time = datetime.datetime.now()
# now = current_time.strftime("%H:%M:%S %p")



#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 10).place(x=50,y=55)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 10).place(x=160,y=55)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 10).place(x=270,y=55)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="black", bg= "white", width = 10,command = actual_time()).place(x =150,y=90)
label = Label(clock, font=("ds-digital", 11), background = "black", foreground = "cyan")
label.place(x=220, y=123)
time()
timenow = Label(clock, text = f"Thís time now is: ", bg = "black", fg = "white", font = 10).place(x=60,y=120)

clock.mainloop()
#Execution of the window.