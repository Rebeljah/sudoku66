import pygame, sys
from config import Color

def draw_game_over(screen):
    start_title_font= pygame.font.Font(None,100)
    button_font = pygame.font.Font(None,70)

    screen.fill(Color.BACKGROUND)

    monitor_height = pygame.display.Info().current_h
    height = width = 0.70 * monitor_height
    title_surface = start_title_font.render('Game Over',0,Color.WHITE)
    title_rectangle = title_surface.get_rect(
        center=(height // 2, width //2 - 150))
    screen.blit(title_surface, title_rectangle)


    start_text = button_font.render('Start',0,(255,255,255))
    quit_text = button_font.render('Quit',0,(255,255,255))

    start_surface =pygame.Surface((start_text.get_size()[0] + 20, start_text.get_size()[1] + 20))
    start_surface.fill(Color.WHITE)
    start_surface.blit(start_text,(10,10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(Color.WHITE)
    quit_surface.blit(quit_text, (10,10))

    start_rectangle = start_surface.get_rect(
        center = (width // 2, height // 2 + 50))
    quit_rectangle = quit_surface.get_rect(
        center = (width//2, height//2 + 150))

    screen.blit(start_surface, start_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
