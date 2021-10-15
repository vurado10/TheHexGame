import pygame
from typing import List
from game_classes.color_theme import SCENE_BG_COLOR
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.math import Vector2
from pygame.surface import Surface


class Line(Widget):
    def __init__(self,
                 points: List[Vector2],
                 color: RgbColor,
                 width: float = 5.0):
        super().__init__(Vector2(0, 0))

        self._points = list(map(lambda v: Vector2(v), points))
        self._color = color
        self._width = round(width)

    def update_self_on(self, surface: Surface):
        pygame.draw.lines(surface,
                          tuple(self._color),
                          False,
                          self._points,
                          width=self._width)
