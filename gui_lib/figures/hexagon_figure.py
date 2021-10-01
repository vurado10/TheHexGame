import math
from gui_lib.figures.figure import Figure
from pygame.math import Vector2


class HexagonFigure(Figure):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float):
        super(HexagonFigure, self).__init__(center, size, rotation_radians)

        if self._size.x != self._size.y:
            raise Exception(f"Hexagon size.x must be equal to "
                            f"size.y, but size: {self._size}")

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
        pass

    def rotate(self, radians: float):
        pass

    def translate(self, offset: Vector2):
        pass

    @staticmethod
    def __get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes