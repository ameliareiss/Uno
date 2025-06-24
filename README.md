# UNO

A Python implementation of the classic card game UNO with a custom GUI built using Pygame. In this version of UNO, you play against a single AI opponent, trying to be the first to get rid of all your cards. The server manages the game state and provides real-time feedback through an interactive GUI.

## Files

*   `uno.py`: Main game loop.
*   `game.py`: Game logic, state management, and turn handling.
*   `card.py`: Card class with display logic and validation.
*   `deck.py`: Deck creation and card management.
*   `player.py`: Player class for hand management and turn actions.
*   `gui.py`: Graphical user interface and user interaction.
*   `design.py`: UI layout constants and design specifications.

## Building the Project

Open your terminal and navigate to the directory where you saved the project files. Then, install the required dependency.

For example:
```bash
cd /path/to/your/project/files
pip install pygame
```

This will install Pygame, which is required to run the game.

## How to Run

Open your terminal and navigate to the project directory. Then run the following command:

```bash
python uno.py
```

The game will start automatically with 7 cards dealt to each player. The top card of the deck becomes the first card in the discard pile.

## How to Play

**Game Controls:**
*   Click on a card in your hand to play it (if valid)
*   Click the "Draw" button to draw a card from the deck
*   Click the "End Turn" button to end your turn
*   Use the left/right arrows to navigate through your hand (when you have more than 7 cards)
*   Click your desired color quadrant to choose a color when playing wild cards

**Game Rules:**
*   Play a card that matches the top card's color or value
*   Wild cards can be played on any card, and a new color is chosen immediately
*   Action cards execute their special effects (reverse, skip, +2, +4)
*   Draw once OR play one card per turn
*   First player to get rid of all cards wins

**Note:**
*   In this two-player version, reverse cards act as skip cards, granting another turn
*   +2 and +4 cards are NOT stackable by the opponent
*   If you draw a card on your turn and it is playable, you may play it immediately

**AI Opponent:**
The dummy AI plays any valid card in its hand, or draws if no valid cards are available. 
