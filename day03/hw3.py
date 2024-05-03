# HW 3 - a Python program that is a number guessing game

import random


def the_guess_of_user():
    user_guess = input(
        "The computer think about a whole number betwee 1 and 20, guess what number: "
    )
    return user_guess


def correct_or_not(user_guess, computer_think):
    number_of_guess = 0
    while True:
        if user_guess == "x":
            print("Exiting the game. Goodbye!")
            return user_guess
        elif user_guess == "n":
            print("Leaving current game.")
            break
        elif user_guess == "s":
            print(f"The hidden number is: {computer_think}")
            break
        elif user_guess.isnumeric():
            user_guess = int(user_guess)
        number_of_guess += 1
        if user_guess == computer_think:
            print("You are correct!")
            break
        elif user_guess > computer_think:
            print("Your number is bigger then the computer number, guess again:")
        elif user_guess < computer_think:
            print("Your number is smaller then the computer number, guess again:")

        user_guess = input()
    if user_guess != "n" and user_guess != "x":
        print(f"You had {number_of_guess} guesses")


def guessing_game():
    computer_think = random.randrange(1, 21)
    user_guess = the_guess_of_user()
    user_guess = correct_or_not(user_guess, computer_think)
    return user_guess


def main():

    user_guess = guessing_game()
    while True:
        if user_guess == "x":
            break
        else:
            another_game = input("Do you want to plat another game ? [y/n]")
            if another_game == "y":
                user_guess = guessing_game()
            else:
                print("It was fun to play ! ")
                break


main()
