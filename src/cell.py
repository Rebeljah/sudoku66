import pygame as pg
from config import *


class Cell:
    """
    Represents a single cell in the Sudoku board. A typical board consists of 81 cells.
    """

    def __init__(self, value, topleft, size) -> None:
        """
        Constructor for the Cell class

        :param int value: The value (confirmed) in the cell
        :param int row: The row coordinate of the cell
        :param int col: The col coordinate of the cell
        :return: None
        """
        self.selected = False
        self.value = value  # The confirmed value in the cell
        self.sketched_value = -1  # The unconfirmed value in the cell
        self.size = size

        self.image = pg.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.background_color = Color.LIGHT_GRAY


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
            render = cell_font.render(str(self.value), 1, Color.BLACK)
            render_rect = render.get_rect(center=self.rect.center)
            self.image.blit(render, render_rect)
        elif self.sketched_value != -1:
            render = sketched_font.render(str(self.sketched_value), 1, Color.LIGHT_GRAY)
            render_rect = render.get_rect(center=self.rect.center)
            self.image.blit(render, render_rect)

        # Draw the cell outline if it is selected
        if self.selected:
            pg.draw.rect(self.image, Color.RED, self.rect, 2)
        
        other_surface.blit(self.image, self.rect)