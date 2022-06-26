from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text= 'Timer', fg=GREEN)
    label2.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label['text'] = 'Break'
        label['fg'] = 'red'
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        label['text'] = 'Break'
        label['fg'] = 'pink'
    else:
        count_down(work_sec)
        label['text'] = 'Work'
        label['fg'] = 'Green'





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label2['text'] = marks



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=90, pady=50, bg=YELLOW)
label = Label(text='Timer', font=(FONT_NAME, 23, 'bold'), fg=GREEN, highlightthickness=0)
label.grid(column=1, row=0)

label2 = Label(fg=GREEN)
label2.grid(column=1, row=4)

button = Button(text='Start', highlightthickness=0, command=start_timer)
button.grid(column=0, row=3)

button2 = Button(text='Reset', highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=3)

tomato_image = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(103, 112, text="00:00", fill='white', font=(FONT_NAME, 23, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()
