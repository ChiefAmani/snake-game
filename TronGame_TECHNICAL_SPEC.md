# TECHNICAL_SPEC.md

## Project Overview
This project aims to develop a 2D Tron-style game where two players control light cycles, leaving persistent trails. The objective is to force opponents to collide with trails or walls, leading to their elimination. The game will be built using Python and the Pygame library.

## Tech Stack
- Python==3.9.13 (or latest stable 3.9.x)
- Pygame==2.5.2

## Development Environment Setup
For Windows users encountering build errors during Pygame installation (e.g., `FileNotFoundError: [WinError 2] The system cannot find the file specified` related to `pacman`), it is recommended to install a pre-built wheel of Pygame.

1.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

2.  **Install Pygame (Windows Specific):**
    If `pip install pygame==2.5.2` fails due to compilation issues, download the appropriate pre-built wheel (`.whl` file) for your Python version and Windows architecture from a reliable source (e.g., unofficial Windows binaries often found on sites like `https://www.lfd.uci.edu/~gohlke/pythonlibs/` or similar community-maintained repositories).
    Then install it using pip:
    ```bash
    pip install path/to/pygame-2.5.2-cpXX-cpXX-win_amd64.whl
    ```
    (Replace `cpXX-cpXX` with your Python version, e.g., `cp39-cp39` for Python 3.9, and `win_amd64` with your architecture if different).

3.  **Install Other Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` only contains `pygame==2.5.2` or other non-Pygame dependencies if Pygame was installed via wheel).

## File Tree
tron_game/
- src/
  - main.py
  - game.py
  - player.py
  - trail.py
  - constants.py
- assets/
  - fonts/
    - tron_font.ttf
  - sounds/
    - collision.wav
- tests/
  - test_game.py
- .gitignore
- README.md
- requirements.txt

## Game Mechanics
- Players: Two players, each controlling a light cycle.
- Movement: Players control their light cycle's direction (up, down, left, right). Continuous forward movement.
- Trails: Each light cycle leaves a persistent, colored trail behind it.
- Collision:
    - Collision with any trail (player's own or opponent's) results in elimination.
    - Collision with game boundaries (walls) results in elimination.
- Game Over: When a player is eliminated, the other player wins the round.
- Scoring: Each round win awards a point to the winning player.
- Game States:
    - START_SCREEN: Displays game title, instructions, and "Press any key to start".
    - PLAYING: Active gameplay.
    - GAME_OVER: Displays winner and "Press R to restart" or "Press Q to quit".

## Core Features
- Two-player local multiplayer.
- Real-time light cycle movement and trail generation.
- Collision detection for trails and boundaries.
- Score tracking and display.
- Game state management (start, playing, game over).
- Basic sound effects for collisions.
- Simple UI for start and game over screens.

## API Endpoints
N/A (Standalone desktop game)

## Environment Variables
N/A (Standalone desktop game)

## Dependencies
pygame==2.5.2

## README.md Content Specification
The `README.md` file located in the `tron_game/` directory must include the following sections to ensure the game is properly documented for a GitHub repository:

### 1. Project Title and Description
- Clear and concise title: "2D Tron Game"
- Brief description of the game and its objective.

### 2. Features
- A bulleted list of core game features (e.g., two-player local multiplayer, real-time movement, collision detection, score tracking).

### 3. How to Run the Game
#### Installation
- Instructions on how to clone the repository.
- Steps to set up a Python virtual environment (recommended).
- Command to install dependencies from `requirements.txt`.
- **Crucially, for Windows users, add a note about potential Pygame build issues and recommend installing a pre-built wheel if `pip install pygame` fails.**

#### Execution
- Command to run the `main.py` file.

### 4. Controls
- A clear mapping of keys for each player's movement (e.g., Player 1: WASD, Player 2: Arrow Keys).

### 5. Future Enhancements (Optional)
- A section outlining potential future additions or improvements to the game.

### 6. License
- Information about the project's license (e.g., MIT License).
