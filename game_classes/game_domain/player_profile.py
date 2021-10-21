from gui_lib.rgb_color import RgbColor


class PlayerProfile:
    def __init__(self,
                 name: str,
                 color: RgbColor,
                 score: int = 0):
        self.name = name
        self.score = score

        # TODO: Delete
        self.color = color
