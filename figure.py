from abc import ABC, abstractmethod
from pygame.math import Vector2


class Figure(ABC):
    @property
    @abstractmethod
    def vertexes(self):
        pass

    @property
    @abstractmethod
    def center(self):
        pass

    @abstractmethod
    def is_point_inside(self, point: Vector2) -> bool:
        pass

    @abstractmethod
    def start_painter(self, is_filled: bool) -> None:
        pass

    @abstractmethod
    def transform(self,
                  translate_vector: Vector2,
                  scale_factor: float,
                  rotate_angle_radians: float):
        pass
