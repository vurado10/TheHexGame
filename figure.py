import copy
from abc import ABC, abstractmethod
from figure_size import FigureSize
from painter import Painter
from pygame.math import Vector2


class Figure(ABC):
    def __init__(self,
                 center: Vector2,
                 size: FigureSize,
                 painter: Painter):
        self._center = Vector2(center)
        self._size = size
        self._painter = painter
        self._border_vertexes = self.get_vertexes(center, size)

    @abstractmethod
    def get_vertexes(self, center: Vector2, size: FigureSize):
        pass

    @property
    def border_vertexes(self):
        return self._border_vertexes

    @property
    def center(self):
        return Vector2(self._center)

    def is_point_inside(self, point: Vector2) -> bool:
        length = len(self._border_vertexes)
        for index in range(1, length + 1):
            point1 = self._border_vertexes[(index - 1) % length]
            point2 = self._border_vertexes[index % length]

            (r, s) = point2 - point1

            if s * (point.x - point1.x) - r * (point.y - point1.y) < 0:
                return False

        return True

    def start_painter(self, is_filled: bool) -> None:
        self._painter.draw(self, is_filled)

    @abstractmethod
    def transform(self,
                  translate_vector: Vector2,
                  scale_factor: float,
                  rotate_angle_radians: float):
        pass
