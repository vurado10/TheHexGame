import pygame
from gui_lib.figures.described_figure import DescribedFigure
from gui_lib.figures.figure import Figure
from gui_lib.painters.painter import Painter
from gui_lib.rgb_color import RgbColor
from pygame import Surface
from pygame.math import Vector2


class DescribedFigurePainter(Painter):
    def __init__(self,
                 bg_color: RgbColor,
                 border_color: RgbColor,
                 fill_color: RgbColor,
                 padding_factor: float):
        super().__init__(bg_color, border_color, fill_color, padding_factor)

    def draw(self, surface: Surface, figure: Figure, is_filled: bool) -> None:
        if not isinstance(figure, DescribedFigure):
            raise Exception("figure must be DescribedFigure")

        self.__draw_with_filling(surface,
                                 figure.center,
                                 figure.vertexes,
                                 self._bg_color)
        self.__draw_border(surface, figure.vertexes)

        if is_filled:
            inner_figure = figure.scale(self._padding_factor)

            self.__draw_with_filling(surface,
                                     inner_figure.center,
                                     inner_figure.vertexes,
                                     self._fill_color)

    def __draw_border(self, surface: Surface, vertexes) -> None:
        pygame.draw.aalines(surface,
                            self._border_color.convert_to_tuple(),
                            True,
                            vertexes)

    @staticmethod
    def __draw_with_filling(surface: Surface,
                            center: Vector2,
                            vertexes,
                            color: RgbColor) -> None:
        length = len(vertexes)
        for index in range(1, length + 1):
            polygon_vertexes = [
                vertexes[(index - 1) % length],
                vertexes[index % length],
                center
            ]

            pygame.draw.polygon(surface,
                                color.convert_to_tuple(),
                                polygon_vertexes)

