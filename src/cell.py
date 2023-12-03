import pygame as pg
from config import *


class Cell:
    """
    Represents a single cell in the Sudoku board. A typical board consists of 81 cells.
    """

    def __init__(self, value, row, col, screen) -> None:
        """
        Constructor for the Cell class

        :param int value: The value (confirmed) in the cell
        :param int row: The row coordinate of the cell
        :param int col: The col coordinate of the cell
        :param pg.Surface screen: The screen to draw the cell on
        :return: None
        """
        self.selected = False
        self.value = value  # The confirmed value in the cell
        self.sketched_value = -1  # The unconfirmed value in the cell
        self.row = row  # The row coordinate of the cell
        self.col = col  # The col coordinate of the cell
        self.screen = screen  # The screen to draw the cell on

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

    def draw(self) -> None:
        """
        Draws the cell and the value within it, as long as the value is non-zero.
        Outlines the cell Red if it currently selected.

        :param: None
        :return: None
        """
        # Creating the cell font
        cell_font = pg.font.Font(None, CELL_FONT)
        sketched_font = pg.font.Font(None, SKETCHED_FONT)

        # Creating the cell surface
        cell_surface = cell_font.render(str(self.value), 1, Color.BLACK)

        # Creating a rectangle to blit the text onto the cell
        cell_rect = cell_surface.get_rect(
            center=(CELL_SIZE * self.col + CELL_SIZE // 2, CELL_SIZE * self.row + CELL_SIZE // 2))

        # Draw the value only if it is non-zero
        # And draw any sketched values in light gray in the top left corner of the cell
        if self.value != 0:
            self.screen.blit(cell_surface, cell_rect)
        elif self.sketched_value != -1:
            sketched_surface = sketched_font.render(str(self.sketched_value), 1, Color.LIGHT_GRAY)
            sketched_rect = sketched_surface.get_rect(
                center=(CELL_SIZE * self.col + CELL_SIZE // 4, CELL_SIZE * self.row + CELL_SIZE // 4))
            self.screen.blit(sketched_surface, sketched_rect)

        # Draw the cell outline if it is selected
        if self.selected:
            pg.draw.rect(self.screen, Color.RED, (CELL_SIZE * self.col, CELL_SIZE * self.row, CELL_SIZE, CELL_SIZE),
                         2)