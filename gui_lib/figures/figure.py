from abc import ABC
from abcmeta import abstractmethod
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
    @abstractmethod
    def vertexes(self):
        return [Vector2()]

    def is_point_inside(self, point: Vector2) -> bool:
        pass

    @abstractmethod
    def scale(self, factor: float):
        pass

    @abstractmethod
    def rotate(self, radians: float):
        pass

    @abstractmethod
    def translate(self, offset: Vector2):
        pass
