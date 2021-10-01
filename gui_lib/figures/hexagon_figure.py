import math
from gui_lib.figures.described_figure import DescribedFigure
from pygame.math import Vector2


class HexagonFigure(DescribedFigure):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float):
        super(HexagonFigure, self).__init__(center, size, rotation_radians)

        self.__radius = self._size.x

    @property
    def vertexes(self):
        normalized_vertexes = \
            self.__get_normalized_vertexes(self._rotation_radians)

        return [
            self._center + self.__radius * vertex
            for vertex in normalized_vertexes
        ]

    def scale(self, factor: float):
        return HexagonFigure(self._center,
                             Vector2(self._size.x * factor,
                                     self._size.y * factor),
                             self._rotation_radians)

    def rotate(self, radians: float):
        return HexagonFigure(self._center,
                             self._size,
                             self._rotation_radians + radians)

    def translate(self, offset: Vector2):
        return HexagonFigure(self._center + offset,
                             self._size,
                             self._rotation_radians)

    @staticmethod
    def __get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes