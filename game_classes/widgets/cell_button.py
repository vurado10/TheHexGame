from gui_lib.figures.hexagon_figure import Hexagon
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from pygame.math import Vector2
from pygame.surface import Surface


class CellButton(AbstractButton):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float,
                 position: Vector2 = None):
        super().__init__(Vector2(0, 0) if position is None else position,
                         Hexagon(center, size.x, rotation_radians),
                         HexagonPainter(RgbColors.BLACK,
                                        RgbColors.BLACK,
                                        RgbColors.BLACK, 1.0))
        self._figure.center += self.position

    @property
    def center(self):
        return self._figure.center

    def set_painter(self, painter: HexagonPainter):
        self._figure_painter = painter

    def update_self_on(self, surface: Surface):
        self._figure_painter.draw(surface, self._figure)
