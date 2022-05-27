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
# Disclaimer: I am aware there might be vulgar and crude words in the lists, I have
#             randomly pulled long lists of words out without filtering them, there
#             still might be vulgar words hidden in the lists, be aware of that.
# Date Created: 05/25/2022
# Date Last Modified: 05/26/2022

import random
import word_list
import hangman_art

user_lives = 6
cheater = "cheater"
user_difficulty_choice = input("easy, medium, or hard?: ").lower()

if user_difficulty_choice == "easy":
    list = random.choice(word_list.combined_list[0]).lower() # chooses random easy word from list
elif user_difficulty_choice == "medium":
    list = random.choice(word_list.combined_list[1]).lower() # chooses random mediumwo rd from list
elif user_difficulty_choice == "hard":
    list = random.choice(word_list.combined_list[2]).lower() # chooses random hard word from list
elif user_difficulty_choice == cheater:
    print("Cheater!, foresight unlocked")
    list = random.choice(random.choice(word_list.combined_list)).lower()
    print(list)
else:
    print("Choose a valid option, you lose!")
    quit()

save_input = []
game_end = False

size = len(list)
for size in range(size):
    save_input += "_" # fills up save_input with "_"

print(f"I am thinking of a {size + 1} letter word...")

while (not game_end) and (user_lives > 0):
    user_input = input("Enter a letter... ").lower()
    for position in range(size + 1):
        letter = list[position] # letter is assigned the letter in the specific index
        if letter == user_input:
            save_input[position] = letter # index at [position] is assigned value of letter
            print(f"{' '.join(save_input)}") # string transformation
    if user_input not in list:
        print(f"{user_input} is not in the word! lose a life")
        user_lives -= 1
        print(hangman_art.stages[user_lives])
    if "_" not in save_input:
        game_end = True

if user_lives <= 0:
    print("You lost!")
    print(f"{list} is the word")
elif user_lives > 0:
    print("You win!")
