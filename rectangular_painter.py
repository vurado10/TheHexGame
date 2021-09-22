import pygame
from figure import Figure
from painter import Painter
from rgb_color import RgbColor


class RectangularPainter(Painter):
    def __init__(self,
                 surface: pygame.Surface,
                 color: RgbColor):
        self._surface = surface
        self._color = color

    def draw(self, figure: Figure, is_filled: bool):
        vertexes = figure.vertexes
        length = len(vertexes)
        for index in range(1, length + 1):
            polygon_vertexes = [
                vertexes[(index - 1) % length],
                vertexes[index % length],
                figure.center
            ]

            pygame.draw.polygon(self._surface,
                                self._color.convert_to_tuple(),
                                polygon_vertexes)
