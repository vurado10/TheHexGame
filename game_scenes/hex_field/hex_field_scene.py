from game_scenes.hex_field.hex_field_model import HexFieldModel
from gui_lib.scene import Scene
from pygame.surface import Surface


class HexFieldScene(Scene):
    def __init__(self, screen: Surface, model: HexFieldModel):
        super().__init__(screen)
