from abc import ABC, abstractmethod

from pygame.math import Vector2


class Painter(ABC):
    @abstractmethod
    def draw(self,
             center: Vector2,
             radius: int,
             rotation_angle_radians: float):
        pass
