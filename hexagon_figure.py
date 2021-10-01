import math
from figure import Figure
from hexagon_painter import HexagonPainter
from pygame.math import Vector2
from radius_size import RadiusSize


class HexagonFigure(Figure):
    def __init__(self,
                 center: Vector2,
                 radius: int,
                 rotation_angle_radians: float,
                 painter: HexagonPainter):
        super(HexagonFigure, self).__init__(center,
                                            RadiusSize(radius,
                                                       rotation_angle_radians),
                                            painter)

    def get_vertexes(self, center, size: RadiusSize):

        normalized_vertexes = \
            self._get_normalized_vertexes(size.rotation_angle_radians)

        return [
            center + size.radius * vertex
            for vertex in normalized_vertexes
        ]

    @property
    def center(self):
        return Vector2(self._center)

    def transform(self,
                  translate_vector: Vector2,
                  scale_factor: float,
                  rotate_angle_radians: float):
        current_radius, current_angle = \
            self._size.radius, self._size.rotation_angle_radians
        return HexagonFigure(self.center + translate_vector,
                             int(current_radius * scale_factor),
                             current_angle
                             + rotate_angle_radians,
                             self._painter)

    @staticmethod
    def _get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes
