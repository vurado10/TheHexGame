import math
import pygame
from cell_states import CellStates
from gui_lib.figures.hexagon_figure import HexagonFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from pygame.math import Vector2


class HexField:
    def __init__(self,
                 scene: Scene,
                 width,
                 height,
                 border_color: RgbColor,
                 background_color: RgbColor,
                 player_color1: RgbColor,
                 player_color2: RgbColor):
        self.__scene = scene
        self._width = width
        self._height = height
        self._border_color = border_color
        self._background_color = background_color
        self._player_color1 = player_color1
        self._player_color2 = player_color2
        self.controls = []  # tmp to delete

        self._cells = []
        for i in range(self._width):
            self._cells.append([])
            for j in range(self._height):
                self._cells[i].append(CellStates.NEUTRAL)

    def show(self):
        surface_width, surface_height = self.__scene.size
        radius = min(surface_height / (2 + 3 * (self._height - 1) / 2),
                     2 * surface_width / (
                             3 ** (1 / 2) * (3 * self._width - 1)))
        h = round(radius * 3 ** (1 / 2) / 2)
        radius = round(radius)

        state_painter_1 = DescribedFigurePainter(RgbColors.BLACK,
                                                 RgbColors.WHITE,
                                                 RgbColors.WHITE,
                                                 0.8)
        state_painter_2 = DescribedFigurePainter(RgbColors.BLACK,
                                                 RgbColors.WHITE,
                                                 RgbColors.BLACK,
                                                 0.8)

        def click_func(bt, evt):
            nonlocal self
            bt.switch_to_next_state()
            bt.update_on(self._surface)

        last_center = Vector2(h, radius)
        for i in range(self._height):
            for j in range(self._width):
                f = HexagonFigure(last_center,
                                  Vector2(radius, radius),
                                  math.pi / 6)
                button = Button(f, [state_painter_2, state_painter_1])
                button.add_on_click(click_func)
                button.label_builder.set_text("button")
                button.label_builder.set_font_size(12)
                button.update_on(self._surface)

                self.controls.append(button)

                last_center += Vector2(2 * h, 0)
            last_center = Vector2(h * (i + 2), last_center.y + 3 * radius / 2)
