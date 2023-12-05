import sys

import pygame as pg
import pygame.display


from board import Board
import config
import pubsub
from views import GameLostView, GameWonView, StartMenuView, BoardView


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
        self.screen_rect = screen.get_rect()

        self.start_menu_view = StartMenuView(*self.screen_rect.size, self)
        self.game_won_view = GameWonView(*self.screen_rect.size, self)
        self.game_lost_view = GameLostView(*self.screen_rect.size, self)
        self.board_view = None
        self.board = None

        self.ui_mode = 'start_game'

        pubsub.subscribe('EDIT_CELL_VALUE', self._check_win)
    
    def start_game(self, difficulty: str):
        if self.ui_mode != 'start_game':
            return
        
        self.board = Board(self.screen_rect.w, difficulty)
        self.board_view = BoardView(*self.screen_rect.size, self)
        self.ui_mode = 'playing_game'
    
    def restart(self):       
        self.ui_mode = 'start_game'
        self.board = None
    
    def exit(self):
        

        sys.exit()

    def _check_win(self, cell):
        if not self.board.is_full():
            return
        
        if self.board.is_solved():
            self.ui_mode = 'game_won'
        else:
            self.ui_mode = 'game_lost'

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
            elif event.type == pg.KEYDOWN:
                pubsub.publish(event.type, event.key)
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
        self.screen.fill(config.Color.BACKGROUND)

        if self.ui_mode == 'start_game':
            self.start_menu_view.draw(self.screen)
        elif self.ui_mode == 'playing_game':
            self.board_view.draw(self.screen)
        elif self.ui_mode == 'game_won':
            self.game_won_view.draw(self.screen)
        elif self.ui_mode == 'game_lost':
            self.game_lost_view.draw(self.screen)

        pg.display.flip()  # Re-renders the screen


def new_screen() -> pg.Surface:
    """
    Creates a new Pygame screen based on the user's monitor size.

    Returns:
    - screen (pg.Surface): The Pygame screen surface.
    """
    monitor_height = pg.display.Info().current_h
    width = 0.70 * monitor_height
    height = width + 100

    screen = pg.display.set_mode((width, height))
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

    game = GameState(new_screen())

    fps_clock = pg.time.Clock()
    while True:
        fps_clock.tick(30)  # limit to 30 FPS
        game.check_events()
        game.update()
        game.draw()


if __name__ == '__main__':
    main()
