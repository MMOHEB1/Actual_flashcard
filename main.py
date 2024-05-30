# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- UNIVERSAL CONSTANCE'S ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Flash cards")
root.config(padx=50, pady=50, background=f"{BACKGROUND_COLOR}")
# root.wm_attributes('-transparentcolor', '#ab23ff')

canvas = Canvas(width=800, height=550)
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 275, image=card_back)
canvas.config(background=f"{BACKGROUND_COLOR}", highlightthickness=0)
# canvas.create_text(400, 100, text=f"English \n The word in English", font=)
canvas.grid(row=0, column=0, columnspan=3, rowspan=3)

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

# LABELS:
english_label = Label(text=f"English", font=('Courier', 30))
english_label.config(highlightthickness=0)
english_label.grid(row=0, column=1)

english_word = Label(text=f"\nThe word in English", font=('Courier', 35, "bold"))
english_word.config(highlightthickness=0)
english_word.grid(row=1, column=1)



# BUTTONS
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=4, column=2)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=4, column=0)





root.mainloop()
