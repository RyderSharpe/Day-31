# Import necessary libraries
import tkinter as tk
from tkinter import *  # For UI components
import pandas
import random
from tkinter import messagebox  # For displaying messages


# Define color constants
WHITE ="#ffffff"
BACKGROUND_COLOR = "#B1DDC6"
DARK_PURPLE = "#522258"
LIGHT_PURPLE = "#8C3061"
RED = "#C63C51"
ORANGE = "#D95F59"
BLACK = "#000000"

# ---------------------------- DATA ------------------------------- #
def next_card():

    # Load data
    data = pandas.read_csv("data/words.csv", header=0, index_col=False)

    # Select random French word
    rand_french = str(random.choice(data["french"].to_list()))
    canvas.itemconfig(english, text=rand_french)

    # # Find corresponding English translation
    # english_translation = data[data.french == rand_french]
    # canvas.itemconfig(english, text=english_translation['english'].values[0])

# ---------------------------- FLIP CARD ------------------------------- #





# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Apprenons le Français!")  # Set window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure window padding and background color

# Create a canvas for displaying the flashcard
canvas = Canvas(
    width=800,  # Canvas width
    height=526,  # Canvas height
    bg=BACKGROUND_COLOR,  # Canvas background color
    highlightthickness=0  # Remove border
)
# Load the card front image
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)

# Load the back card
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_back_img)

# Place the canvas in the window's grid layout
canvas.grid(row=0, column=0, columnspan=2)


# Create French and English word via canvas
french = canvas.create_text(400, 150, text="french", font=("Arial", 40, "italic"))
english = canvas.create_text(400, 263, text="english", font=("Arial", 40, "bold"))

# BUTTON WRONG
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)


# BUTTON RIGHT
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)


# Start the Tkinter event loop
window.mainloop()