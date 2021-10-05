from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.label import Label
from pygame.math import Vector2
from pygame.surface import Surface


class GameOverScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(RgbColors.DARK_BLUE)
        self.__label = Label(RectangleFigure(Vector2(480, 270),
                                             Vector2(),
                                             0.0),
                             [DescribedFigurePainter(
                                 self._bg_color,
                                 self._bg_color,
                                 self._bg_color,
                                 1.0)])
        self.__label.label_builder.set_text("Game Over")
        self.__label.label_builder.set_font_color(RgbColors.DARK_GREEN)
        self.__label.label_builder.set_font_size(36)

        self.add_gui_element(self.__label)
