from rich2d.models import Model
from rich2d.sprites.shapes import Rectangle
from rich2d.elements.grid import GridElement


class SnakeModel(Model):
    def __init__(self, play_grid=None):
        if play_grid is None:
            raise RuntimeError("SnakeModel play_grid cannot be None")
        initial_sprite = Rectangle(rect=(0, 0, 0, 0), colour="green")
        self._play_grid = play_grid
        self._sprites = [initial_sprite]
        self._elements = [GridElement(sprite=initial_sprite,
                                      grid=play_grid, grid_tiles=(1, 9, 1, 1))]
        return

    def reset(self):
        initial_sprite = Rectangle(rect=(0, 0, 0, 0), colour="green")
        self._sprites = [initial_sprite]
        self._elements = [GridElement(sprite=initial_sprite,
                                      grid=self._play_grid, grid_tiles=(1, 9, 1, 1))]
        return

    def get_sprites(self):
        return tuple(self._sprites)

    def get_elements(self):
        return tuple(self._elements)

    def get_handlers(self):
        return tuple([])
