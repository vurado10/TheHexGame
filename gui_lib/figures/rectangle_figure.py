from gui_lib.figures.described_figure import DescribedFigure
from pygame.math import Vector2


class RectangleFigure(DescribedFigure):
    """
    Прямоугольник. Между диагональю и одной из сторон угол pi / 6
    """

    def __init__(self,
                 center: Vector2,
                 size: Vector2,
                 rotation_radians: float):
        super().__init__(center, size, rotation_radians)

        self.__width = self._size.x * 3 ** (1 / 2)
        self._height = self._size.x

    @property
    def vertexes(self):
        half_width, half_height = self.__width / 2, self._height / 2

        return [
            self._center + Vector2(-half_width, -half_height),
            self._center + Vector2(-half_width, half_height),
            self._center + Vector2(half_width, half_height),
            self._center + Vector2(half_width, -half_height)
        ]

    def scale(self, factor: float):
        return RectangleFigure(self._center,
                               Vector2(self._size.x * factor,
                                       self._size.y * factor),
                               self._rotation_radians)

    def rotate(self, radians: float):
        return RectangleFigure(self._center,
                               self._size,
                               self._rotation_radians + radians)

    def translate(self, offset: Vector2):
        return RectangleFigure(self._center + offset,
                               self._size,
                               self._rotation_radians)
