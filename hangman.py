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
# Date Last Modified: 05/26/2022

import random
import word_list
import hangman_art

user_lives = 6
list = random.choice(word_list.normal_words).lower() # chooses random word from list
save_input = []
game_end = False

size = len(list)
for size in range(size):
    save_input += "_" # fills up save_input with "_"

print("I am thinking of a five letter word...")
print(list) # debug

while (not game_end) and (user_lives > 0):
    user_input = input("Enter a letter... ").lower()
    for position in range(size + 1):
        letter = list[position] # letter is assigned the letter in the specific index
        if letter == user_input:
            save_input[position] = letter # index at [position] is assigned value of letter
            print(f"{' '.join(save_input)}") # string transformation
    if user_input not in list:
        print(f"{user_input} not in the word! lose a life")
        user_lives -= 1
        print(hangman_art.stages[user_lives])
    if "_" not in save_input:
        game_end = True

if user_lives <= 0:
    print("You lost!")
