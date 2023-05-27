import pygame
from rich2d.models import Model, ModelGroup
from rich2d.models.state import State, StateModel
from rich2d.sprites.shapes import Rectangle, Circle
from rich2d.elements.grid import Grid, GridElement
from rich2d.sprites import Text
from rich2d.handlers import KeyboardHandler
from game import ScoreElement, SnakeModel, GameLogicElement


def snake_play_screen(window_width, window_height):
    play_rows = 20
    play_columns = 20
    play_grid = Grid(rect=(0, 0, window_width, window_height - 100), rows=play_rows, columns=play_columns)
    play_state = State(value="play")

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
    top_instructions_text = Text(text="Use the arrow keys", rect=(0, 0, 0, 0), colour="black",
                                 font_name="courier", font_size=28,
                                 horizontal_alignment=Text.HorizontalAlignment.LEFT)
    top_instructions_text_grid_element = GridElement(sprite=top_instructions_text, grid=status_grid,
                                                     grid_tiles=(9, 0, 10, 1))
    bottom_instructions_text = Text(text="to move the snake", rect=(0, 0, 0, 0), colour="black",
                                    font_name="courier", font_size=28,
                                    horizontal_alignment=Text.HorizontalAlignment.LEFT)
    bottom_instructions_text_grid_element = GridElement(sprite=bottom_instructions_text, grid=status_grid,
                                                        grid_tiles=(9, 1, 10, 1))

    top_game_over_text = Text(text="Game Over", rect=(0, 0, 0, 0), colour="black",
                              font_name="courier", font_size=28, font_bold=True,
                              horizontal_alignment=Text.HorizontalAlignment.LEFT)
    top_game_over_text_grid_element = GridElement(sprite=top_game_over_text, grid=status_grid,
                                                  grid_tiles=(9, 0, 10, 1))
    bottom_game_over_text = Text(text="Press spacebar to play again", rect=(0, 0, 0, 0), colour="black",
                                 font_name="courier", font_size=18,
                                 horizontal_alignment=Text.HorizontalAlignment.LEFT)
    bottom_game_over_text_grid_element = GridElement(sprite=bottom_game_over_text, grid=status_grid,
                                                     grid_tiles=(9, 1, 10, 1))

    snake_model = SnakeModel(play_grid=play_grid)
    snake_model.start_game()
    boundary_tiles_list = tuple([top_boundary_element.get_grid_tiles(), left_boundary_element.get_grid_tiles(),
                                 right_boundary_element.get_grid_tiles(), bottom_boundary_element.get_grid_tiles()])
    game_logic_element = GameLogicElement(play_grid=play_grid, play_state=play_state,
                                          snake_model=snake_model,
                                          boundary_tiles_list=boundary_tiles_list,
                                          food_tile=food_element.get_grid_tiles(),
                                          score_element=score_sync_element)

    play_sprites = [play_background, top_boundary, left_boundary, right_boundary, bottom_boundary,
                    score_label_text, score_text, top_instructions_text, bottom_instructions_text, food_sprite]
    play_elements = [play_background_element, top_boundary_element, left_boundary_element,
                     right_boundary_element, bottom_boundary_element, food_element,
                     score_label_grid_element, score_text_grid_element, game_logic_element, score_sync_element,
                     top_instructions_text_grid_element, bottom_instructions_text_grid_element]
    play_handlers = []
    play_model = ModelGroup(models=[Model(sprites=play_sprites, elements=play_elements, handlers=play_handlers),
                                    snake_model])
    game_over_sprites = [play_background, top_boundary, left_boundary, right_boundary, bottom_boundary,
                         score_label_text, score_text, top_game_over_text, bottom_game_over_text, food_sprite]
    game_over_elements = [play_background_element, top_boundary_element, left_boundary_element,
                          right_boundary_element, bottom_boundary_element, food_element,
                          score_label_grid_element, score_text_grid_element, score_sync_element,
                          top_game_over_text_grid_element, bottom_game_over_text_grid_element]

    def handle_spacebar():
        game_logic_element.new_game()
        return

    key_pressed_map = {pygame.K_SPACE: handle_spacebar}
    game_over_handlers = [KeyboardHandler(key_pressed_map=key_pressed_map)]
    game_over_model = ModelGroup(models=[Model(sprites=game_over_sprites, elements=game_over_elements,
                                               handlers=game_over_handlers), snake_model])
    state_map = {'play': play_model, 'game_over': game_over_model}
    return StateModel(state=play_state, state_map=state_map)
