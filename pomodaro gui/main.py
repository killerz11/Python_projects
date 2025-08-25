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
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    Timer_label.config(text="Timer")
    ticks_mark.config(text="")
    global REPS
    REPS=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        Timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 != 0:
        count_down(work_sec)
        Timer_label.config(text="Work", fg=GREEN)

    else:
        count_down(short_break_sec)
        Timer_label.config(text="Short Break", fg=PINK)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark =""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        ticks_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODARO")
window.config(padx=100,pady=50,  bg=YELLOW)


window.after(1000)

Timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
Timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Restart", command=reset_timer)
reset_button.grid(row=2, column=2)

ticks_mark = Label(fg=GREEN,  bg=YELLOW, font=(FONT_NAME,13, "bold"))
ticks_mark.grid(row=3, column=1)

window.mainloop()