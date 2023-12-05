import pygame
import sys

from config import Color
from button import Button


class GameLostView:
    def __init__(self, width, height, game_state):
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(Color.BACKGROUND)

        message_font = pygame.font.Font(None, 50)
        message_surface = message_font.render('Game Over!', 1, Color.TEXT)
        message_rect = message_surface.get_rect()
        message_rect.centerx = self.rect.w // 2
        message_rect.top = int(self.rect.h * 0.10)

        button_height = int(0.09 * self.rect.h)
        restart_btn = Button('restart', button_height, game_state.restart)

        restart_btn.rect.center = self.rect.w // 2, self.rect.h // 2

        self.image.blit(message_surface, message_rect)
        restart_btn.draw(self.image)

    def draw(self, other_surface: pygame.Surface):
        other_surface.blit(self.image, self.rect)

class GameWonView:
    def __init__(self, width, height, game_state):
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(Color.BACKGROUND)

        message_font = pygame.font.Font(None, 50)
        message_surface = message_font.render('You win!', 1, Color.TEXT)
        message_rect = message_surface.get_rect()
        message_rect.centerx = self.rect.w // 2
        message_rect.top = int(self.rect.h * 0.10)

        button_height = int(0.09 * self.rect.h)
        exit_btn = Button('exit', button_height, game_state.exit)
        exit_btn.rect.center = self.rect.w // 2, self.rect.h // 2

        self.image.blit(message_surface, message_rect)
        exit_btn.draw(self.image)

    def draw(self, other_surface: pygame.Surface):
        other_surface.blit(self.image, self.rect)


class StartMenuView:
    def __init__(self, width, height, game_state):
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(Color.BACKGROUND)

        font = pygame.font.Font(None, 50)
        title_surface = font.render('SUDOKU', 1, Color.TEXT)
        title_rect = title_surface.get_rect()
        title_rect.centerx = self.rect.w // 2
        title_rect.top = int(self.rect.h * 0.10)
        subheading_surface = font.render('choose a difficulty...', 1, Color.TEXT)
        subheading_rect = subheading_surface.get_rect()
        subheading_rect.centerx = self.rect.w // 2
        subheading_rect.top = title_rect.bottom + 100

        button_height = int(0.09 * self.rect.h)
        start_game = game_state.start_game
        easy_button = Button('easy', button_height, lambda: start_game('easy'))
        medium_button = Button('medium', button_height, lambda: start_game('medium'))
        hard_button = Button('hard', button_height, lambda: start_game('hard'))

        medium_button.rect.center = self.rect.w // 2, self.rect.h // 2
        easy_button.rect.y = hard_button.rect.y = medium_button.rect.y
        easy_button.rect.right = medium_button.rect.left - 15
        hard_button.rect.left = medium_button.rect.right + 15

        self.image.blit(title_surface, title_rect)
        self.image.blit(subheading_surface, subheading_rect)
        easy_button.draw(self.image)
        medium_button.draw(self.image)
        hard_button.draw(self.image)

    def draw(self, other_surface: pygame.Surface):
        other_surface.blit(self.image, self.rect)


class BoardView:
    def __init__(self, width, height, game_state) -> None:
        self.game_state = game_state
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(Color.BACKGROUND)

        button_height = int(0.09 * self.rect.h)
        self.exit_btn = Button('exit', button_height, game_state.exit)
        self.restart_btn = Button('restart', button_height, game_state.restart)
        self.reset_btn = Button('reset', button_height, game_state.board.reset)
    
    def draw(self, other_surface):
        self.image.fill(Color.BACKGROUND)

        self.exit_btn.rect.y = self.reset_btn.rect.y = self.restart_btn.rect.y = self.game_state.board.rect.bottom + 15
        self.reset_btn.rect.centerx = self.rect.w // 2
        self.exit_btn.rect.right = self.reset_btn.rect.left - 10
        self.restart_btn.rect.left = self.reset_btn.rect.right + 10

        self.game_state.board.draw(self.image)
        self.exit_btn.draw(self.image)
        self.restart_btn.draw(self.image)
        self.reset_btn.draw(self.image)

        other_surface.blit(self.image, self.rect)
