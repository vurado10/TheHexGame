import pygame
from gui_lib.figures.hexagon_figure import HexagonFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.scene_elements.button import Button
from pygame.math import Vector2


class CellButton(Button):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float,
                 painter: DescribedFigurePainter):
        super().__init__(HexagonFigure(center, size, rotation_radians),
                         [painter])

        self.label_builder.set_text("")

    def set_painter(self, painter: DescribedFigurePainter):
        self._states_painters[0] = painter
