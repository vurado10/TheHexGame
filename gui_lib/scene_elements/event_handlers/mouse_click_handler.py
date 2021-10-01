from abc import ABC


class MouseClickHandler(ABC):
    def __init__(self):
        self._on_click = None

    def set_on_click(self, func):
        self._on_click = func
