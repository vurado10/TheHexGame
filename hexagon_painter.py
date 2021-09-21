import pygame
import math
from painter import Painter
from pygame.math import Vector2
from rgb_color import RgbColor


class HexagonPainter(Painter):
    def __init__(self,
                 surface: pygame.Surface,
                 padding: int,
                 border_color: RgbColor,
                 fill_color: RgbColor):
        self._surface = surface
        self._padding = padding
        self._border_color = border_color
        self._fill_color = fill_color

    @staticmethod
    def _get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes

    def draw(self,
             center: Vector2,
             radius: int,
             rotation_angle_radians: float) -> None:

        normalized_vertexes = \
            self._get_normalized_vertexes(rotation_angle_radians)

        border_vertexes = [
            center
            + radius * vertex for vertex in normalized_vertexes
        ]

        inside_border_vertexes = [
            center + (radius - self._padding) * vertex
            for vertex in normalized_vertexes
        ]

        self._draw_without_filling(border_vertexes)
        self._draw_with_filling(center, inside_border_vertexes)

    def _draw_without_filling(self, vertexes) -> None:
        pygame.draw.aalines(self._surface,
                            self._border_color.convert_to_tuple(),
                            True,
                            vertexes)

    def _draw_with_filling(self, center: Vector2, vertexes) -> None:
        length = len(vertexes)
        for index in range(1, length + 1):
            polygon_vertexes = [
                vertexes[(index - 1) % length],
                vertexes[index % length],
                center
            ]

            pygame.draw.polygon(self._surface,
                                self._fill_color.convert_to_tuple(),
                                polygon_vertexes)
