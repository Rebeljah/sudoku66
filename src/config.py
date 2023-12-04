from enum import Enum
import pygame as pg


class Color(tuple, Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    LIGHT_GRAY = (128, 128, 128)
    BACKGROUND = (81, 86, 121)
    BUTTON_BACKGROUND = (153, 174, 191)


ROW_LENGTH = 9
BUTTON_FONT_PATH = './assets/Blox2.ttf'
CELL_FONT = 50  # TODO: Should this be dependant on the size of the displayed area?
SKETCHED_FONT = 40  # TODO: Should this be dependant on the size of the displayed area?
CELL_SIZE = 50  # TODO: Should this be dependant on the size of the displayed area?
