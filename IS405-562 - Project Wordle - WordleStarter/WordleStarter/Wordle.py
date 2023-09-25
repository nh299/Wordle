# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
The code is now a functioning wordle game!
"""

import os
import random
import tkinter as tk
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def start_game(color_scheme_choice, game_mode_choice):
    actual_word = ""
    
    DEFAULT_COLOR_SCHEME = {
        "CORRECT_COLOR": "#66BB66",  
        "PRESENT_COLOR": "#CCBB66",  
        "MISSING_COLOR": "#999999"   
    }
    ALTERNATE_COLOR_SCHEME = {
        "CORRECT_COLOR": "#4466BB", 
        "PRESENT_COLOR": "#FF6666",  
        "MISSING_COLOR": "#888888"   
    }

    current_color_scheme = DEFAULT_COLOR_SCHEME

    if color_scheme_choice == 'Alternate':
        current_color_scheme = ALTERNATE_COLOR_SCHEME

    hard_mode = game_mode_choice == 'Hard mode'
    correct_guesses = {}

    def validate_guess_hard_mode(guess):
        for position, letter in correct_guesses.items():
            if guess[position] != letter:
                return False
        return True

    def enter_action(s):
        guess = s.upper()

        if len(guess) != len(actual_word):
            gw.show_message("Guess should be of length " + str(len(actual_word)))
            return

        if guess.lower() in FIVE_LETTER_WORDS:
            if hard_mode and not validate_guess_hard_mode(guess):
                gw.show_message("You must use the known letters in their correct positions!")
                return

            colors = determine_square_colors(guess, actual_word)
            row = gw.get_current_row()

            for col, color in enumerate(colors):
                gw.set_square_color(row, col, color)
                if color == current_color_scheme["CORRECT_COLOR"]:
                    correct_guesses[col] = guess[col]

            if guess == actual_word:
                gw.show_message("Congratulations! You guessed the correct word.")
            else:
                gw.set_current_row(row + 1)

            for letter in guess:
                if letter in actual_word:
                    gw.set_key_color(letter, current_color_scheme["CORRECT_COLOR"])
                else:
                    gw.set_key_color(letter, current_color_scheme["MISSING_COLOR"])

        else:
            gw.show_message("Not in word list")

    def determine_square_colors(guess, word):
        colors = []
        used_indices = []
        
        for i in range(len(guess)):
            if guess[i] == word[i]:
                colors.append(current_color_scheme["CORRECT_COLOR"])
                used_indices.append(i)
            else:
                colors.append(None)

        for i in range(len(guess)):
            if colors[i] is None:
                for j, letter in enumerate(word):
                    if letter == guess[i] and j not in used_indices:
                        colors[i] = current_color_scheme["PRESENT_COLOR"]
                        used_indices.append(j)
                        break
        
        for i in range(len(guess)):
            if colors[i] is None:
                colors[i] = current_color_scheme["MISSING_COLOR"]

        return colors


    def placeWordFirstRow(wordlewindow):
        nonlocal actual_word
        num = random.randint(0, len(FIVE_LETTER_WORDS) - 1)
        actual_word = FIVE_LETTER_WORDS[num].upper()
        for col in range(N_COLS):
            wordlewindow.set_square_letter(0, col, actual_word[col])



    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    placeWordFirstRow(gw)
    gw.show()  # Ensure the window pops up and has the focus


def setup_screen():
    root = tk.Tk()
    root.title("Wordle Setup")

    color_scheme_var = tk.StringVar(value="Default")
    game_mode_var = tk.StringVar(value="Regular")

    def on_submit():
        selected_color_scheme = color_scheme_var.get()
        selected_game_mode = game_mode_var.get()

        root.destroy()  # Close the setup window
        start_game(selected_color_scheme, selected_game_mode)

    tk.Label(root, text="Choose a color scheme:").pack(pady=10)
    color_dropdown = tk.OptionMenu(root, color_scheme_var, "Default", "Alternate")
    color_dropdown.pack(pady=10)

    tk.Label(root, text="Choose game mode:").pack(pady=10)
    game_mode_dropdown = tk.OptionMenu(root, game_mode_var, "Regular", "Hard mode")
    game_mode_dropdown.pack(pady=10)

    tk.Button(root, text="Start Game", command=on_submit).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    setup_screen()


