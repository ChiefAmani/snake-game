import pygame
from constants import GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y, color, up_key, down_key, left_key, right_key):
        self.x = x
        self.y = y
        self.color = color
        self.direction = 'RIGHT'
        self.keys = {
            up_key: 'UP',
            down_key: 'DOWN',
            left_key: 'LEFT',
            right_key: 'RIGHT'
        }
        self.trail = []
        self.alive = True

    def change_direction(self, new_direction):
        if self.direction == 'UP' and new_direction == 'DOWN': return
        if self.direction == 'DOWN' and new_direction == 'UP': return
        if self.direction == 'LEFT' and new_direction == 'RIGHT': return
        if self.direction == 'RIGHT' and new_direction == 'LEFT': return
        self.direction = new_direction

    def move(self):
        self.trail.append((self.x, self.y))
        if self.direction == 'UP':
            self.y -= GRID_SIZE
        elif self.direction == 'DOWN':
            self.y += GRID_SIZE
        elif self.direction == 'LEFT':
            self.x -= GRID_SIZE
        elif self.direction == 'RIGHT':
            self.x += GRID_SIZE

    def draw(self, screen):
        for segment in self.trail:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, (self.x, self.y, GRID_SIZE, GRID_SIZE))

    def get_head_rect(self):
        return pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    def check_collision_with_walls(self):
        return not (0 <= self.x < SCREEN_WIDTH and 0 <= self.y < SCREEN_HEIGHT)

    def check_collision_with_trail(self, other_trail):
        return (self.x, self.y) in self.trail[:-1] or (self.x, self.y) in other_trail
