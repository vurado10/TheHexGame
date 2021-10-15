import math
from gui_lib.figures.figure import Figure
from pygame.math import Vector2


class Hexagon(Figure):
    def __init__(self,
                 center: Vector2,
                 radius: float,
                 rotation_radians: float):
        self.__center = center
        self.__radius = radius
        self.__rotation_radians = rotation_radians

    @property
    def center(self):
        return Vector2(self.__center)

    @center.setter
    def center(self, value):
        self.__center = Vector2(value)

    @property
    def vertexes(self):
        normalized_vertexes = \
            self.__get_normalized_vertexes(self.__rotation_radians)

        return [
            self.__center + self.__radius * vertex
            for vertex in normalized_vertexes
        ]

    def scale(self, factor: float):
        return Hexagon(self.__center,
                       self.__radius * factor,
                       self.__rotation_radians)

    def rotate(self, radians: float):
        return Hexagon(self.__center,
                       self.__radius,
                       self.__rotation_radians + radians)

    def translate(self, offset: Vector2):
        return Hexagon(self.__center + offset,
                       self.__radius,
                       self.__rotation_radians)

    # def get_box(self):
    #     vertexes = self.vertexes
    #     vertexes_sorted_by_x = sorted(vertexes,
    #                                   key=lambda v: v.x)
    #     min_x, max_x = (vertexes_sorted_by_x[0], vertexes_sorted_by_x[-1])
    #
    #     vertexes_sorted_by_y = sorted(vertexes,
    #                                   key=lambda v: v.y)
    #     min_y, max_y = (vertexes_sorted_by_y[0], vertexes_sorted_by_y[-1])
    #     return Rectangle()

    @staticmethod
    def __get_normalized_vertexes(rotation_angle_radians: float):
        normalized_vertexes = []

        for k in range(1, 7):
            angle = math.pi * k / 3 + rotation_angle_radians
            vertex = Vector2(math.cos(angle), -math.sin(angle))

            normalized_vertexes.append(vertex)

        return normalized_vertexes
