import pygame as pg

from config import *

class Cell:
    """
    Represents a single cell in the Sudoku board. A typical board consists of 81 cells.
    """

    def __init__(self, value, row, col, screen) -> None:
        """
        Constructor for the Cell class

        :param int value: The value in the cell
        :param int row: The row coordinate of the cell
        :param int col: The col coordinate of the cell
        :param pg.Surface screen: The screen to draw the cell on
        :return: None
        """
        self.value = value
        self.sketched_value = 0  # TODO: Review sketched value functionality to see if this is necessary
        self.row = row
        self.col = col
        self.screen = screen

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

    def draw(self) -> None:
        """
        Draws the cell and the value within it, as long as the value is non-zero.
        Outlines the cell Red if it currently selected.

        :param: None
        :return: None
        """

        # Creating the cell font
        cell_font = pg.font.Font(None, CELL_FONT)

        # Creating the cell surface
        cell_surface = cell_font.render(str(self.value), 0, Color.BLACK)

        # Creating a rectangle to blit the text onto the cell
        cell_rect = cell_surface.get_rect(
            center=(CELL_SIZE * self.col + CELL_SIZE // 2, CELL_SIZE * self.row + CELL_SIZE // 2))

        # Drawing the cell onto the screen
        self.screen.blit(cell_surface, cell_rect)
