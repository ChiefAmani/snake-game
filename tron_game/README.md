# 2D Tron Game

This project aims to develop a 2D Tron-style game where two players control light cycles, leaving persistent trails. The objective is to force opponents to collide with trails or walls, leading to their elimination.

## Features
- Two-player local multiplayer.
- Real-time light cycle movement and trail generation.
- Collision detection for trails and boundaries.
- Score tracking and display.
- Game state management (start, playing, game over).
- Basic sound effects for collisions (placeholder).
- Simple UI for start and game over screens.

## How to Run the Game

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ChiefAmani/snake-game.git
   cd snake-game/tron_game
   ```
2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Execution
Run the game using the following command from the `tron_game/src` directory:
```bash
python main.py
```

## Controls
- **Player 1:**
  - **W**: Move Up
  - **S**: Move Down
  - **A**: Move Left
  - **D**: Move Right
- **Player 2:**
  - **Up Arrow**: Move Up
  - **Down Arrow**: Move Down
  - **Left Arrow**: Move Left
  - **Right Arrow**: Move Right

## Future Enhancements (Optional)
- Implement more sophisticated AI for single-player mode.
- Add different game modes or power-ups.
- Improve graphics and sound effects.
- Network multiplayer.

## License
This project is licensed under the MIT License.
