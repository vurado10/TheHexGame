import pygame
from abc import ABC
from gui_lib.painters.painter import Painter
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


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

    @property
    def position(self):
        return Vector2(self._position)

    @position.setter
    def position(self, value: Vector2):
        prev_position = self._position
        self._position = Vector2(value)
        self._figure.position = self._position

        for child in self.children:
            child.position += self._position - prev_position

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self._figure.is_point_inside(Vector2(x, y))

    def update_self_on(self, surface: Surface):
        self._figure_painter.draw(surface, self._figure)
