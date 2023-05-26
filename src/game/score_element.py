from rich2d.elements import Element


class ScoreElement(Element):
    def __init__(self, score_text_sprite=None,  score=0):
        if score_text_sprite is None:
            raise RuntimeError("ScoreElement score_text_sprite cannot be None")
        self._score_text_sprite = score_text_sprite
        self._score = score
        return

    def update(self):
        self._score_text_sprite.set_text(str(self._score))
        return

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score
        return
