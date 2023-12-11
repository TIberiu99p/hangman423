# Hangman

## Table of Contents
- [Project Description](#project-description)
- [Milestone 1](task1)
- [Milestone 2](task2)
- [Milestone 3](task3)
- [Latest Updates](#latest-updates)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Description
The **Hangman** game is a Python-based interactive implementation of the classic word guessing game. In this version, the computer selects a word, and the user attempts to guess it by suggesting letters within a limited number of tries. This project showcases skills in Python programming, including functions, loops, conditional statements, and input validation. Key learnings include efficient code organization, handling user input, and implementing game logic.

## Milestone 1
Environment set up 

## Milestone 2
Create variables for the game
`milestone_2.py`

## Milestone 3
Check if the guessed character is in the word
`milestone_3.py`

## Milestone 4
Create the Game class
`milestone_4py`

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
- `README.md`: Documentation of the project.

## License
This project is licensed under [appropriate license]. See the `LICENSE` file for more details.