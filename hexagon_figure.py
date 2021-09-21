import math
from figure import Figure
from hexagon_painter import HexagonPainter
from pygame.math import Vector2


class HexagonFigure(Figure):
    def __init__(self,
                 center: Vector2,
                 radius: int,
                 rotation_angle_radians: float,
                 painter: HexagonPainter):
        if not isinstance(painter, HexagonPainter):
            raise Exception("painter must be an instance of HexagonPainter")

        self._painter = painter
        self._center = center
        self._radius = radius
        self._rotation_angle_radians = rotation_angle_radians

        self._border_vertexes = self.vertexes

    @property
    def vertexes(self):
        normalized_vertexes = \
            self._get_normalized_vertexes(self._rotation_angle_radians)

        return [
            self._center + self._radius * vertex
            for vertex in normalized_vertexes
        ]

    @property
    def center(self):
        return Vector2(self._center)

    def start_painter(self, is_filled: bool) -> None:
        self._painter.draw(self, is_filled)

    def transform(self, translate_vector: Vector2, scale_factor: float,
                  rotate_angle_radians: float):
        return HexagonFigure(self._center + translate_vector,
                             int(self._radius * scale_factor),
                             self._rotation_angle_radians
                             + rotate_angle_radians,
                             self._painter)

    def is_point_inside(self, point: Vector2) -> bool:
        length = len(self._border_vertexes)
        for index in range(1, length + 1):
            point1 = self._border_vertexes[(index - 1) % length]
            point2 = self._border_vertexes[index % length]

            (r, s) = point2 - point1

            if s * (point.x - point1.x) - r * (point.y - point1.y) < 0:
                return False

        return True

    @staticmethod
    def _get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes
