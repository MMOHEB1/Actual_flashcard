# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- UNIVERSAL CONSTANCE'S ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Flash cards")
root.config(padx=50, pady=50, background=f"{BACKGROUND_COLOR}")

canvas = Canvas(height=550, width=800)
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 275, image=card_back)
canvas.config(background=f"{BACKGROUND_COLOR}", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=4, rowspan=4)

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")


# BUTTONS
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=4, column=3)
wrong_button = Button(image=right_image, highlightthickness=0)
wrong_button.grid(row=4, column=0)





root.mainloop()
