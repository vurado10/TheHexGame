from abc import ABC
from gui_lib.figures.figure import Figure
from pygame.math import Vector2


class DescribedFigure(Figure, ABC):
    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float):
        if not abs(size.x - size.y) < 1e-6:
            raise Exception(f"Hexagon size.x must be equal to "
                            f"size.y, but size: {size}")

        super().__init__(center, size, rotation_radians)

