# TECHNICAL_SPEC.md

## Project Overview
This project aims to develop a 2D Tron-style game where two players control light cycles, leaving persistent trails. The objective is to force opponents to collide with trails or walls, leading to their elimination. The game will be built using Python and the Pygame library.

## Tech Stack
- Python==3.9.13 (or latest stable 3.9.x)
- Pygame==2.5.2

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
