from tkinter import * 
import datetime

standby = Tk()

standby.title("Stand by")
standby.geometry("400x150")
standby.configure(bg="black")
current_time = datetime.datetime.now().strftime("%H:%M")
now = Label(standby, text=f"{current_time}", bg="black", fg="cornflowerblue", font="Arian 80 bold").pack(side="left")

standby.mainloop()