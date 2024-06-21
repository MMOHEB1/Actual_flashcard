# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import time
import pandas

# ---------------------------- UNIVERSAL CONSTANCE'S ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- READING DATA ------------------------------- #
def word_collection():
    data = pandas.read_csv("data/french_words.csv")
    english_list = data["English"].tolist()
    for word in english_list:
        time.sleep(1)
        return word

def french_word():
    data = pandas.read_csv("data/french_words.csv")
    english_list = data[""].tolist()
    for word in english_list:
        time.sleep(1)
        return word

# ---------------------------- TIMER SETUP ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #
# ENGLISH SIDE:
root = Tk()
root.title("Flash cards")
root.config(padx=50, pady=50, background=f"{BACKGROUND_COLOR}")

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


canvas = Canvas(width=800, height=550)
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 275, image=card_back)
canvas.config(background=f"{BACKGROUND_COLOR}", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

# LABELS:
e_label = Label(text=f"English", font=('Courier', 30))
e_label.config(highlightthickness=0)
e_label.grid(row=0, column=1)
e_word = Label(text=f"\n{word_collection()}", font=('Courier', 35, "bold"))
e_word.config(highlightthickness=0)
e_word.grid(row=1, column=1)


# FRENCH SIDE:
def french_side():
    white_canvas = Canvas(width=800, height=550)
    card_front = PhotoImage(file="images/card_front.png")
    white_canvas.create_image(400, 275, image=card_front)
    white_canvas.config(highlightthickness=0)
    white_canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

    # LABELS:
    f_label = Label(text=f"French", font=('Courier', 30))
    f_label.config(highlightthickness=0)
    f_label.grid(row=0, column=1)
    f_word = Label(text=f"\nThe word in French", font=('Courier', 35, "bold"))
    f_word.config(highlightthickness=0)
    f_word.grid(row=1, column=1)


# BUTTONS
right_button = Button(image=right_image, highlightthickness=0, command=french_side)
right_button.grid(row=4, column=2)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=4, column=0)

# english_side()

root.mainloop()
