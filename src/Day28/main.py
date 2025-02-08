import math
import tkinter as tk
from PIL import Image as PillowImage, ImageTk as PillowImageTk

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
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", foreground="black")
    check_label.config(text="")
    global reps
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
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # using dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# Configure the window object
root = tk.Tk()
root.title("Pomodoro")
root.resizable(width=False, height=False)
root.config(padx=20, pady=20, bg=YELLOW)

# Prepare the tomato image
image = PillowImage.open("tomato.png")
resize_image = image.resize((300, 300))
tomato_img = PillowImageTk.PhotoImage(resize_image)

# Add the canvas
canvas = tk.Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0, borderwidth=0)
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(
    150,
    180,
    text="00:00",
    font=(FONT_NAME, 50, "bold"),
    fill="white")
canvas.grid(column=1, row=1)

# Configure and place the timer label
timer_label = tk.Label(
    text="TIMER",
    font=("Consolas", 50),
    bg=YELLOW,
    foreground="black")
timer_label.grid(column = 1, row = 0)

# Configure and place the start button
start_button = tk.Button(
    text="START",
    borderwidth = 0,
    highlightthickness= 0,
    font=("Consolas", 20),
    cursor="hand2",
    bg=RED,
    activebackground=RED,
    fg="white",
    command=start_timer)
start_button.grid(column = 0, row = 1, padx=(0, 50), pady=(50, 0))

# Configure and place the reset button
reset_button = tk.Button(
    text="RESET",
    borderwidth = 0,
    highlightthickness= 0,
    font=("Consolas", 20),
    cursor="hand2",
    bg=RED,
    activebackground=RED,
    fg="white",
    command=reset_timer)
reset_button.grid(column = 2, row = 1, padx=(50, 0), pady=(50, 0))

# Configure and place the check label
check_label = tk.Label(
    font=("Consolas", 30),
    bg=YELLOW,
    foreground=GREEN)
check_label.grid(column = 1, row = 3, pady=(20, 0))

root.mainloop()