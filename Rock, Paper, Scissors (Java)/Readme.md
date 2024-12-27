# ✊ Rock, Paper, Scissors Game (Java) 🪨📄✂️

## A Classic Game of Chance and Strategy 🕹️

This document describes the Java code for a classic Rock, Paper, Scissors game implemented in the `Main.java` file. The game simulates a match between you and the computer, where you both choose either rock, paper, or scissors, and the winner is determined based on the game's classic rules.

**Functionality:**

*   🤝 **User vs. Computer:** Play a round of Rock, Paper, Scissors against the computer.
*   🎲 **Random Computer Choice:** The computer randomly selects its move (rock, paper, or scissors).
*   ⌨️ **User Input:** You enter your move through the console by typing 'r' for rock, 'p' for paper, or 's' for scissors.
*   🏆 **Winner Declaration:** The program compares your choice against the computer's, and declares the winner or a tie.
*   💯 **Classic Game Logic:** Follows the standard Rock, Paper, Scissors game rules.

## ⚙️ Code Breakdown:

1.  **Computer Choice:**

    *   A string `compOption` containing "rps" is created, representing rock, paper, and scissors.
    *   A `Random` object is used to generate a random index within the bounds of `compOption`.
    *   The character at the generated index is extracted using `charAt()`.
    *   A `switch` statement then converts the character to a human-readable choice (`rock`, `paper`, or `scissors`) which is stored in `compChoose`.

2.  **User Input:**

    *   A `Scanner` object reads user input from the console.
    *   The user is prompted to enter 'r' for rock, 'p' for paper, or 's' for scissors.
    *   The program reads user input using `next()`.
    *   The input is converted to lowercase, ensuring that the program is case-insensitive.
    *   The program checks for invalid input (length greater than 1) and prints an error message if necessary.
    *   The first character of the user input is extracted, and a `switch` statement is used to store it as a human-readable choice (`rock`, `paper`, or `scissors`) in `youChoose`.

3.  **Displaying Choices:**

    *   The user's and computer's choices are displayed using `printf()` for formatted output.

4.  **Determining the Winner:**

    *   An `if` statement checks if both choices are the same, resulting in a tie.
    *   An `else if` statement with nested conditions checks for all other cases to determine the winner based on the rules of Rock-Paper-Scissors.
    *   The program then announces the results - "The Game is tie", "You Win the game", or "You Lose the Game".

5.  **Closing Scanner:**

    *   The `Scanner` object is closed to release resources.

## 🚀 Running the Code:

1.  **Save:** Save the Java code as `Main.java`.
2.  **Compile:** Compile the code using a Java compiler:
    ```bash
    javac Main.java
    ```
3.  **Run:** Run the compiled class using Java runtime:
    ```bash
    java Main
    ```
4.  **Play:** Follow the prompts to enter your choice (r, p, or s), and see the result.

## ➕ Future Improvements:

This code provides a basic Rock, Paper, Scissors game. Here are some ideas to extend it further:

*   **Multiple Rounds:** Add support for playing multiple rounds.
*   **Scorekeeping:** Keep track of the score and display the results at the end of multiple rounds.
*   **Graphical Interface:** Create a graphical user interface for a more interactive gaming experience.

**Contribute:**

Feel free to contribute to this project! You can modify the code to make it better, suggest new features or report issues, all using the proper pull request procedure.

**Created By:** Lakshay Chhabra
