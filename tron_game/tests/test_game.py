import pytest
import pygame
from tron_game.src.player import Player
from tron_game.src.constants import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER1_COLOR, PLAYER1_UP, PLAYER1_DOWN, PLAYER1_LEFT, PLAYER1_RIGHT

# Initialize Pygame for font rendering in tests
pygame.init()

@pytest.fixture
def player():
    return Player(100, 100, PLAYER1_COLOR, PLAYER1_UP, PLAYER1_DOWN, PLAYER1_LEFT, PLAYER1_RIGHT)

def test_player_initial_direction(player):
    assert player.direction == 'RIGHT'

def test_player_change_direction(player):
    player.change_direction('UP')
    assert player.direction == 'UP'
    player.change_direction('LEFT')
    assert player.direction == 'LEFT'

def test_player_invalid_direction_change(player):
    player.change_direction('UP')
    player.change_direction('DOWN') # Should not change to opposite direction
    assert player.direction == 'UP'

def test_player_move(player):
    initial_x, initial_y = player.x, player.y
    player.move()
    assert player.x == initial_x + GRID_SIZE
    assert player.y == initial_y
    assert (initial_x, initial_y) in player.trail

def test_player_collision_with_walls(player):
    # Move player out of bounds to the right
    player.x = SCREEN_WIDTH + GRID_SIZE
    assert player.check_collision_with_walls() is True

    # Move player out of bounds to the top
    player.x = 100 # Reset x
    player.y = -GRID_SIZE
    assert player.check_collision_with_walls() is True

    # Player within bounds
    player.x = 100
    player.y = 100
    assert player.check_collision_with_walls() is False

def test_player_collision_with_own_trail(player):
    player.move() # (100,100) in trail
    player.change_direction('UP')
    player.move() # (120,100) in trail
    player.change_direction('LEFT')
    player.move() # (120,80) in trail
    player.change_direction('DOWN')
    player.move() # (100,80) in trail
    player.change_direction('RIGHT')
    player.move() # (100,100) current head, should collide with first trail segment
    assert player.check_collision_with_trail(player.trail) is True

def test_player_collision_with_other_trail(player):
    other_player = Player(200, 200, PLAYER1_COLOR, PLAYER1_UP, PLAYER1_DOWN, PLAYER1_LEFT, PLAYER1_RIGHT)
    other_player.move()
    other_player.move()
    # Player 1 moves into Player 2's trail
    player.x = other_player.trail[0][0]
    player.y = other_player.trail[0][1]
    assert player.check_collision_with_trail(other_player.trail) is True

# Clean up pygame after tests
pygame.quit()
