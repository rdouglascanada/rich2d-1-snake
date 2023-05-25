from rich2d.game import Game, GameConfig

snake_config = GameConfig(window_width=600, window_height=700,
                          window_title="Snake", background_colour="black")
snake_game = Game(config=snake_config)
snake_game.run()
