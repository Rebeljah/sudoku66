import pygame as pg

class GameState:
    def __init__(self, screen):
        self.screen = screen

    def check_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.flip()


def check_events(game: GameState):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()


def update_game(game: GameState):
    pass


def draw_screen(game: GameState, screen: pg.Surface):
    pass


def new_screen() -> pg.Surface:
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