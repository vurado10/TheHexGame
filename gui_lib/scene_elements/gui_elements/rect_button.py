from gui_lib.figures.rectangle import Rectangle
from gui_lib.painters.rectangle_painter import RectanglePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from pygame.math import Vector2


class RectButton(AbstractButton):
    def __init__(self,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 bg_color: RgbColor,
                 text_color: RgbColor,
                 text: str = ""):
        super().__init__(position,
                         Rectangle(position, width_px, height_px),
                         RectanglePainter(bg_color, bg_color, bg_color, 1.0))

        self._label.set_font_color(text_color)
        self.set_text(text)

    def set_text(self, text):
        self._label.set_text(text)
        self._label.position = (self
                                ._figure
                                .get_centered_position(self._label.width,
                                                       self._label.height))

    @property
    def height(self) -> int:
        return self._figure.height

    @property
    def width(self) -> int:
        return self._figure.width
