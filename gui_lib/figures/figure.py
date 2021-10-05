from abc import ABC, abstractmethod
from typing import List
from pygame.math import Vector2


class Figure(ABC):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float):
        """
        size - размеры (радиусы) ограничивающего эллипса.
        center - центер описанного эллипса.
        size и center имеют целочисленность координат.
        """
        self._center = Vector2(center)
        self._size = Vector2(size)
        self._rotation_radians = rotation_radians

    @property
    def center(self):
        return Vector2(self._center)

    @center.setter
    def center(self, point: Vector2):
        self._center = Vector2(point)

    @property
    @abstractmethod
    def vertexes(self) -> List[Vector2]:
        return []

    def is_point_inside(self, point: Vector2) -> bool:
        border_vertexes = self.vertexes
        length = len(border_vertexes)
        for index in range(1, length + 1):
            point1 = border_vertexes[(index - 1) % length]
            point2 = border_vertexes[index % length]

            (r, s) = point2 - point1

            if s * (point.x - point1.x) - r * (point.y - point1.y) < 0:
                return False

        return True

    @abstractmethod
    def scale(self, factor: float):
        pass

    @abstractmethod
    def rotate(self, radians: float):
        pass

    @abstractmethod
    def translate(self, offset: Vector2):
        pass
