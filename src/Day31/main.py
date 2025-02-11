import tkinter as tk
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_HEIGHT = 526
CANVAS_WIDTH = 800

words_list = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_to_english = {entry['French']: entry['English'] for entry in words_list}
else:
    french_to_english = {entry['French']: entry['English'] for entry in data.to_dict(orient="records")}

def new_random_word():
    global timer

    canvas.itemconfig(canvas_img, image=card_front_img)
    random_french_word = random.choice(words_list)["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_french_word, fill="Black")
    root.after_cancel(timer)
    timer = root.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    current_french_word = canvas.itemcget(card_word, "text")
    english_word = french_to_english.get(current_french_word)
    canvas.itemconfig(card_word, text=english_word, fill="white")

root = tk.Tk()
root.title("Flashy")
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)

timer = root.after(3000, func=flip_card)

# Images
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_front_img = tk.PhotoImage(file="images/card_front.png")
x_img = tk.PhotoImage(file="images/wrong.png")
check_img = tk.PhotoImage(file="images/right.png")

# Canvas
canvas = tk.Canvas()

canvas.config(
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    background=BACKGROUND_COLOR,
    highlightthickness=0)

canvas_img = canvas.create_image(
    CANVAS_WIDTH / 2,
    CANVAS_HEIGHT / 2,
    image=card_front_img)

card_title = canvas.create_text(
    CANVAS_WIDTH / 2,
    150,
    font=("Ariel", 40, "italic"),
    text="French")

card_word = canvas.create_text(
    CANVAS_WIDTH / 2,
    CANVAS_HEIGHT / 2,
    font=("Ariel", 60, "bold"),
    text=random.choice(words_list)["French"])

canvas.grid(column=0, row=0, columnspan=2)

# Buttons

def check_button_click():
    current_french_word = canvas.itemcget(card_word, "text")
    french_to_english.pop(current_french_word, None)
    new_random_word()

def x_button_click():
    df = pandas.DataFrame(list(french_to_english.items()), columns=['French', 'English'])
    df.to_csv("data/words_to_learn.csv", index=False)
    new_random_word()


x_button = tk.Button(image=x_img, highlightthickness=0)
x_button.config(cursor="hand2", command=new_random_word)
x_button.grid(column=0, row=1)

check_button = tk.Button(image=check_img, highlightthickness=0)
check_button.config(cursor="hand2", command=check_button_click)
check_button.grid(column=1, row=1)

root.mainloop()
