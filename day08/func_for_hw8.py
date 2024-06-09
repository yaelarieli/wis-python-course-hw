import random
import tkinter as tk
from tkinter import messagebox, ttk

def start_game():
    global computer_think, guess_counter
    computer_think = random.randrange(1, 21)
    guess_counter = 0
    result_label.config(text="")
    guess_nuber.set("")  # Clear previous selection

def check_guess():
    global guess_counter
    try:
        guess = int(guess_nuber.get())
        if guess:
            guess_counter += 1

            if guess < computer_think:
                result_label.config(text="Your number is smaller then the computer number! Try again.")
            elif guess > computer_think:
                result_label.config(text="Your number is bigger then the computer number! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {guess_counter} attempts.")
                result_label.config(text="You guessed it! If you want to play again, press Restart")
        else:
            messagebox.showerror("Invalid input", "Please select a number.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please select a valid number.")

def show_number():
    messagebox.showinfo("Hidden Number", f"The hidden number is {computer_think}")

def create_gui(root):
    global guess_nuber, result_label
    
    label = tk.Label(root, text="Select a number between 1 and 20:")
    label.pack(pady=10)
    
    guess_nuber = ttk.Combobox(root, values=list(range(1, 21)))
    guess_nuber.pack(pady=10)
    guess_nuber.set("")  # Set default to empty
    
    guess_button = tk.Button(root, text="Guess", command=check_guess)
    guess_button.pack(pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)
    
    restart_button = tk.Button(root, text="Restart", command=start_game)
    restart_button.pack(side=tk.LEFT, padx=20)
    
    show_number_button = tk.Button(root, text="Show Number", command=show_number)
    show_number_button.pack(side=tk.LEFT, padx=20)
    
    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(side=tk.LEFT, padx=20)