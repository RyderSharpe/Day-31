# Import necessary libraries
import tkinter as tk
from tkinter import *  # For UI components
import pandas  # For data handling
import random  # For random selection
import time
from tkinter import messagebox  # For displaying messages

# Define color constants
WHITE = "#ffffff"
BACKGROUND_COLOR = "#B1DDC6"
DARK_PURPLE = "#522258"
LIGHT_PURPLE = "#8C3061"
RED = "#C63C51"
ORANGE = "#D95F59"
BLACK = "#000000"

# Load data from CSV file
data = pandas.read_csv("data/short_list.csv", header=0, index_col=False)

# ---------------------------- DATA ------------------------------- #
def next_card():
    """
    Loads random French word and schedules flip_card after 2 seconds.
    """
    global data, rand_french, flip_timer
    window.after_cancel(flip_timer)
    # Reset canvas image to front
    canvas.itemconfig(canvas_image, image=card_front_img)

    # Reset text labels
    canvas.itemconfig(french, text="french")

    # Select random French word
    rand_french = str(random.choice(data["french"].to_list()))
    canvas.itemconfig(english, text=rand_french)

    # Schedule flip_card after 2 seconds
    flip_timer = window.after(3000, flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """
    Flips card to show English translation.
    """
    global data, rand_french
    try:

        # Find corresponding English translation
        english_translation = data[data.french == rand_french]
        canvas.itemconfig(english, text=english_translation['english'].values[0])

        # Update text labels
        canvas.itemconfig(french, text="english")
        canvas.itemconfig(canvas_image, image=card_back_img)
    except:
        pass
# ---------------------------- ✅ BUTTON ------------------------------- #
def check():
    global rand_french, data


def find(rand_french):
    for row in data:
        if row == rand_french:
            huh = data.lin_num
            return huh
print(find)




# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Apprenons le Français!")  # Set window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure window padding and background color

flip_timer = window.after(3000, func=flip_card)

# Create a canvas for displaying the flashcard
canvas = Canvas(
    width=800,  # Canvas width
    height=526,  # Canvas height
    bg=BACKGROUND_COLOR,  # Canvas background color
    highlightthickness=0  # Remove border
)

# Load the card front and back images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
# Display front card image initially
canvas_image = canvas.create_image(400, 263, image=card_front_img)

# Place the canvas in the window's grid layout
canvas.grid(row=0, column=0, columnspan=2)

# Create French and English word text fields on the canvas
french = canvas.create_text(400, 150, text="french", font=("Arial", 40, "italic"))
english = canvas.create_text(400, 263, text="english", font=("Arial", 40, "bold"))

# ❌ ❌ ❌ BUTTON WRONG (user does not know the word) ❌ ❌ ❌
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# ✅ ✅ ✅ BUTTON RIGHT (user knows the word) ✅ ✅ ✅

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=find)
known_button.grid(row=1, column=1)

# Start the Tkinter event loop
window.mainloop()
