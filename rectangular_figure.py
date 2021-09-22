from figure import Figure
from pygame.math import Vector2
from rectangular_painter import RectangularPainter


class RectangularFigure(Figure):
    def __init__(self,
                 center: Vector2,
                 width: int,
                 height: int,
                 painter: RectangularPainter):
        self.change_painter(painter)

        self._center = Vector2(center)
        self._width = width
        self._height = height
        self._border_vertexes = self.vertexes

    @property
    def vertexes(self):
        half_width, half_height = round(self._width / 2), round(self._height / 2)

        return [
            self._center + Vector2(-half_width, half_height),
            self._center + Vector2(-half_width, -half_height),
            self._center + Vector2(half_width, -half_height),
            self._center + Vector2(half_width, half_height)
        ]

    @property
    def center(self):
        return self._center

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

    def transform(self,
                  translate_vector: Vector2,
                  scale_factor: float,
                  rotate_angle_radians: float):
        pass

    def change_painter(self, painter):
        self._painter = painter
