from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from pygame.math import Vector2
from pygame.surface import Surface


class GameOverScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(RgbColors.DARK_BLUE)
        self.__label = Label("Game Over")
        self.__label.position = Vector2(480, 270)
        self.__label.label_builder.set_text("Game Over")
        self.__label.label_builder.set_font_color(RgbColors.DARK_GREEN)
        self.__label.label_builder.set_font_size(36)

        self.add_gui_element(self.__label)
