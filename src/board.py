from copy import deepcopy
import pygame as pg

from cell import Cell


class Board:
    def __init__(self, width: int, height: int, board_state: list[list[int]]):
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()

        self.selected_cell = (0, 0)

        # convert values in board to cell objects
        self.initial_state = deepcopy(board_state)
        self.cells = None
        self._build_cells(board_state)
    
    def _build_cells(self, board_state):
        self.cells = deepcopy(board_state)

        for i, row in enumerate(self.cells):
            for j, value in enumerate(row):
                self.cells[i][j] = Cell(value, i, j)
    
    def draw(self, other_surface):
        other_surface.blit(self.image, self.rect)
    
    def reset(self):
        self._build_cells(self.initial_state)
    
    def get_all_cells(self):
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

        
