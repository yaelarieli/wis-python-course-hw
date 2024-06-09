import tkinter as tk
from tkinter import messagebox, ttk
from func_for_hw8 import start_game, check_guess, show_number, create_gui

# This is a GUI for the number guessing game

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Number Guessing Game")
    
    
    create_gui(root)
    start_game()
    
    root.mainloop()
