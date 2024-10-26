from tkinter import *
import datetime # comment all and --> print(datetime.datetime.now()) to check the output

# create a function to update the time
def date_time():
    current_time = datetime.datetime.now() # get the current time
    hr = current_time.strftime("%I") # get the current hour
    min = current_time.strftime("%M") # get the current minute
    sec = current_time.strftime("%S") # get the current second
    am = current_time.strftime("%p") # get the current phase
    date = current_time.strftime("%d") # get the current date
    month = current_time.strftime("%m") # get the current month
    year = current_time.strftime("%y") # get the current year, Y --> 2024 & y --> 24
    day = current_time.strftime("%a") # get the current day, A --> Sunday & a --> Sun
    
    lab_hr.config(text=hr) # update the hour
    lab_min.config(text=min) # update the minute
    lab_sec.config(text=sec) # update the second
    lab_am.config(text=am) # update the phase
    lab_date.config(text=date) # update the date
    lab_day.config(text=month) # update the m
    lab_month.config(text=year) # update the y
    lab_year.config(text=day) # update the day
    
    lab_hr.after(1000, date_time) # update the time after 1000ms = 1sec

    

import tkinter as tk
from tkinter import Canvas

clock = Tk() # function to create a window
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.resizable(False, False)  # Disable window resizing to block maximize

#clock.configure(bg='black')
## Also use Gradient Background with create a function
def create_gradient(canvas, width, height, color1, color2, color3):
    limit = height // 2
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        r3, g3, b3 = canvas.winfo_rgb(color3)
        
        r = int(r1 * (limit - i) / limit + r2 * i / limit) if i < limit else int(r2 * (height - i) / limit + r3 * (i - limit) / limit)
        g = int(g1 * (limit - i) / limit + g2 * i / limit) if i < limit else int(g2 * (height - i) / limit + g3 * (i - limit) / limit)
        b = int(b1 * (limit - i) / limit + b2 * i / limit) if i < limit else int(b2 * (height - i) / limit + b3 * (i - limit) / limit)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        canvas.create_line(0, i, width, i, fill=color)

canvas = Canvas(clock, width=1000, height=500)
canvas.pack()

create_gradient(canvas, 1000, 500, 'black', 'dark blue', 'violet')

# Box 1
lab_hr = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_hr.place(x=75+60, y=40,height=110, width=100)
lab_hr_txt = Label(clock, text="Hour", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=75+60, y=150, height=30, width=100)

# Box 2
lab_min = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_min.place(x=325, y=40,height=110, width=100)
lab_hr_txt = Label(clock, text="min", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=325, y=150, height=30, width=100)


# Box 3
lab_sec = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_sec.place(x=575-40, y=40,height=110, width=100)
lab_hr_txt = Label(clock, text="sec", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=575-40, y=150, height=30, width=100)

# Box 4
lab_am = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_am.place(x=825-(40+60), y=40,height=110, width=120)
lab_hr_txt = Label(clock, text="phase", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=825-(40+60), y=150, height=30, width=120)

# Box 1
lab_date = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_date.place(x=75+60, y=250,height=110, width=100)
lab_date_txt = Label(clock, text="Date", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=75+60, y=350+10, height=30, width=100)

# Box 2
lab_day = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_day.place(x=325, y=250,height=110, width=100)
lab_day_txt = Label(clock, text="Month", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=325, y=350+10, height=30, width=100)


# Box 3
lab_month = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_month.place(x=575-40, y=250,height=110, width=100)
lab_month_txt = Label(clock, text="Year", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=575-40, y=350+10, height=30, width=100)

# Box 4
lab_year = Label(clock,text="00", font=("Helvetica", 50, "bold"), bg='black', fg='white')
lab_year.place(x=825-(40+60), y=250,height=110, width=120)
lab_year_txt = Label(clock, text="Day", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=825-(40+60), y=350+10, height=30, width=120)

lab_year_txt = Label(clock, text="by AKASHDIP MAHAPATRA", font=("Helvetica", 10), bg='violet', fg='White').place(x=820, y=470, height=30, width=180)


date_time() # function to run the time



clock.mainloop() # function to run the window
