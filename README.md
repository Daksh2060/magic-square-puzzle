# Magic Square Puzzle
This is Magic Square, a Python puzzle game challenging your strategic thinking. Choose a grid, manipulate it to make each row and column sum to 0. There are multiple starting grids, with a limited number of turns per board. You can change only one spot per turn. The program will generate 2 images each game to record your progress. Good luck!

## Features

- **Board Selection:** Choose from four different game boards, each a grid with its own set of initial numbers, dimensions, and maximum number of turns to solve.

- **Scoring System:** Game keeps track of how many games you have won and the total number of turns it took you to to get this score.

- **Custom Images:** Two images are generated and saved based on the game board for each playthrough, allowing you to keep a catalogue of past rounds.

## Requirements

- Python 3.x

- Modules: `numpy` and `pygame`

## Setup

Follow these steps to set up and run the Magic Square Puzzle game in python:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/magic-square-puzzle-python.git
   ```

2. Install `numpy` and `pygame` if not already installed:

    - **numpy:** [Install numpy with pip](https://numpy.org/install/)

    - **pygame:** [Install pygame with pip](https://www.pygame.org/wiki/GettingStarted)

    - **pip:** [Install pip (usually included with python)](https://pip.pypa.io/en/stable/installation/)

3. Run `magicSquare.py` to start the game.

## How to play

1. **Choose a game goard:** Select a game board by entering a number from 1 to 4.

2. **Pick a spot on the board:** Choose value to change by inputing row and column.

3. **Change value:** Choose a value between -9 and 9 to change value.

3. **Win condition:** Achieve a win by making the sum of each row and column equal to zero within the turn limit.

4. **Scoring:** Earn points for boards won.

5. **Past game catalogue:** The final board of each game is saved as a generated image, using colored squares to represent game baord states.

6. **Play Again:** You can quickly start a new game if you choose to play again.

7. **Exit game:** You can exit Magic Square Puzzle between games or during a round.

## Contact

Feel free to reach out if you have any questions, suggestions, or feedback:

- **Email:** dpa45@sfu.ca
- **LinkedIn:** [@Daksh Patel](https://www.linkedin.com/in/daksh-patel-956622290/)
