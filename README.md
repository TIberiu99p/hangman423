# Hangman

## Table of Contents
- [Project Description](#project-description)
- [Milestones](#milestones)
- [Latest Updates](#latest-updates)
- [Gameplay Demonstration](#gameplay-demonstration)
- [Last Updates to Hangman Game](#latest-updates)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Description
The **Hangman** game is a Python-based interactive implementation of the classic word guessing game. In this version, the computer selects a word, and the user attempts to guess it by suggesting letters within a limited number of tries. This project showcases skills in Python programming, including functions, loops, conditional statements, and input validation. Key learnings include efficient code organization, handling user input, and implementing game logic.

## Milestones
- **Milestone 1**: Initial Setup
- **Milestone 2**: Word Selection
- **Milestone 3**: Game Logic
- **Milestone 4**: User Interface
- **Milestone 5**: Difficulty Levels and Hints

## Latest Updates 

### Enhanced Guessing Logic (Milestone 4)
The Hangman game has seen significant improvements in its guessing logic, making the gameplay more intuitive and challenging:

1. **Guess Validation:**
   - The game now checks each user input to ensure it's a single alphabetical character. Non-compliant inputs prompt the user to try again, ensuring that guesses are valid before processing.

2. **Repeated Guess Handling:**
   - Attempts to re-guess letters are detected and flagged, preventing the waste of a guess on a letter that's already been tried.

3. **Dynamic Guess Feedback:**
   - Correct guesses: When a player guesses a letter correctly, the game reveals its position(s) in the word, replacing the corresponding underscores in `word_guessed` with the guessed letter.
   - Incorrect guesses: Each incorrect guess results in a reduction of the player's lives. The game notifies the player of the incorrect guess and displays the remaining number of lives.

### Game Progress Tracking
The game now meticulously tracks and updates several key elements to enhance the gaming experience:

- **Number of Unique Letters Left:** The game keeps track of the number of unique letters in the word that have not been guessed yet, providing players with a measure of their progress.
- **Lives Count:** Reflecting the classic Hangman element, the game now has a 'lives' system, where incorrect guesses decrement the player's available lives, adding a layer of challenge to the game.

### Recent changes after milestone 4
- Fixed the check_guess method to correctly handle guesses and update num_letters.
- Added a game completion check in ask_for_input.
- Ensured all instance variables are accessed with self.
- Improved user feedback messages.
- Optimized the loop in check_guess.


### Hangman Game - Milestone 5 Documentation

#### Overview
In Milestone 5 of the Hangman game project, we focused on refining the game logic, enhancing user interaction, and encapsulating the game flow within a standalone function. This milestone ensures a more robust, user-friendly, and maintainable codebase.

#### Key Features and Changes

1. **Hangman Class Refinement**
- Random Word Selection: The `Hangman` class randomly selects a word from a provided list, starting a new game instance with this word.
- Guess Checking: Enhanced the `check_guess` method to accurately update the game state (guessed letters and remaining lives) based on user input.
- Improved User Feedback: Included informative messages for successful guesses, incorrect guesses, and repeat attempts.

2. **Game Flow Management**
- `play_game` Function:Introduced a new function to manage the overall game flow. This function initializes the game, keeps track of lives, and checks for win/lose conditions.

3. **Game Loop**
- Win/Lose Conditions: The game loop in `play_game` continuously prompts the user for input until the player either guesses the word correctly (wins) or runs out of lives (loses).
- User Input Validation: The game now checks for valid input (single alphabetical characters) and handles invalid or repeated guesses gracefully.

4. **User Experience**
- Enhanced Interaction: The game provides real-time feedback about correct guesses, incorrect guesses, and the remaining number of lives.
- Endgame Messages: Custom messages are displayed to the user upon winning or losing the game.



#### Example Invocation:
```python
word_list = ['python', 'hangman', 'programming']
play_game(word_list)
```

### Menu implementation
Key Features:

- Interactive Menu System: A new menu-driven user interface implemented in menu.py allows users to start the game, view rules, or exit the application seamlessly.
- Modular Design: The game logic is encapsulated in hangman.py, ensuring clean separation of game mechanics from the user interface.
- Enhanced User Experience: Improved game flow with clear instructions, input validation, and end-game scenarios, offering an engaging user experience.


### Difficulty Levels
- **Implemented Difficulty Levels**: The game now includes three difficulty levels: easy, medium, and hard. 
- **Dynamic Word Selection**: Words are chosen based on the selected difficulty. Each difficulty level has a different set of words and a varying number of lives.
- **JSON File Integration**: Words and their difficulty levels are stored in a JSON file, allowing for easy updates and expansion of the word list.

#### Hint System
- **Hint Functionality**: Players can now request hints to help them guess the word.
- **Integration with JSON**: Hints for each word are stored alongside the words in the JSON file, allowing for easy management and updates.

### Technical Enhancements

#### Modular Design
- The game has been split into multiple Python files for better code organization and readability:
    - `menu.py`: Handles the game's main menu and user interactions.
    - `milestone_5.py`: Contains the core game logic and the `Hangman` class.
    - `difficulty.py`: Manages the game's difficulty levels and word selection.
    - `hint.py`: Provides the hint functionality linked with the words.
    - `drawHang.py`: Draw the hangman

#### JSON Data Structure
- The `words.json` file has been structured to store words along with their respective difficulty levels and hints, facilitating easy data management.

### Hangman Drawing Feature
- **New Feature**: The game now includes a dynamic hangman drawing feature. As the player makes incorrect guesses, the hangman drawing progresses, visually representing the player's remaining lives.
- **Difficulty Integration**: The progression of the hangman drawing is tailored to the chosen difficulty level, with more lives in easier levels resulting in a slower drawing progression.

## Gameplay Demonstration
Watch a playthrough of our Hangman game on YouTube: [Hangman Game Playthrough](https://www.youtube.com/watch?v=QTLFDCAK0cE)


### Running the Game
To run the game, navigate to the directory containing the files and execute the following command in your terminal:
```python
python menu.py
```
## Updates to Hangman Game

### Last Modifications in HangmanDrawing Class
- Updated the `draw` method to accept `word_guessed` as an additional parameter.
- The method now displays the current state of the word (guessed letters and underscores) under the hangman drawing.

```python
class HangmanDrawing:
    # ... existing methods and attributes ...

    def draw(self, stage, word_guessed):
        # Display the current stage of the hangman
        print(self.stages[stage])
        # Display the current state of word guessed
        print("Word: " + " ".join(word_guessed))
```

### Modifications in Hangman Class
#### Updated `check_guess` Method
- Modified to display only the current state of the word when a correct guess is made.
- Modified to display only the hangman drawing when an incorrect guess is made.

```python
def check_guess(self, guess):
    if guess in self.word:
        print(f"{guess} is in the word.")
        for index, letter in enumerate(self.word):
            if letter == guess and self.word_guessed[index] == '_':
                self.word_guessed[index] = guess

        # Display only the current state of the word when the guess is correct
        print("Word: " + " ".join(self.word_guessed))

    else:
        self.num_lives -= 1
        print(f"{guess} is not in the word. Try again.")
        print(f"You have {self.num_lives} lives left.")

        # Calculate the current drawing stage and display only the hangman
        drawing_stage = len(self.hangman_drawing.stages) - self.num_lives - 1
        self.hangman_drawing.draw(drawing_stage, self.word_guessed)

    if guess not in self.list_of_guesses:
        self.list_of_guesses.append(guess)
```

These changes enhance the player experience by providing clear feedback on their guesses and the current state of the game.


## Installation
Ensure Python is installed on your system. Download and install Python from [python.org](https://www.python.org/downloads/).

Clone the repository:
```
git clone https://github.com/TIberiu99p/hangman423.git
```

## Usage
Open a command line, navigate to the script's directory, and run:
```
python milestone2.py
python milestone3.py
python hangman_Template.py
```
Follow the on-screen prompts to guess letters in the selected word.

## File Structure
- `hangman`: Folder that contains 3 files
- `hangman_Template.py`: template for the full hangman
- `milestone_2.py`: milestone 2 and all of its task
- `milestone_3.py`: milestone 3 and all of its task
- `milestone_4.py`: milestone 4 and all of its task
- `milestone_5.py`: milestone 3 and all of its task
- `menu.py`: starts the game with a menu
- `hint.py`: gives hints 
- `difficulty.py`: allows change of difficulty
- `words.json`: database for words and hints
- `README.md`: Documentation of the project.
- `hangDraw.py`: draws the hangman

## License
This project is licensed under [appropriate license]. See the `LICENSE` file for more details.