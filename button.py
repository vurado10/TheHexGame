from figure import Figure
from label import Label
from pygame.math import Vector2


class Button:
    def __init__(self, figure: Figure, label: Label = None):
        self._figure = figure
        self._label = label
        self._state = 0
        self._on_click_function = None

        self._figure.start_painter(False)
        if self._label is not None:
            self._label.show()

    @property
    def on_click_function(self):
        return self._on_click_function

    @on_click_function.setter
    def on_click_function(self, value):
        self._on_click_function = value

    def switch_state(self):
        if self._state == 0:
            self._state = 1
            self._figure.start_painter(True)
        else:
            self._state = 0
            self._figure.start_painter(False)

    def is_clicked(self, point: Vector2) -> bool:
        return self._figure.is_point_inside(point)


