from copy import deepcopy
import pygame as pg

from cell import Cell
from sudoku_generator import SudokuGenerator
import config
import pubsub


class Board:
    def __init__(self, width: int, difficulty):
        self.image = pg.Surface((width, width))
        self.rect = self.image.get_rect()

        # Determines removed_cells based on difficulty
        if difficulty == 'easy':
            removed_cells = 30
        elif difficulty == 'medium':
            removed_cells = 40
        elif difficulty == 'hard':
            removed_cells = 50

        self.generator = SudokuGenerator(config.ROW_LENGTH, removed_cells)
        self.generator.fill_values()
        self.generator.remove_cells()

        board_state = self.generator.get_board()
        self.selected_cell = None
        self.board_size = len(board_state)
        self.cell_size = width // self.board_size

        # convert values in board to cell objects
        self.initial_state = deepcopy(board_state)
        self.cells = None
        self._build_cells(board_state)

        #listen for click to select a cell
        pubsub.subscribe(pg.MOUSEBUTTONUP, self._check_click)
    
    def _check_click(self, mouse_pos):
        if not self.rect.collidepoint(mouse_pos):
            return
        
        col = (mouse_pos[0] - self.rect.x) // self.cell_size
        row = (mouse_pos[1] - self.rect.y) // self.cell_size

        self._select_cell(self.cells[col][row])                    
    
    def _select_cell(self, cell):
        if self.selected_cell:
            self.selected_cell.selected = False

        cell.selected = True
        self.selected_cell = cell

    def _build_cells(self, board_state):
        self.cells = deepcopy(board_state)

        for i, row in enumerate(self.cells):
            for j, value in enumerate(row):
                x = self.cell_size * i
                y = self.cell_size * j
                is_editable = value == 0
                self.cells[i][j] = Cell(value, (x, y), self.cell_size, is_editable)

    def draw(self, other_surface):
        self.image.fill(config.Color.RED)  # TODO: Get rid of the red outline around the box.

        # draw cells
        for cell in self.get_all_cells():
            cell.draw(self.image)
            if cell is self.selected_cell:
                pg.draw.rect(self.image, config.Color.RED, cell.rect, 3)

        # draw grid lines.
        for x in range(0, self.rect.width + 1, self.cell_size):

            # Every third line should be thicker to indicate the 3x3 boxes.
            if x % (self.cell_size * 3) == 0:
                pg.draw.line(self.image, config.Color.BLACK, (x, 0), (x, self.rect.height), 3)
            else:
                pg.draw.line(self.image, config.Color.BLACK, (x, 0), (x, self.rect.height))

        for y in range(0, self.rect.height + 1, self.cell_size):

            # Every third line should be thicker to indicate the 3x3 boxes.
            if y % (self.cell_size * 3) == 0:
                pg.draw.line(self.image, config.Color.BLACK, (0, y), (self.rect.width, y), 3)
            else:
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
