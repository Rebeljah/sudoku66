from enum import Enum
import pygame as pg


class Color(tuple, Enum):
    BLACK = (0, 0, 0)
    BACKGROUND = (208, 71, 29)
    BUTTON_BACKGROUND = (153, 174, 191)

BUTTON_FONT_PATH = './assets/Blox2.ttf'