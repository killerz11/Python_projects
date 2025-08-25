from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_list = {}

try:
    df = pd.read_csv("data/Words to learn")
except:
    original_data = pd.read_csv("data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = df.to_dict(orient="records")


def change_side():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white",text=current_card["English"])

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word,text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(1000, func=change_side)

def is_known():
    word_list.remove(current_card)
    next_card()
    data = pd.DataFrame(word_list)
    data.to_csv("data/Words to learn", index=False)

window = Tk()
window.title("FLASHCARD")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(1000, func=change_side)
#---------------------------------UI setup---------------------------------

#Canvas
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text="", font=("Aerial",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Aerial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
right_image = PhotoImage(file="images/right.png")
yes_button = Button(image=right_image, highlightthickness=0, command=is_known)
yes_button.grid(row=1,column=0)

cross_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=cross_image, highlightthickness=0, command=next_card)
no_button.grid(row=1,column=1)

next_card()

window.mainloop()