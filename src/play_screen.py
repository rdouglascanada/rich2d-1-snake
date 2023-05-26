from rich2d.models import Model, ModelGroup
from rich2d.sprites.shapes import Rectangle, Circle
from rich2d.elements.grid import Grid, GridElement
from rich2d.sprites import Text
from game import ScoreElement, SnakeModel


def snake_play_screen(window_width, window_height):
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
    food_sprite = Circle(rect=(0, 0, 0, 0), colour="red")
    food_element = GridElement(sprite=food_sprite, grid=play_grid,
                               grid_tiles=(5, 5, 1, 1))

    status_grid = Grid(rect=(0, window_height - 100, window_width, 100), rows=2, columns=20)
    score_label_text = Text(text="Score:", rect=(0, 0, 0, 0), colour="black",
                            font_name="courier", font_size=32, font_bold=True,
                            horizontal_alignment=Text.HorizontalAlignment.RIGHT)
    score_label_grid_element = GridElement(sprite=score_label_text, grid=status_grid,
                                           grid_tiles=(0, 0, 5, 2))

    score_text = Text(text="", rect=(0, 0, 0, 0), colour="black",
                      font_name="courier", font_size=32, font_bold=True,
                      horizontal_alignment=Text.HorizontalAlignment.CENTRE)
    score_text_grid_element = GridElement(sprite=score_text, grid=status_grid,
                                          grid_tiles=(6, 0, 1, 2))
    score_sync_element = ScoreElement(score_text_sprite=score_text, score=0)

    snake_model = SnakeModel(play_grid=play_grid)

    sprites = [play_background, top_boundary, left_boundary, right_boundary, bottom_boundary,
               score_label_text, score_text, food_sprite]
    elements = [play_background_element, top_boundary_element, left_boundary_element,
                right_boundary_element, bottom_boundary_element, food_element,
                score_label_grid_element, score_text_grid_element, score_sync_element]
    handlers = []
    play_model = ModelGroup(models=[Model(sprites=sprites, elements=elements, handlers=handlers), snake_model])
    return play_model
