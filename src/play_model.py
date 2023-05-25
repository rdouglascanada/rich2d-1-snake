from rich2d.models import Model
from rich2d.sprites.shapes import Rectangle
from rich2d.elements.grid import Grid, GridElement
from rich2d.sprites import Text


class SnakePlayModel(Model):
    def __init__(self, game_state, window_width, window_height):
        play_rows = 20
        play_columns = 20
        play_grid = Grid(rect=(0, 0, window_width, window_height - 100), rows=play_rows, columns=play_columns)

        play_background = Rectangle(rect=(0, 0, 0, 0), colour="yellow")
        play_background_element = GridElement(sprite=play_background, grid=play_grid,
                                              grid_tiles=(0, 0, play_columns, play_rows))
        top_boundary = Rectangle(rect=(0, 0, 0, 0), colour="darkgray")
        top_boundary_element = GridElement(sprite=top_boundary, grid=play_grid,
                                           grid_tiles=(0, 0, play_columns, 1))
        left_boundary = Rectangle(rect=(0, 0, 0, 0), colour="darkgray")
        left_boundary_element = GridElement(sprite=left_boundary, grid=play_grid,
                                            grid_tiles=(0, 1, 1, play_rows - 2))
        right_boundary = Rectangle(rect=(0, 0, 0, 0), colour="darkgray")
        right_boundary_element = GridElement(sprite=right_boundary, grid=play_grid,
                                             grid_tiles=(play_columns - 1, 1, 1, play_rows - 2))
        bottom_boundary = Rectangle(rect=(0, 0, 0, 0), colour="darkgray")
        bottom_boundary_element = GridElement(sprite=bottom_boundary, grid=play_grid,
                                              grid_tiles=(0, play_rows - 1, play_columns, 1))

        status_grid = Grid(rect=(0, window_height - 100, window_width, 100), rows=2, columns=20)
        score_label_text = Text(text="Score:", rect=(0, 0, 0, 0), colour="black",
                                font_name="courier", font_size=32, font_bold=True,
                                horizontal_alignment=Text.HorizontalAlignment.RIGHT)
        score_label_text_element = GridElement(sprite=score_label_text, grid=status_grid,
                                               grid_tiles=(0, 0, 5, 2))

        score_text = Text(text="0", rect=(0, 0, 0, 0), colour="black",
                          font_name="courier", font_size=32, font_bold=True,
                          horizontal_alignment=Text.HorizontalAlignment.CENTRE)
        score_text_element = GridElement(sprite=score_text, grid=status_grid,
                                         grid_tiles=(6, 0, 1, 2))

        sprites = [play_background, top_boundary, left_boundary, right_boundary, bottom_boundary,
                   score_label_text, score_text]
        elements = [play_background_element, top_boundary_element, left_boundary_element,
                    right_boundary_element, bottom_boundary_element,
                    score_label_text_element, score_text_element]
        handlers = []
        super().__init__(sprites=sprites, elements=elements, handlers=handlers)
        return
