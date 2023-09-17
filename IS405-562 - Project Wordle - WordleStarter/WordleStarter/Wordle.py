# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    def enter_action(s):
        entered_word = s.lower()  # Convert entered word to lowercase for case-insensitive comparison
        if entered_word in FIVE_LETTER_WORDS:
            gw.show_message("You guessed a valid word.")
        else:
            gw.show_message("Not in word list")
        

    def placeWordFirstRow(wordlewindow):
        row = 0
        num = random.randint(0, len(FIVE_LETTER_WORDS))
        for col in range(N_COLS):
            wordlewindow.set_square_letter(row, col, FIVE_LETTER_WORDS[num][col])

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    placeWordFirstRow(gw)


# Startup code

if __name__ == "__main__":
    wordle()
