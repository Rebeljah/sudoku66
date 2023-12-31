import pygame as pg
from config import *
import pubsub


class Cell:
    """
    Represents a single cell in the Sudoku board. A typical board consists of 81 cells.
    """

    def __init__(self, value, topleft, position, size, is_editable, selected=False) -> None:
        """
        Constructor for the Cell class

        :param int value: The value (confirmed) in the cell
        :param int row: The row coordinate of the cell
        :param int col: The col coordinate of the cell
        :return: None
        """
        self.row, self.column = position
        self.selected = selected
        self.is_editable = is_editable
        self.value = value  # The confirmed value in the cell
        self.sketched_value = 0  # The unconfirmed value in the cell
        self.size = size

        self.image = pg.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.background_color = Color.CELL_BACKGROUND

        pubsub.subscribe(pg.KEYUP, self.on_key_up)

    def on_key_up(self, key) -> None:
        """
        Checks if the key pressed a key.
        If a number key is pressed, set the sketched value as the number.
        If the backspace key is pressed, set the sketched value to 0.
        If the enter key is pressed, set the value as the sketched value.

        :param int key: The key pressed
        :return: None
        """
        number_keys = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]
        if self.selected and self.is_editable and key in number_keys:
            self.sketched_value = int(pg.key.name(key))
        elif self.selected and self.is_editable and key == pg.K_BACKSPACE:
            self.sketched_value = 0
        elif self.selected and self.is_editable and key == pg.K_RETURN and self.sketched_value != 0:
            self.value = self.sketched_value
            self.sketched_value = 0
            self.is_editable = False
            pubsub.publish('EDIT_CELL_VALUE', self)

    def draw(self, other_surface) -> None:
        """
        Draws the cell and the value within it, as long as the value is non-zero.
        Outlines the cell Red if it currently selected.

        :param: other_surface: The surface to draw the cell onto
        :return: None
        """
        self.image.fill(self.background_color)

        # Creating the cell font
        cell_font = pg.font.Font(None, CELL_FONT)
        sketched_font = pg.font.Font(None, SKETCHED_FONT)

        # Draw the value if it is non-zero
        if self.value != 0:
            color = Color.BLACK
            render = cell_font.render(str(self.value), 1, color)
            render_rect = render.get_rect(center=self.image.get_rect().center)
            self.image.blit(render, render_rect)

        # Draw the sketched value if it is non-zero, and render it in the top left corner
        if self.sketched_value != 0:
            color = Color.LIGHT_GRAY
            render = sketched_font.render(str(self.sketched_value), 1, color)
            render_rect = render.get_rect(topleft=(10, 10))
            self.image.blit(render, render_rect)

        other_surface.blit(self.image, self.rect)
