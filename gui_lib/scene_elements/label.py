from typing import List

from gui_lib.figures.described_figure import DescribedFigure
from gui_lib.figures.figure import Figure
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.painters.painter import Painter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame.math import Vector2
from pygame.surface import Surface


class Label(GuiElement, TextElement):
    def __init__(self, figure: Figure, states_painters: List[Painter]):
        # BUG: figure - ограничивающая фигура, если её размер слишком мал,
        # то надпись будет неправильно отображаться при перерисовке"""

        GuiElement.__init__(self,
                            figure,
                            states_painters)
        TextElement.__init__(self)

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))

    @staticmethod
    def create(text,
               font_color=RgbColors.DARK_GREEN,
               font_size=20):
        label = Label(RectangleFigure(Vector2(), Vector2(), 0.0),
                      [DescribedFigurePainter(
                          RgbColors.DARK_BLUE,
                          RgbColors.DARK_BLUE,
                          RgbColors.DARK_BLUE,
                          1)])
        label.label_builder.set_font_size(font_size)
        label.label_builder.set_font_color(font_color)
        label.label_builder.set_text(text)

        return label
