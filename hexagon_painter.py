import pygame
from figure import Figure
from painter import Painter
from pygame.math import Vector2
from rgb_color import RgbColor


class HexagonPainter(Painter):
    def __init__(self,
                 surface: pygame.Surface,
                 padding_factor: float,
                 border_color: RgbColor,
                 background_color: RgbColor,
                 fill_color: RgbColor):
        self._surface = surface
        self._padding_factor = padding_factor
        self._border_color = border_color
        self._background_color = background_color
        self._fill_color = fill_color

    def draw(self, hexagon: Figure, is_filled: bool) -> None:
        self._draw_with_filling(hexagon.center,
                                hexagon.get_vertexes(hexagon.center, hexagon._size),
                                self._background_color)
        self._draw_without_filling(hexagon.get_vertexes(hexagon.center, hexagon._size))

        if is_filled:
            inner_hexagon = hexagon.transform(Vector2(),
                                              self._padding_factor,
                                              0.0)
            self._draw_with_filling(inner_hexagon.center,
                                    inner_hexagon.get_vertexes(inner_hexagon.center, inner_hexagon._size),
                                    self._fill_color)

    def _draw_without_filling(self, vertexes) -> None:
        pygame.draw.aalines(self._surface,
                            self._border_color.convert_to_tuple(),
                            True,
                            vertexes)

    def _draw_with_filling(self,
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

            pygame.draw.polygon(self._surface,
                                color.convert_to_tuple(),
                                polygon_vertexes)
