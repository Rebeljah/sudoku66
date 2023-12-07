import pygame as pg

import config
import pubsub


class Button:
    def __init__(self, text, height, on_click_function) -> None:
        """
        Initializes a Button object.

        Args:
        - text (str): The text displayed on the button.
        - height (int): The height of the button.
        - on_click_function (function): The function to be executed when the button is clicked.
        """
        self.on_click_function = on_click_function

        font = pg.font.Font(config.BUTTON_FONT_PATH, int(0.30 * height))
        # render the text to a surf
        text_render = font.render(text, True, config.Color.BLACK)
        text_rect = text_render.get_rect()

        # image and rect for drawing to screen
        self.image = pg.Surface((text_render.get_width() + 30, height))
        self.rect = self.image.get_rect()

        # border and bg
        self.image.fill(config.Color.BUTTON_BACKGROUND)
        pg.draw.rect(self.image, config.Color.BLACK, self.rect, 3)

        # add text
        text_rect.center = self.rect.w // 2, self.rect.h // 2
        self.image.blit(text_render, text_rect)

        pubsub.subscribe(pg.MOUSEBUTTONUP, self.on_click)
        self.is_active = False
    
    def activate(self):
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False

    def on_click(self, mouse_pos):
        """Can be called on mouse up or mouse down to react to user clicking on
        screen"""
        if self.is_active and self.rect.collidepoint(mouse_pos):
            self.on_click_function()

    def draw(self, other_surface: pg.Surface):
        other_surface.blit(self.image, self.rect)
