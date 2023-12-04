from copy import deepcopy
import pygame as pg

from cell import Cell
from sudoku_generator import SudokuGenerator
import config


class Board:
    def __init__(self, width: int):
        self.image = pg.Surface((width, width))
        self.rect = self.image.get_rect()

        self.generator = SudokuGenerator(config.ROW_LENGTH, 15)
        self.generator.fill_values()
        self.generator.remove_cells()

        board_state = self.generator.get_board()
        self.selected_cell = (0, 0)
        self.board_size = len(board_state)
        self.cell_size = width // self.board_size

        # convert values in board to cell objects
        self.initial_state = deepcopy(board_state)
        self.cells = None
        self._build_cells(board_state)

    def _build_cells(self, board_state):
        self.cells = deepcopy(board_state)

        for i, row in enumerate(self.cells):
            for j, value in enumerate(row):
                x = self.cell_size * i
                y = self.cell_size * j
                is_editable = value == 0
                self.cells[i][j] = Cell(value, (x, y), self.cell_size, is_editable)

    def draw(self, other_surface):
        self.image.fill(config.Color.LIGHT_GRAY)

        # draw cells
        for cell in self.get_all_cells():
            cell.draw(self.image)

        # draw grid lines
        for x in range(0, self.rect.width + 1, self.cell_size):
            pg.draw.line(self.image, config.Color.BLACK, (x, 0), (x, self.rect.height))

        for y in range(0, self.rect.height + 1, self.cell_size):
            pg.draw.line(self.image, config.Color.BLACK, (0, y), (self.rect.width, y))

        other_surface.blit(self.image, self.rect)

    def reset(self):
        self._build_cells(self.initial_state)

    def get_all_cells(self) -> list[Cell]:
        cells = []

        if self.cells is None:
            return []

        for row in self.cells:
            for cell in row:
                cells.append(cell)

        return cells

    def is_full(self):
        for cell in self.get_all_cells():
            if cell.value == 0:
                return False
        else:
            return True
