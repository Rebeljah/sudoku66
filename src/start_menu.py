import pygame
import sys

from config import Color


def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 20)

    screen.fill(Color.BACKGROUND)

    monitor_height = pygame.display.Info().current_h
    height = width = 0.70 * monitor_height
    title_surface = start_title_font.render('Welcome to Sudoku', 0, Color.WHITE)
    title_rectangle = title_surface.get_rect(
        center=(height // 2 + 100, width // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render('Easy Mode', 0, (255, 255, 255))
    medium_text = button_font.render('Medium Mode', 0, (255, 255, 255))
    hard_text = button_font.render('Hard Mode', 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(Color.BLACK)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(Color.BLACK)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(Color.BLACK)
    hard_surface.blit(hard_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(width // 2 - 50, height // 2 + 150))
    medium_rectangle = medium_surface.get_rect(
        center=(width // 2 + 100, height // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(width // 2 + 250, height // 2 + 150))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 'easy_mode'
                if medium_rectangle.collidepoint(event.pos):
                    return 'medium_mode'
                if hard_rectangle.collidepoint(event.pos):
                    return 'hard_mode'
        pygame.display.update()
