from abc import ABC

from gui_lib.figures.figure import Figure
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler
from pygame.math import Vector2


class MouseClickHandler(EventHandler, ABC):
    def __init__(self, figure: Figure):
        super().__init__()
        self._figure = figure

    def add_on_click(self, func):
        self._handlers_functions.append(func)

    def remove_on_click(self, func):
        self._handlers_functions.remove(func)

    def is_clicked(self, point_on_surface: Vector2) -> bool:
        return self._figure.is_point_inside(point_on_surface)
