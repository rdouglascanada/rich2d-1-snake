from rich2d.game import Game, GameConfig
from title_model import SnakeTitleModel

window_width = 600
window_height = 700
snake_config = GameConfig(window_width=window_width, window_height=window_height,
                          window_title="Snake", background_colour="white")

title_model = SnakeTitleModel(window_width, window_height)
snake_game = Game(model=title_model, config=snake_config)
snake_game.run()
