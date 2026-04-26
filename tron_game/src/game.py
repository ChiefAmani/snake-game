import pygame
from player import Player
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("2D Tron Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74) # Default font for now
        self.small_font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.player1 = Player(PLAYER1_START_POS[0], PLAYER1_START_POS[1], PLAYER1_COLOR, PLAYER1_UP, PLAYER1_DOWN, PLAYER1_LEFT, PLAYER1_RIGHT)
        self.player2 = Player(PLAYER2_START_POS[0], PLAYER2_START_POS[1], PLAYER2_COLOR, PLAYER2_UP, PLAYER2_DOWN, PLAYER2_LEFT, PLAYER2_RIGHT)
        self.game_state = START_SCREEN
        self.score1 = 0
        self.score2 = 0
        self.winner = None

    def handle_input(self, event):
        if self.game_state == START_SCREEN:
            if event.type == pygame.KEYDOWN:
                self.game_state = PLAYING
        elif self.game_state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key in self.player1.keys:
                    self.player1.change_direction(self.player1.keys[event.key])
                if event.key in self.player2.keys:
                    self.player2.change_direction(self.player2.keys[event.key])
        elif self.game_state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_round()
                    self.game_state = PLAYING
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

    def update(self):
        if self.game_state == PLAYING:
            self.player1.move()
            self.player2.move()

            # Check collisions for Player 1
            if self.player1.check_collision_with_walls() or \
               self.player1.check_collision_with_trail(self.player2.trail) or \
               self.player1.check_collision_with_trail(self.player1.trail):
                self.player1.alive = False

            # Check collisions for Player 2
            if self.player2.check_collision_with_walls() or \
               self.player2.check_collision_with_trail(self.player1.trail) or \
               self.player2.check_collision_with_trail(self.player2.trail):
                self.player2.alive = False

            if not self.player1.alive:
                self.score2 += 1
                self.winner = "Player 2"
                self.game_state = GAME_OVER
            elif not self.player2.alive:
                self.score1 += 1
                self.winner = "Player 1"
                self.game_state = GAME_OVER

            if self.score1 >= WINNING_SCORE or self.score2 >= WINNING_SCORE:
                self.game_state = GAME_OVER # This will be the final game over, not just round over
                if self.score1 >= WINNING_SCORE:
                    self.winner = "Player 1 Wins the Game!"
                else:
                    self.winner = "Player 2 Wins the Game!"

    def reset_round(self):
        self.player1 = Player(PLAYER1_START_POS[0], PLAYER1_START_POS[1], PLAYER1_COLOR, PLAYER1_UP, PLAYER1_DOWN, PLAYER1_LEFT, PLAYER1_RIGHT)
        self.player2 = Player(PLAYER2_START_POS[0], PLAYER2_START_POS[1], PLAYER2_COLOR, PLAYER2_UP, PLAYER2_DOWN, PLAYER2_LEFT, PLAYER2_RIGHT)
        self.winner = None

    def draw(self):
        self.screen.fill(BLACK)

        if self.game_state == START_SCREEN:
            self.draw_start_screen()
        elif self.game_state == PLAYING:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.draw_scores()
        elif self.game_state == GAME_OVER:
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.draw_game_over_screen()

        pygame.display.flip()

    def draw_start_screen(self):
        title_text = self.font.render("TRON 2D", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(title_text, title_rect)

        instruction_text = self.small_font.render("Press any key to start", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(instruction_text, instruction_rect)

    def draw_game_over_screen(self):
        if self.winner:
            winner_text = self.font.render(f"{self.winner}", True, YELLOW)
            winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            self.screen.blit(winner_text, winner_rect)

        restart_text = self.small_font.render("Press R to restart round or Q to quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

        self.draw_scores()

    def draw_scores(self):
        score_text = self.small_font.render(f"P1: {self.score1}   P2: {self.score2}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
