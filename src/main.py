import pygame as pg

class GameState:
    """Class to manage and update game objects and draw to screen."""
    def __init__(self, screen):
        self.screen = screen

    def check_events(self):
        """Check pygame events and update game state / objects"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    def update(self):
        """This method runs on each frame to make updates to game objects like
        the Board"""
        pass

    def draw(self):
        """Draw the UI onto the pygame screen"""
        self.screen.flip()


def new_screen() -> pg.Surface:
    """Creates a new pygame screen based on the user's monitor size"""
    monitor_height = pg.display.Info().current_h
    height = width = 0.45 * monitor_height

    screen = pg.display.set_mode((height, width))
    pg.display.set_caption('Sudoku 66')

    return screen


def main():
    # need to initialize display module before making a new screen
    pg.display.init()

    screen = new_screen()
    game = GameState(screen)

    while True:
        game.check_events()
        game.update()
        game.draw_screen(screen)


if __name__ == '__main__':
    main()