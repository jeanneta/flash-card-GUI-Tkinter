from tkinter import *
from random import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
dict_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")

    dict_to_learn = original_data.to_dict(orient="records")
else:
    # orients = "Records" to make it list base
    dict_to_learn = data.to_dict(orient="records")
    # print(dict_to_lear)


def known_word():
    # print(len(dict_to_lear))
    dict_to_learn.remove(random_card)
    # print(len(dict_to_lear))
    new_random_word()
    data = pandas.DataFrame(dict_to_learn)
    # print(data)
    data.to_csv("data/words_to_learn.csv", index=False)


def new_random_word():
    global random_card, flip_timer
    window.after_cancel(flip_timer)

    random_card = choice(dict_to_learn)
    print(random_card)
    print(type(random_card))
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_card["French"], fill="black")
    # To change the image:
    canvas.itemconfig(canvas_image_first, image=first_image)
    # After xxx Millisecond, this function will do xxx
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_card["English"], fill="white")
    # To change the image:
    canvas.itemconfig(canvas_image_first, image=second_image)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# After xxx Millisecond, this function will do xxx
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
first_image = PhotoImage(file="images/card_front.png")
second_image = PhotoImage(file="images/card_back.png")
canvas_image_first = canvas.create_image(400, 263, image=first_image)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=new_random_word)
wrong_button.config(padx=50, pady=50)
wrong_button.grid(column=0, row=1)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=known_word)
correct_button.config(padx=50, pady=50)
correct_button.grid(column=1, row=1)

new_random_word()

window.mainloop()
