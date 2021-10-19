from typing import List
from gui_lib.figures.figure import Figure
from pygame.math import Vector2


class Rectangle(Figure):
    def __init__(self, position: Vector2, width_px: int, height_px: int):
        self.__position = Vector2(position)
        self.__width_px = width_px
        self.__height_px = height_px

    @property
    def vertexes(self) -> List[Vector2]:
        return [
            self.__position,
            self.__position + self.height_vector,
            self.__position + self.height_vector + self.width_vector,
            self.__position + self.width_vector
        ]

    @property
    def width_vector(self):
        return Vector2(self.__width_px, 0)

    @property
    def height_vector(self):
        return Vector2(0, self.__height_px)

    @property
    def width(self) -> int:
        return self.__width_px

    @property
    def height(self) -> int:
        return self.__height_px

    @property
    def position(self):
        return Vector2(self.__position)

    @position.setter
    def position(self, value: Vector2):
        self.__position = Vector2(value)

    def get_relative_centered_position(self,
                                       element_width,
                                       element_height) -> Vector2:
        return Vector2((self.width - element_width) / 2,
                       (self.height - element_height) / 2)

    def scale(self, factor):
        return Rectangle(self.__position,
                         self.__width_px * factor,
                         self.__height_px * factor)

    def transform(self, transformer):
        transformer.transform(self)
