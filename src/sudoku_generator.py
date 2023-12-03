import math
import random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        """
        create a sudoku board - initialize class variables and set up the 2D board
        This should initialize:
        self.row_length		- the length of each row
        self.removed_cells	- the total number of cells to be removed
        self.board			- a 2D list of ints to represent the board
        self.box_length		- the square root of row_length

        Parameters:
        row_length is the number of rows/columns of the board (always 9 for this project)
        removed_cells is an integer value - the number of cells to be removed

        Return:
        None
        """
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        """
        Returns a 2D python list of numbers which represents the board

        Parameters: None
        Return: list[list]
        """
        return self.board

    def print_board(self):
        """
        Displays the board to the console
        This is not strictly required, but it may be useful for debugging purposes

        Parameters: None
        Return: None
        """
        print(self.board)

    def valid_in_row(self, row, num):
        """
        Determines if num is contained in the specified row (horizontal) of the board
        If num is already in the specified row, return False. Otherwise, return True

        Parameters:
        row is the index of the row we are checking
        num is the value we are looking for in the row

        Return: boolean
        """
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):
        """
        Determines if num is contained in the specified column (vertical) of the board
        If num is already in the specified col, return False. Otherwise, return True

        Parameters:
        col is the index of the column we are checking
        num is the value we are looking for in the column

        Return: boolean
        """
        for row in self.board:
            if num == row[col]:
                return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num):
        """
        Determines if num is contained in the 3x3 box specified on the board
        If num is in the specified box starting at (row_start, col_start), return False.
        Otherwise, return True

        Parameters:
        row_start and col_start are the starting indices of the box to check
        i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
        num is the value we are looking for in the box

        Return: boolean
        """
        # Finds the top left corner of the default box for the given index
        row_i = row_start  # Tracks new row index
        col_j = col_start  # Tracks new col index

        # If the indexes aren't divisible by 3, subtract one until it is.
        # This way, it will find the closest default box
        while row_i % 3 != 0:
            row_i -= 1
        while col_j % 3 != 0:
            col_j -= 1

        # Finally, check every cell in the box to see if the number would
        # be a valid addition.
        for i in range(row_i, row_i + 3):
            for j in range(col_j, col_j + 3):
                if num == self.board[i][j]:
                    return False
        else:
            return True

    def is_valid(self, row, col, num):
        """
        Determines if it is valid to enter num at (row, col) in the board
        This is done by checking that num is unused in the appropriate, row, column, and box

        Parameters:
        row and col are the row index and col index of the cell to check in the board
        num is the value to test if it is safe to enter it into this cell

        Return: boolean
        """

        # Must pass all checks to be valid: Row, Col, and Box
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        """
        Fills the specified 3x3 box with values
        For each position, generates a random digit which has not yet been used in the box

        Parameters:
        row_start and col_start are the starting indices of the box to check
        i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

        Return: None
        """
        row_i = row_start  # Tracks new row index
        col_j = col_start  # Tracks new col index

        # If the indexes aren't divisible by 3, subtract one until it is.
        # This way, it will find the closest default box's top left corner.
        while row_i % 3 != 0:
            row_i -= 1
        while col_j % 3 != 0:
            col_j -= 1

        # Iterate through the box, generating a random number each time and checking if it can be placed in the box.
        for i in range(row_i, row_i + 3):
            for j in range(col_j, col_j + 3):
                while True:
                    num = random.randint(1, 9)
                    if self.valid_in_box(row_i, col_j, num):
                        self.board[i][j] = num
                        break

    def fill_diagonal(self):
        """
        Fills the three boxes along the main diagonal of the board
        These are the boxes which start at (0,0), (3,3), and (6,6)

        Parameters: None
        Return: None
        """
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        """
        DO NOT CHANGE
        Provided for students
        Fills the remaining cells of the board
        Should be called after the diagonal boxes have been filled

        Parameters:
        row, col specify the coordinates of the first empty (0) cell

        Return:
        boolean (whether we could solve the board)
        """
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        """
        DO NOT CHANGE
        Provided for students
        Constructs a solution by calling fill_diagonal and fill_remaining

        Parameters: None
        Return: None
        """
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        """
        Removes the appropriate number of cells from the board
        This is done by setting some values to 0
        Should be called after the entire solution has been constructed
        i.e. after fill_values has been called

        NOTE: Be careful not to 'remove' the same cell multiple times
        i.e. if a cell is already 0, it cannot be removed again

        Parameters: None
        Return: None
        """
        count = 0
        while count != self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
            count += 1


def generate_sudoku(size, removed):
    """
    DO NOT CHANGE
    Provided for students
    Given a number of rows and number of cells to remove, this function:
    1. creates a SudokuGenerator
    2. fills its values and saves this as the solved state
    3. removes the appropriate number of cells
    4. returns the representative 2D Python Lists of the board and solution

    Parameters:
    size is the number of rows/columns of the board (9 for this project)
    removed is the number of cells to clear (set to 0)

    Return: list[list] (a 2D Python list to represent the board)
    """
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


if __name__ == "__main__":
    # Get an example board with 5 removed values
    print(generate_sudoku(9, 0))