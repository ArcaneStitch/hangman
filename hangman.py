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

list = word_list.normal_words[:]
list_number = len(list)

random_word = random.randint(0, list_number - 1)
chosen_word = list[random_word]
print(chosen_word)
print(list_number)

#user_input = input("I am thinking of a five letter word... ")
