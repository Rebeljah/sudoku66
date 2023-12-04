import pygame as pg

from sudoku_generator import SudokuGenerator
from button import Button
from cell import Cell
from board import Board
import config
import pubsub


class GameState:
    """
    Class to manage and update game objects and draw to screen.
    """

    def __init__(self, screen: pg.Surface):
        """
        Initializes the game state.

        Args:
        - screen (pg.Surface): The Pygame surface to draw the game.
        """
        self.generator = SudokuGenerator(config.ROW_LENGTH, 10)
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

    screen = pg.display.set_mode((height, width))
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

    screen = new_screen()
    game = GameState(screen)

    fps_clock = pg.time.Clock()
    while True:
        fps_clock.tick(30) # limit to 30 FPS
        game.check_events()
        game.update()
        game.draw()


if __name__ == '__main__':
    main()
