import random
import time
from rich2d.elements import Element
from rich2d.elements.grid import GridTiles


class GameLogicElement(Element):
    UPDATE_INTERVAL = 0.25

    def __init__(self, play_state=None, play_grid=None, snake_model=None,
                 boundary_tiles_list=None, food_tile=None, score_element=None):
        if play_state is None:
            raise RuntimeError("GameLogicElement play_state cannot be None")
        if play_grid is None:
            raise RuntimeError("GameLogicElement play_grid cannot be None")
        if snake_model is None:
            raise RuntimeError("GameLogicElement snake_model cannot be None")
        if boundary_tiles_list is None:
            raise RuntimeError("GameLogicElement boundary_tiles_list cannot be None")
        if food_tile is None:
            raise RuntimeError("GameLogicElement food_tile cannot be None")
        if score_element is None:
            raise RuntimeError("GameLogicElement score_element cannot be None")

        self._play_state = play_state
        self._play_grid = play_grid
        self._snake_model = snake_model
        self._boundary_tiles_list = boundary_tiles_list
        self._food_tile = food_tile
        self._score_element = score_element
        self._update_timestamp = time.time()
        return

    def new_game(self):
        self._play_state.set_value("play")
        self._snake_model.start_game()
        self._place_food_tile()
        self._score_element.set_score(0)
        self._update_timestamp = time.time()
        return

    def update(self):
        if self._play_state.get_value() == "game_over":
            return

        current_time = time.time()
        if current_time - self._update_timestamp >= GameLogicElement.UPDATE_INTERVAL:
            self._update_timestamp = current_time
            tile_in_front_of_snake = GridTiles(values=self._snake_model.get_tile_in_front())
            for boundary_tiles in self._boundary_tiles_list:
                if boundary_tiles.collides_with(tile_in_front_of_snake):
                    self._play_state.set_value("game_over")
                    return
            if self._snake_model.collides_with(tile_in_front_of_snake):
                self._play_state.set_value("game_over")
                return
            if self._food_tile.collides_with(tile_in_front_of_snake):
                self._snake_model.grow()
                self._score_element.set_score(self._score_element.get_score() + 1)
                self._place_food_tile()
            else:
                self._snake_model.move()
        return

    def _place_food_tile(self):
        self._food_tile.set_x_index(random.randint(1, self._play_grid.get_columns() - 2))
        self._food_tile.set_y_index(random.randint(1, self._play_grid.get_columns() - 2))
        while self._snake_model.collides_with(self._food_tile):
            self._food_tile.set_x_index(random.randint(1, self._play_grid.get_columns() - 2))
            self._food_tile.set_y_index(random.randint(1, self._play_grid.get_columns() - 2))
        return
