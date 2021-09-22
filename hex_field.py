import pygame
from button import Button
from cell_states import CellStates
from hexagon_figure import HexagonFigure
from hexagon_painter import HexagonPainter
from pygame.math import Vector2
from rgb_color import RgbColor
from rgb_colors import RgbColors


class HexField:
    def __init__(self,
                 surface: pygame.Surface,
                 width,
                 height,
                 border_color: RgbColor,
                 background_color: RgbColor,
                 player_color1: RgbColor,
                 player_color2: RgbColor):
        self._surface = surface
        self._width = width
        self._height = height
        self._border_color = border_color
        self._background_color = background_color
        self._player_color1 = player_color1
        self._player_color2 = player_color2
        self.controls = [] # tmp to delete

        self._cells = []
        for i in range(self._width):
            self._cells.append([])
            for j in range(self._height):
                self._cells[i].append(CellStates.NEUTRAL)

    def show(self):
        surface_width = self._surface.get_width()
        surface_height = self._surface.get_height()
        radius = min(surface_height / (2 + 3 * (self._height - 1) / 2),
                     2 * surface_width / (
                                 3 ** (1 / 2) * (3 * self._width - 1)))
        h = round(radius * 3 ** (1 / 2) / 2)
        radius = round(radius)

        figure_painter = HexagonPainter(self._surface,
                                        0.8,
                                        RgbColors.WHITE,
                                        RgbColors.BLACK,
                                        RgbColors.WHITE)
        last_center = Vector2(h, radius)
        for i in range(self._height):
            for j in range(self._width):
                f = HexagonFigure(last_center,
                                  radius,
                                  11.0,
                                  figure_painter)
                self.controls.append(Button(f))

                self.controls[-1].on_click_function = \
                    lambda b: b.switch_state()
                last_center += Vector2(2 * h, 0)
            last_center = Vector2(h * (i + 2), last_center.y + 3 * radius / 2)
