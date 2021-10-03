from abc import ABC

import pygame
from gui_lib.figures.figure import Figure
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler
from pygame.event import Event
from pygame.math import Vector2


class MouseClickHandler(EventHandler, ABC):
    def __init__(self, figure: Figure):
        # super(MouseClickHandler, self).__init__([pygame.MOUSEBUTTONDOWN])
        EventHandler.__init__(self, [pygame.MOUSEBUTTONDOWN])
        self._figure = figure

    def add_on_click(self, func):
        self._handlers_functions.append(func)

    def remove_on_click(self, func):
        self._handlers_functions.remove(func)

    def is_clicked(self, point_on_surface: Vector2) -> bool:
        return self._figure.is_point_inside(point_on_surface)

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self.is_clicked(Vector2(x, y))
