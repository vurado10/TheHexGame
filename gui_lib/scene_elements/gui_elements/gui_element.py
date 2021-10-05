from abc import ABC, abstractmethod
from typing import List
from gui_lib.figures.figure import Figure
from gui_lib.painters.painter import Painter
from pygame.math import Vector2
from pygame.surface import Surface


class GuiElement(ABC):
    def __init__(self, figure: Figure, states_painters: List[Painter]):
        if len(states_painters) < 1:
            raise Exception()

        self._current_state = 0
        self._states_painters = states_painters
        self._figure = figure

    @property
    def center(self) -> Vector2:
        return self._figure.center

    @center.setter
    def center(self, position: Vector2):
        self._figure.center = position

    def switch_to_next_state(self):
        self._current_state = (self._current_state + 1) \
                              % len(self._states_painters)

    def draw_current_state(self, surface: Surface):
        self._states_painters[self._current_state].draw(surface, self._figure)

    @abstractmethod
    def update_on(self, surface: Surface):
        pass
