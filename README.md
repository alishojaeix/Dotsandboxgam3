# Dots and Boxes Game

![Game Screenshot](assets/screenshot.png) *(add screenshot later)*

A Python implementation of the classic Dots and Boxes strategy game using Pygame.

## 🎯 Features

- 🕹️ Two-player turn-based gameplay
- 📊 Score tracking
- 🏆 Win detection
- 🎨 Clean graphical interface
- 🔄 Player turn management

## 📋 Table of Contents
- [Game Rules](#-game-rules)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Controls](#-controls)
- [Customization](#-customization)
- [Roadmap](#-roadmap)
- [License](#-license)

## 🧩 Game Rules

1. Players take turns connecting adjacent dots with horizontal or vertical lines
2. When a player completes a 1x1 box, they claim it and get another turn
3. The game ends when all lines are drawn
4. The player with the most claimed boxes wins

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alishojaeix/dots-and-boxes.git
   cd dots-and-boxes


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🖱️ How to Play

1. Click between two adjacent dots to draw a line
2. Try to complete boxes to earn points
3. The game automatically tracks turns and scores

## 🛠️ Customization

Modify `main.py` to change game settings:
```python
# Change grid size (5x5 dots = 4x4 boxes)
game = DotsAndBoxesGUI(rows=5, cols=5)
```

Modify `gui.py` to change visual settings:
```python
# Change colors, spacing, etc.
GRID_SPACING = 60  # Distance between dots
PLAYER_COLORS = {
    1: (255, 0, 0),  # Player 1 color (Red)
    2: (0, 0, 255)   # Player 2 color (Blue)
}
```

## 🚧 Roadmap

- [ ] Add AI opponent
- [ ] Implement different grid sizes
- [ ] Add game menu and settings
- [ ] Include sound effects
- [ ] Add online multiplayer

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

## How to Run

1. Create the files as shown above
2. Install requirements: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## Game Assets

For images/sounds, check these free asset sites:
- [OpenGameArt.org](https://opengameart.org/)
- [Kenney.nl](https://kenney.nl/)
- [Itch.io Game Assets](https://itch.io/game-assets)

   
