import pygame.draw
from gui_lib.figures.stable_rectangle_figure import StableRectangleFigure
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.math import Vector2
from pygame.surface import Surface


class PolygonGuiElement(GuiElement):
    def __init__(self,
                 points: list[Vector2],
                 bg_color: RgbColor,
                 color: RgbColor):
        GuiElement.__init__(self,
                            StableRectangleFigure(Vector2(), Vector2(), 0.0),
                            [HexagonPainter(bg_color,
                                            bg_color,
                                            bg_color,
                                            1.0)])

        self._points = list(points)
        self._color = color

    def update_on(self, surface: Surface):
        pygame.draw.polygon(surface, tuple(self._color), self._points)
