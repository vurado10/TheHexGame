import pygame.draw
from gui_lib.figures.rectangle import Rectangle
from gui_lib.painters.painter import Painter
from gui_lib.rgb_color import RgbColor
from pygame import Surface


class RectanglePainter(Painter):
    def __init__(self,
                 bg_color: RgbColor,
                 border_color: RgbColor,
                 fill_color: RgbColor,
                 padding_factor: float):
        super().__init__(bg_color, border_color, fill_color, padding_factor)

    def draw(self, surface: Surface, figure: Rectangle) -> None:
        self.__draw_with_filling(surface,
                                 figure.vertexes,
                                 self._bg_color)

        self._draw_border(surface, figure.vertexes)

        inner_figure = figure.scale(self._padding_factor)
        self.__draw_with_filling(surface,
                                 inner_figure.vertexes,
                                 self._fill_color)

    @staticmethod
    def __draw_with_filling(surface: Surface,
                            vertexes,
                            color: RgbColor) -> None:
        length = len(vertexes)
        for index in [0, 2]:
            polygon_vertexes = [
                vertexes[index],
                vertexes[(index + 1) % length],
                vertexes[(index + 2) % length]
            ]

            pygame.draw.polygon(surface,
                                tuple(color),
                                polygon_vertexes)
