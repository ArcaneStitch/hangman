# Author: Mengyue Lu
# Description: Very basic hangman game
# Abstract: The program will start with minimal features and I will add onto it,
#           The program will start will a life system and 5 letter word to guess.
#           After the basics of the game is successfully implemented I will continue 
#           to add on features and track them through git, this will be a quiz to 
#           see if I learned enough of git, python loops and functions to create something
#           on my own.
# Additional features: I will implement the stick figure after the basics are laid out,
#                      easy medium and hard modes, a separate file that will contain the 
#                      words in three lists for each difficulty
# Date Created: 05/25/2022
# Date Last Modified: 05/25/2022

import random
import word_list

user_lives = 6
user_input = ""


list = word_list.normal_words
chosen_word = str(list).split(", ")
list_number = len(list)

print(chosen_word)