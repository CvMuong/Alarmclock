from tkinter import *
import datetime
import time as tm
from playsound import playsound
from threading import *

root = Tk()
root.geometry("370x200")
root.title("Alarm clock")
root.configure(background="black")

def Threading():
    t1 = Thread(target = alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
        tm.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%d:%m:%y")
        print("This set date is: ", date)
        print(current_time)
        if current_time == set_alarm_timer:
            print("Time to wake up !!!")
            playsound("alarmsound.mp3")
            break

def time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, time)

    
Label(root, text="Alarm clock", font="Arian 20 bold", fg="red", bg="black").pack()
Label(root, text="Set Time", fg="cyan", font="Arian 20 bold", bg="black").pack()

time_now = Label(root, text='This time now is: ', fg="white", bg='black', font='Arian 15').place(x=70, y=150)
label = Label(root, font=("ds-digital", 12), background = "black", foreground = "cyan")
label.place(x=225, y=153)
time()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
         '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
         '20', '21', '22', '23')

hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side="left")

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60')

minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side="left")

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')

second.set(seconds[0])
sns = OptionMenu(frame, second, *seconds)
sns.pack(side="left")

Button(root, text="Set Alarm", font="Arian 10", fg="black", bg='white', command=Threading).place(x=150, y = 120)

root.mainloop()
