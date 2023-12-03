from enum import Enum
import pygame as pg


class Color(tuple, Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BACKGROUND = (81, 86, 121)
    BUTTON_BACKGROUND = (153, 174, 191)


BUTTON_FONT_PATH = './assets/Blox2.ttf'
CELL_FONT = 50  # TODO: Should this be dependant on the size of the displayed area?
CELL_SIZE = 50  # TODO: Should this be dependant on the size of the displayed area?
