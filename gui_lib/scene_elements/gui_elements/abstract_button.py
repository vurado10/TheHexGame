from abc import ABC
import pygame
from gui_lib.painters.painter import Painter
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class AbstractButton(Widget, ABC):
    def __init__(self,
                 position: Vector2,
                 figure,
                 figure_painter: Painter):
        Widget.__init__(self, position, [pygame.MOUSEBUTTONDOWN])

        self._figure = figure

        self._label = Label("")
        self.add_child(self._label)

        self._figure_painter = figure_painter

    @property
    def label(self):
        return self._label

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self._figure.is_point_inside(Vector2(x, y))
