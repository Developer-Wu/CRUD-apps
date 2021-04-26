from tkinter import *
from PIL import ImageTk, Image
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
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label['text'] = 'Timer'




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    #if 1,3,5,7
    if reps % 2 != 0:
        countdown(WORK_MIN*60)
        timer_label['text'] = 'Work'
        timer_label['fg'] = GREEN

    elif reps % 2 == 0 and reps % 8 != 0:
        countdown(SHORT_BREAK_MIN*60)
        timer_label['text'] = 'Short Break'
        timer_label['fg'] = PINK
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        timer_label['text'] = 'Long Break'
        timer_label['fg'] = RED



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec:02d}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown,count - 1)
    else:
        start_timer()
        global reps
        mark =""
        for _ in range(math.floor(reps/2)):
            mark += "✔️"
        tick_label['text'] = mark




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title('Pomodoro')
window.config(padx= 100, pady=50, bg=YELLOW)

start_btn = Button(text='Start', bg= YELLOW, highlightthickness= 0, command=start_timer)
start_btn.grid(column=1,row=3)


timer_label = Label(text='Timer', bg= YELLOW, fg= GREEN, font= (FONT_NAME, 30))


reset_btn = Button(text='Reset', bg=YELLOW,highlightthickness= 0, command=reset_timer)
reset_btn.grid(column= 3, row='3')

tick_label= Label(text="️", fg= GREEN, bg=YELLOW)
tick_label.grid(column=2,row=4)
timer_label.grid(column=2,row='1')
canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)


tomato_img = ImageTk.PhotoImage(Image.open('tomato.png'))
canvas.create_image(100,112, image=tomato_img)
canvas_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,'bold'))
canvas.grid(column=2,row=2)









window.mainloop()
