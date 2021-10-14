import math
import pygame.draw
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.math import Vector2
from pygame.surface import Surface


class ArrowGuiElement(GuiElement):
    def __init__(self,
                 point_from: Vector2,
                 vector: Vector2,
                 color: RgbColor,
                 bg_color: RgbColor):
        self.__vector = Vector2(vector)

        super().__init__(RectangleFigure(Vector2(), Vector2(), 0.0),
                         [DescribedFigurePainter(bg_color,
                                                 bg_color,
                                                 bg_color,
                                                 1)])
        self.__point_from = Vector2(point_from)
        self.__point_to = self.__point_from + self.__vector
        self.__color = color

    def update_on(self, surface: Surface):
        pygame.draw.aaline(surface,
                           self.__color.convert_to_tuple(),
                           self.__point_from,
                           self.__point_to)

        pygame.draw.polygon(surface,
                            self.__color.convert_to_tuple(),
                            [
                                self.__point_from
                                + (self.__vector * 0.9).rotate_rad(
                                    math.pi / 180),
                                self.__point_from
                                + (self.__vector * 0.9).rotate_rad(
                                    -math.pi / 180),
                                self.__point_to
                            ])
