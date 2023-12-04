import pygame as pg

import config
import pubsub


class Button:
    def __init__(self, width, height, text, on_click_function) -> None:
        """
        Initializes a Button object.

        Args:
        - width (int): The width of the button.
        - height (int): The height of the button.
        - text (str): The text displayed on the button.
        - on_click_function (function): The function to be executed when the button is clicked.
        """
        self.text = text
        self.on_click_function = on_click_function

        # image and rect for drawing to screen
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.rect = self.image.get_rect()

        pubsub.subscribe(pg.MOUSEBUTTONUP, self.on_click)

    def on_click(self, mouse_pos):
        """Can be called on mouse up or mouse down to react to user clicking on
        screen"""
        if self.rect.collidepoint(mouse_pos):
            self.on_click_function()

    def draw(self, other_surface: pg.Surface):
        # ceate border effect
        self.image.fill(config.Color.BLACK)  # border color
        background_rect = self.rect.inflate(-6, -6)  # shrinked version of rect
        background_rect.center = (self.rect.width // 2, self.rect.height // 2)
        self.image.fill(config.Color.BUTTON_BACKGROUND, background_rect)

        # create text
        text = pg.font.Font(config.BUTTON_FONT_PATH, int(0.35 * self.rect.height))
        # render the text to a surf
        text_render = text.render(self.text, True, config.Color.BLACK)
        # create a rect to blit the text onto the button image
        text_render_rect = text_render.get_rect()
        text_render_rect.center = background_rect.center
        # paste/blit text onto button
        self.image.blit(text_render, text_render_rect)

        # blit self to other surface
        other_surface.blit(self.image, self.rect)
