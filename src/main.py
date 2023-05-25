from rich2d.game import Game, GameConfig
from rich2d.models import Model
from rich2d.models.state import State, StateModel
from title_model import SnakeTitleModel

window_width = 600
window_height = 700
game_config = GameConfig(window_width=window_width, window_height=window_height,
                         window_title="Snake", background_colour="white")

game_state = State(value="title")
title_model = SnakeTitleModel(game_state, window_width, window_height)

game_state_map = {'title': title_model, 'play': Model()}
game_model = StateModel(state=game_state, state_map=game_state_map)

snake_game = Game(model=game_model, config=game_config)
snake_game.run()
