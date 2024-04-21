# HW 2 - a Python program that is a number guessing game

import random

computer_think = random.randrange(1,21)
user_guress=input("The computer think about a whole number betwee 1 and 20, guess what number: ")
number_of_guess=0

while True:
    if int(user_guress)==int(computer_think):
        print("You are correct!")
        number_of_guess=number_of_guess+1
        break
    elif int(user_guress) > int(computer_think):
        number_of_guess=number_of_guess+1
        print("Your number is bigger then the computer number, guess again:")
        user_guress=input()
    elif int(user_guress) < int(computer_think):
        number_of_guess=number_of_guess+1
        print("Your number is smaller then the computer number, guess again:")
        user_guress=input()
print(f"You had {number_of_guess} guesses")