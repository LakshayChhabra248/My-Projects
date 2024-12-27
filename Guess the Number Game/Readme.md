# 🧠 Guess The Number Game (Java)

## A Fun and Competitive Number Guessing Game 🏆

This repository contains the code for a simple yet engaging number guessing game built in Java. Players try to guess a randomly generated number between 1 and 100 with the fewest tries possible. The game supports multiple players, allowing for a competitive and interactive experience.

**Key Features:**

*   🎲 **Random Number Generation:** The game generates a random number between 1 and 100 at the start of each game.
*   👥 **Multiplayer Support:** Allows multiple players to participate and compete against each other.
*   🔢 **Guess Tracking:** Keeps track of the number of guesses each player takes to guess the number.
*   🥇 **Winner Determination:** Determines the winner as the player who guessed the number with the lowest number of attempts.
*   💬 **User-Friendly Prompts:** Provides clear prompts and messages throughout the game to guide the user.

## 💻 Code Structure:

### 🎮 `Game` Class:
This class contains the core game logic:
    *  `genRandNum()`: Generates a random number between 1 and 100
    *  `takeUserInput()`: Takes user input for a player's guess
    *  `isCorrectNumber()`: Manages the core game loop for multiple players, including getting names, playing individual rounds, storing scores, and finding the winner.
    *  `getResult()`: Returns the number of guesses taken by each player.

### 🎬 `Main` Class:
This class is responsible for starting the game. It creates an instance of the `Game` class and calls the `isCorrectNumber()` method to begin the game.

## 🕹️ How to Play:

1.  **Clone the Repository:** Clone or download the repository files to your local machine.
2.  **Import into IDE:** Open the project in your favorite Java IDE (e.g., Eclipse, IntelliJ IDEA, VS Code).
3.  **Run `Main` Class:** Run the `Main` class to start the game.
4.  **Enter Number of Players:** When prompted, enter the number of players you want to participate.
5.  **Enter Name and Guess:** Each player will be prompted to enter their name and then guess a number between 1 and 100.
6.  **Game Results:** The game will announce the winner with the lowest number of guesses.

## ⚙️ Requirements:

*   Java Development Kit (JDK) installed on your system.

## 🚀 Further Enhancements (Ideas):

*   **Difficulty Levels:** Implement different difficulty levels with varying number ranges.
*   **Timer:** Add a timer to limit the guess time for each player, adding an extra layer of challenge.
*   **Visual Feedback:** Improve visual feedback for higher/lower guesses (e.g., provide a hint like "Try a bit higher" or "Try a bit lower").

**Contribute:**

Feel free to contribute to this project! You are welcome to modify and enhance the code further, submit pull requests, or raise issues with suggestions.

**Created By:** Lakshay Chhabra
