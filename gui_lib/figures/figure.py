from abc import ABC, abstractmethod
from typing import List
from pygame.math import Vector2


class Figure(ABC):
    @property
    @abstractmethod
    def vertexes(self) -> List[Vector2]:
        """vertexes counterclockwise"""
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

    def transform(self, transformer):
        pass
