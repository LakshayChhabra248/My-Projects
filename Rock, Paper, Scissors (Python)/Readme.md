# ✊ Rock, Paper, Scissors Game (Python) 🪨📄✂️

## A Classic Game with a Matrix Twist 🔄

This document outlines the Python code for a Rock, Paper, Scissors game, implementing a unique 2D array or matrix method to declare the winner. The game pits you against the computer in a battle of chance and strategy, using a different approach to decision-making than the traditional if/else approach.

**Functionality:**

*   🎮 **User vs. Computer:** A classic Rock, Paper, Scissors game where you play against the computer.
*   🤖 **Random Computer Choice:** The computer randomly selects its move (rock, paper, or scissors).
*   ⌨️ **User Input:** You input your move through the console using 'r' for rock, 'p' for paper, or 's' for scissors.
*   🏆 **Matrix Winner Declaration:** The winner is determined using a 2D array or matrix lookup, offering a more concise and elegant solution.
*   ⚖️ **Classic Game Logic:** Follows the standard rules of Rock, Paper, Scissors.

## ⚙️ Code Breakdown:

1.  **Computer Choice:**

    *   Uses the `random.choice` method to select a random choice of rock, paper or scissors for the computer.
    *  The choices are represented by characters: `r` for rock, `p` for paper, and `s` for scissors.

2.  **User Input:**
    *   Prompts the user to input their choice for rock, paper, or scissors ('r', 'p', or 's').
    *   Converts the user input to lowercase and validates it.

3. **2D Array (Matrix) Logic**
    * A 2D array is used to define the win/loss logic.
        * The rows represent the user's choice
        * The column represents the computer's choice
    * The values inside this 2D array represent the result
        * `0` for a draw
        * `1` if user wins
        * `-1` if computer wins

4.  **Determining the Winner:**

    *   The program uses the matrix to look up the user and the computer choice.
    *   The value from this matrix index is used to declare the winner
    *   If the value is `0` the game is a draw
    *   If the value is `1` user wins
    *    If the value is `-1` computer wins
5.  **Output:**
  * Displays the choices of the computer and the user
  * Declares the winner of the game.

## 🚀 Running the Code:

1.  **Save:** Save the Python code (e.g., as `main.py`).
2.  **Run:** Open your terminal or command prompt and execute the script using:
    ```bash
    python main.py
    ```
3.  **Play:** Follow the prompts to enter your choice (r, p, or s) and see the result.

## ➕ Potential Enhancements:

This code demonstrates a basic Rock, Paper, Scissors game. Here are some ideas to enhance the game further:

*   **Multiple Rounds:** Allow the game to be played for multiple rounds.
*   **Scorekeeping:** Keep track of scores and declare an overall winner.
*  **Input Validation** Add more robust input validation for the user.
*   **User Interface:** Create a graphical user interface for a more interactive experience.

**Contribute:**

Your contributions are welcome! Feel free to submit a pull request with any improvements or new features.

**Created By:** Lakshay Chhabra
