import pygame
from enum import Enum
from rich2d.models import Model
from rich2d.sprites.shapes import Rectangle
from rich2d.elements.grid import GridElement, GridTiles
from rich2d.handlers import KeyboardHandler


class SnakeModel(Model):
    class Direction(Enum):
        UP = 1
        DOWN = 2
        LEFT = 3
        RIGHT = 4

    def __init__(self, play_grid=None):
        if play_grid is None:
            raise RuntimeError("SnakeModel play_grid cannot be None")
        self._play_grid = play_grid
        self._direction = SnakeModel.Direction.RIGHT
        self._sprites = []
        self._elements = []

        def handle_up_arrow():
            if self._direction != SnakeModel.Direction.DOWN:
                self._direction = SnakeModel.Direction.UP
            return

        def handle_down_arrow():
            if self._direction != SnakeModel.Direction.UP:
                self._direction = SnakeModel.Direction.DOWN
            return

        def handle_left_arrow():
            if self._direction != SnakeModel.Direction.RIGHT:
                self._direction = SnakeModel.Direction.LEFT
            return

        def handle_right_arrow():
            if self._direction != SnakeModel.Direction.LEFT:
                self._direction = SnakeModel.Direction.RIGHT
            return

        key_pressed_map = {pygame.K_UP: handle_up_arrow,
                           pygame.K_DOWN: handle_down_arrow,
                           pygame.K_LEFT: handle_left_arrow,
                           pygame.K_RIGHT: handle_right_arrow}

        self._keyboard_handler = KeyboardHandler(key_pressed_map=key_pressed_map)
        return

    def start_game(self):
        initial_sprite = Rectangle(rect=(0, 0, 0, 0), colour="green")
        self._sprites = [initial_sprite]
        head_element = GridElement(sprite=initial_sprite,
                                   grid=self._play_grid,
                                   grid_tiles=(1, self._play_grid.get_rows() // 2, 1, 1))
        self._elements = [head_element]
        self._direction = SnakeModel.Direction.RIGHT
        self.grow()
        self.move()
        return

    def get_tile_in_front(self):
        head_tile = self._elements[len(self._elements) - 1].get_grid_tiles()
        if self._direction == SnakeModel.Direction.RIGHT:
            tile_in_front = GridTiles(values=(head_tile.get_x_index() + 1, head_tile.get_y_index(), 1, 1))
        elif self._direction == SnakeModel.Direction.LEFT:
            tile_in_front = GridTiles(values=(head_tile.get_x_index() - 1, head_tile.get_y_index(), 1, 1))
        elif self._direction == SnakeModel.Direction.UP:
            tile_in_front = GridTiles(values=(head_tile.get_x_index(), head_tile.get_y_index() - 1, 1, 1))
        elif self._direction == SnakeModel.Direction.DOWN:
            tile_in_front = GridTiles(values=(head_tile.get_x_index(), head_tile.get_y_index() + 1, 1, 1))
        else:
            raise RuntimeError(f"SnakeModel get_tile_in_front(): Unexpected value for direction {self._direction}")
        return tile_in_front

    def grow(self):
        tile_in_front = self.get_tile_in_front()
        new_sprite = Rectangle(rect=(0, 0, 0, 0), colour="green")
        new_element = GridElement(sprite=new_sprite, grid=self._play_grid, grid_tiles=tile_in_front)
        self._sprites.append(new_sprite)
        self._elements.append(new_element)
        return

    def move(self):
        tile_in_front = self.get_tile_in_front()
        tail_tip_sprite = self._sprites.pop(0)
        tail_tip_element = self._elements.pop(0)
        tail_tip_tiles = tail_tip_element.get_grid_tiles()
        tail_tip_tiles.set_x_index(tile_in_front.get_x_index())
        tail_tip_tiles.set_y_index(tile_in_front.get_y_index())

        self._sprites.append(tail_tip_sprite)
        self._elements.append(tail_tip_element)
        return

    def collides_with(self, grid_tiles):
        collides = False
        for element in self._elements:
            if element.get_grid_tiles().collides_with(grid_tiles):
                collides = True
                break
        return collides

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction
        return

    def get_sprites(self):
        return tuple(self._sprites)

    def get_elements(self):
        return tuple(self._elements)

    def get_handlers(self):
        return tuple([self._keyboard_handler])

