from gui_lib.rgb_color import RgbColor


class PlayerProfile:
    def __init__(self,
                 name: str,
                 color: RgbColor):
        self.name = name
        self.color = color
