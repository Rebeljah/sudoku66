import pygame as pg
from config import *
import pubsub


class Cell:
    """
    Represents a single cell in the Sudoku board. A typical board consists of 81 cells.
    """

    def __init__(self, value, topleft, size, is_editable, selected=False) -> None:
        """
        Constructor for the Cell class

        :param int value: The value (confirmed) in the cell
        :param int row: The row coordinate of the cell
        :param int col: The col coordinate of the cell
        :return: None
        """
        self.selected = selected
        self.is_editable = is_editable
        self.value = value  # The confirmed value in the cell
        self.sketched_value = -1  # The unconfirmed value in the cell
        self.size = size

        self.image = pg.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.background_color = Color.CELL_BACKGROUND

        # Subscribe to mouse button up events
        pubsub.subscribe(pg.MOUSEBUTTONUP, self.on_click)
        pubsub.subscribe(pg.KEYUP, self.on_key_up)

    def on_key_up(self, key):
        # Function for if the cell is selected and and it is editable, then when a number is pressed, it will be set
        # as value of the cell.
        number_keys = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]
        if self.selected and self.is_editable and key in number_keys:
            self.value = int(pg.key.name(key))

    def on_click(self, mouse_pos):
        """
        Checks if the mouse click is within the cell's rect.
        If so, set the cell as selected.
        Otherwise, deselect it.
        """
        if self.rect.collidepoint(mouse_pos):
            self.selected = True
        else:
            self.selected = False

    def set_cell_value(self, value) -> None:
        """
        Sets the cell's value

        :param int value: The value to be set
        :return: None
        """
        self.value = value

    def set_sketched_value(self, value) -> None:
        """
        Sets the cell's sketched value

        :param int value: The value to be sketched
        :return: None
        """
        self.sketched_value = value

    def set_selected(self, selected) -> None:
        """
        Sets the cell's selected status

        :param bool selected: The selected status to be set
        :return: None
        """
        self.selected = selected

    def draw(self, other_surface) -> None:
        """
        Draws the cell and the value within it, as long as the value is non-zero.
        Outlines the cell Red if it currently selected.

        :param: None
        :return: None
        """
        self.image.fill(self.background_color)

        # Creating the cell font
        cell_font = pg.font.Font(None, CELL_FONT)
        sketched_font = pg.font.Font(None, SKETCHED_FONT)

        # Draw the value only if it is non-zero
        # And draw any sketched values in light gray in the top left corner of the cell
        if self.value != 0:
            color = Color.BLACK if self.is_editable else Color.RED
            render = cell_font.render(str(self.value), 1, color)
            render_rect = render.get_rect(center=self.image.get_rect().center)
            self.image.blit(render, render_rect)

        # TODO: Might be unnecessary code below in comment
        # elif self.sketched_value != -1:
        #     render = sketched_font.render(str(self.sketched_value), 1, Color.LIGHT_GRAY)
        #     render_rect = render.get_rect(center=self.image.get_rect().center)
        #     self.image.blit(render, render_rect)

        # Draw the cell outline if it is selected
        if self.selected:
            pg.draw.rect(self.image, Color.RED, self.image.get_rect(), 2)

        other_surface.blit(self.image, self.rect)
