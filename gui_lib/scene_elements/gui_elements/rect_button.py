from gui_lib.figures.rectangle import Rectangle
from gui_lib.painters.rectangle_painter import RectanglePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from pygame.math import Vector2
from pygame.surface import Surface


class RectButton(AbstractButton):
    def __init__(self, position: Vector2,
                 width_px: int, height_px: int,
                 bg_color: RgbColor, text_color: RgbColor,
                 text: str = ""):
        super().__init__(position,
                         Rectangle(position, width_px, height_px),
                         RectanglePainter(bg_color, bg_color, bg_color, 1.0))

        self._label.set_font_color(text_color)
        self._label.position += Vector2(10, 15)
        self._label.set_text(text)

    def update_self_on(self, surface: Surface):
        self._figure_painter.draw(surface, self._figure)
