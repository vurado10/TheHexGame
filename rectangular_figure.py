from figure import Figure
from pygame.math import Vector2
from rectangular_painter import RectangularPainter
from rectangular_size import RectangularSize


class RectangularFigure(Figure):
    def __init__(self,
                 center: Vector2,
                 width: int,
                 height: int,
                 painter: RectangularPainter):
        super(RectangularFigure, self).__init__(center,
                                                RectangularSize(width, height),
                                                painter)

    def get_vertexes(self, center, size):
        half_width, half_height = round(size.width / 2), round(size.height / 2)

        return [
            center + Vector2(-half_width, half_height),
            center + Vector2(-half_width, -half_height),
            center + Vector2(half_width, -half_height),
            center + Vector2(half_width, half_height)
        ]

    def transform(self,
                  translate_vector: Vector2,
                  scale_factor: float,
                  rotate_angle_radians: float):
        pass
