import pygame
from rich2d.models import Model
from rich2d.elements.grid import Grid, GridElement
from rich2d.elements.animated_text import FlashingText
from rich2d.sprites import Text
from rich2d.handlers import KeyboardHandler


class SnakeTitleModel(Model):
    def __init__(self, game_state, window_width, window_height):
        title_grid = Grid(rect=(0, 0, window_width, window_height), rows=10, columns=10)
        title_text = Text(rect=(0, 0, 0, 0), text="Snake", colour="green",
                          font_size=160, font_bold=True, font_name="courier",
                          horizontal_alignment=Text.HorizontalAlignment.RIGHT)
        title_text_grid_element = GridElement(sprite=title_text, grid=title_grid, grid_tiles=(1, 3, 8, 2))

        spacebar_text = Text(rect=(0, 0, 0, 0), text="Press spacebar to begin", colour="black",
                             font_size=40, font_italic=True, font_name="monospace",
                             horizontal_alignment=Text.HorizontalAlignment.CENTRE)
        spacebar_text_grid_element = GridElement(sprite=spacebar_text, grid=title_grid, grid_tiles=(1, 5, 8, 1))
        flashing_text_element = FlashingText(text_sprite=spacebar_text, flash_interval=2, flashes_per_interval=1)

        def handle_spacebar_press():
            game_state.set_value("play")
            return
        keyboard_handler = KeyboardHandler(key_pressed_map={pygame.K_SPACE: handle_spacebar_press})

        sprites = [title_text, spacebar_text]
        elements = [title_text_grid_element, spacebar_text_grid_element, flashing_text_element]
        handlers = [keyboard_handler]
        super().__init__(sprites=sprites, elements=elements, handlers=handlers)
        return
