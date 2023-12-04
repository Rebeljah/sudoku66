import sys

import pygame as pg
import pygame.display

from sudoku_generator import SudokuGenerator
from button import Button
from cell import Cell
from board import Board
import config
import pubsub
from start_menu import  draw_game_start
from game_won_menu import draw_game_won
from  game_over_menu import draw_game_over
class GameState:
    """
    Class to manage and update game objects and draw to screen.
    """

    def __init__(self, screen: pg.Surface, mode):
        """
        Initializes the game state.

        Args:
        - screen (pg.Surface): The Pygame surface to draw the game.
        """
        removed_cells=0
        if mode == 'easy_mode':
            removed_cells = 30
        elif mode == 'medium_mode':
            removed_cells = 40
        elif mode == 'hard_mode':
            removed_cells = 50

        self.generator = SudokuGenerator(config.ROW_LENGTH, removed_cells)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.board = Board(self.screen_rect.width)

    @staticmethod
    def check_events():
        """
        Checks Pygame events and updates game state/objects accordingly.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONUP:
                pubsub.publish(event.type, pg.mouse.get_pos())
            elif event.type == pg.MOUSEMOTION:
                pubsub.publish(event.type, pg.mouse.get_pos())
            elif event.type == pg.KEYUP:
                pubsub.publish(event.type, event.key)

    def update(self):
        """
        Updates game objects on each frame.
        """
        pass

    def draw(self):
        """
        Draws the UI onto the Pygame screen.
        """
        # Base background
        self.screen.fill(config.Color.RED)

        self.board.draw(self.screen)

        pg.display.flip()  # Re-renders the screen


def new_screen() -> pg.Surface:
    """
    Creates a new Pygame screen based on the user's monitor size.

    Returns:
    - screen (pg.Surface): The Pygame screen surface.
    """
    monitor_height = pg.display.Info().current_h
    height = width = 0.70 * monitor_height

    screen = pg.display.set_mode((height, width+100))
    pg.display.set_caption('Sudoku 66')

    return screen


def main():
    """
    Main function to run the game.
    """
    # Need to initialize display module before making a new screen
    pg.display.init()
    # Init font package before using it
    pg.font.init()
    monitor_height = pg.display.Info().current_h
    height = width = 0.70 * monitor_height
    start_screen = pygame.display.set_mode((height,width))
    mode =  draw_game_start(start_screen)
    if mode:
        print('creating new game board')
        screen = new_screen()
        game = GameState(screen, mode = mode)

    fps_clock = pg.time.Clock()
    while True:
        fps_clock.tick(30)  # limit to 30 FPS
        game.check_events()
        game.update()
        game.draw()


if __name__ == '__main__':
    main()
