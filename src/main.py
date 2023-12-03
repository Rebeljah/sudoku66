import pygame as pg
from button import Button
from cell import Cell
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
        self.screen = screen

        # FIXME: Testing elements
        self.test_button = Button(150, 75, 'click me', lambda: print('click!'))
        self.test_cell0 = Cell(1, 4, 4, self.screen)
        self.test_cell1 = Cell(1, 5, 5, self.screen)
        self.test_cell2 = Cell(2, 5, 6, self.screen)
        self.test_cell3 = Cell(0, 5, 7, self.screen)
        self.test_cell4 = Cell(4, 5, 8, self.screen)
        self.test_cell5 = Cell(4, 8, 8, self.screen)

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
        self.screen.fill(config.Color.BACKGROUND)

        # FIXME: Testing drawing
        self.test_button.draw(self.screen)
        self.test_cell0.draw()
        self.test_cell1.draw()
        self.test_cell2.draw()
        self.test_cell3.draw()
        self.test_cell4.draw()
        self.test_cell3.set_sketched_value(6)
        self.test_cell3.set_selected(True)

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

    while True:
        game.check_events()
        game.update()
        game.draw()


if __name__ == '__main__':
    main()
