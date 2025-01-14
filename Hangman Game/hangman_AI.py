import tkinter as tk
from tkinter import messagebox
import requests
import random
import google.generativeai as genai

# Replace 'YOUR_API_KEY' with your actual Gemini API key
GOOGLE_API_KEY = "YOUR_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def get_random_word(length=None):
    """Fetches a random word from the Random Word API."""
    url = "https://random-word-api.herokuapp.com/word"
    if length:
        url = f"https://random-word-api.herokuapp.com/word?length={length}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[0].lower()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching word from API: {e}")
        return None

def get_word_meaning(word):
    """Fetches the meaning of a word using Gemini API."""
    try:
         prompt = f"Give a short definition or meaning of a word which has these letters but don't mention the word itself: {word}"
         response = model.generate_content(prompt)
         if response and response.text:
             return response.text
         else:
              return "No meaning found."
    except Exception as e:
        print(f"Error fetching meaning from Gemini: {e}")
        return "Could not fetch meaning"


class HangmanGUI:
    def __init__(self, root):
         self.root = root
         self.root.title("Hangman Game")
         self.root.geometry("600x700")
         self.root.configure(bg="lightblue")  # Initial window size


         # Configure grid weights for responsiveness
         for i in range(25):
             self.root.grid_rowconfigure(i, weight=1, minsize=20)
         for i in range(13):
            self.root.grid_columnconfigure(i, weight=1, minsize=40)

         self.mode = None # default value of mode

         self.difficulty_screen()

    def difficulty_screen(self):
        """Displays the difficulty selection screen."""
        self.diff_win = tk.Toplevel(self.root)
        self.diff_win.title("Select Difficulty")
        self.diff_win.geometry("200x280")

        self.diff_win.transient(self.root)  # to associate the diff win to the root window
        self.diff_win.focus_force()  # to force the window to appear on top

        tk.Label(self.diff_win, text="Choose Word Length:", font=("Arial", 14)).pack(pady=10)

        lengths = [4, 5, 6, 7, "any"]  # any is an option for choosing any length word
        for length in lengths:
            if length == "any":
                tk.Button(self.diff_win, text=str(length), command=lambda l=None: self.start_game(l), font=("Arial", 12)).pack(pady=5)
            else:
                tk.Button(self.diff_win, text=str(length), command=lambda l=length: self.start_game(l), font=("Arial", 12)).pack(pady=5)


    def start_game(self, length):
        """Starts the new game and closes the difficulty selection window"""
        self.mode = length
        self.diff_win.destroy()
        self.new_game(length)


    def new_game(self, length=None):
        """Initializes a new game."""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.word = get_random_word(length)  # passing the length parameter
        if not self.word:
            messagebox.showerror("Error", "Could not retrieve a word. Please try again later.")
            self.root.destroy()
            return

        self.guesses = ''
        self.turns = 12
        self.hint_used = False
        self.meaning = get_word_meaning(self.word)


        # Using grid for all widgets
        self.word_label = tk.Label(self.root, text="", font=("Arial", 24), fg = "black", bg = "lightblue")
        self.word_label.grid(row=0, column=0, columnspan=13, pady=10, sticky='nsew')  # Reduced pady

        self.turns_label = tk.Label(self.root, text=f"Turns left: {self.turns}", font=("Arial", 14), bg = "lightblue")
        self.turns_label.grid(row=1, column=0, columnspan=13, pady=10, sticky='nsew')

        self.message_label = tk.Label(self.root, text="", font=("Arial", 14), height=3, bg = "lightblue")
        self.message_label.grid(row=7, column=0, columnspan=13, sticky='nsew')

        self.hint_button = tk.Button(self.root, text="Meaning Hint", command=self.show_hint, font=("Arial", 14))
        self.hint_button.grid(row=2, column=0, columnspan=6, pady=10, sticky='nsew')


        self.letter_hint_button = tk.Button(self.root, text="Letter Hint", command=self.show_letter_hint, font=("Arial", 14))
        self.letter_hint_button.grid(row=2, column=7, columnspan=6, pady=10, sticky='nsew')

        self.change_mode_button = tk.Button(self.root, text="Change Mode", command=self.difficulty_screen, font=("Arial", 14))
        self.change_mode_button.grid(row=3, column=0, columnspan=13, pady=10, sticky='nsew')

        self.replay_button = tk.Button(self.root, text="Replay", command=lambda: self.new_game(self.mode), font=("Arial", 14))
        self.replay_button.grid(row=4, column=0, columnspan=13, pady=10, sticky='nsew')

        # Create letter buttons grid
        self.letter_buttons = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        row = 5  # Starting row for letter buttons
        col = 0


        for letter in alphabet:
            button = tk.Button(self.root, text=letter, command=lambda l=letter: self.make_guess(l), font=("Arial", 14),
                            width=3)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            self.letter_buttons[letter] = button
          #keyboard binding
            self.root.bind(letter, lambda event, l=letter: self.make_guess(l))
            col += 1
            if col > 12:
                col = 0
                row += 1
          # Enable all letter buttons for the new game
        for button in self.letter_buttons.values():
           button.config(state=tk.NORMAL)

        self.update_display()

    def update_display(self):
        """Updates the displayed word with the current guesses."""
        display = ""
        for char in self.word:
            if char in self.guesses:
               display += char + " "
            else:
                display += f"\u2009_\u2009" # black dash using unicode thin space
        self.word_label.config(text=display)


    def make_guess(self, letter):
        """Handles the user's guess with the letter button."""
        if letter in self.guesses:
           self.message_label.config(text="You have already guessed that character.")
           return

        self.guesses += letter
        if letter not in self.word:
             self.turns -= 1
             self.message_label.config(text="Wrong!")
             self.turns_label.config(text=f"Turns left: {self.turns}")
             if self.turns == 0:
                self.end_game(False)
        else:
             self.message_label.config(text="")
             self.update_display()
             if "_" not in self.word_label.cget("text"):
                self.end_game(True)

        if letter in self.letter_buttons:
           self.letter_buttons[letter].config(state=tk.DISABLED)

    def show_hint(self):
        """Reveals the meaning of the word from Gemini."""
        if self.hint_used:
             self.message_label.config(text="You have already used the meaning hint.")
             return

        self.hint_used = True
        self.hint_button.config(state=tk.DISABLED)
        self.message_label.config(text=f"Meaning: {self.meaning}")

    def show_letter_hint(self):
         """Reveals a single unguessed letter"""
         if not self.word or self.hint_used:
             return
         unguessed_chars = [char for char in self.word if char not in self.guesses]
         if unguessed_chars:
            hint_char = random.choice(unguessed_chars)
            self.guesses += hint_char
            self.update_display()
            self.letter_hint_button.config(state=tk.DISABLED)

    def end_game(self, win):
        """Handles the end of the game (win or lose)."""
        if win:
            message = f"You Win!\nThe word was: {self.word}"
        else:
            message = f"You Lose!\nThe word was: {self.word}"
        messagebox.showinfo("Game Over", message)
        self.new_game(self.mode) # Restart the game after completion with the same mode

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()
