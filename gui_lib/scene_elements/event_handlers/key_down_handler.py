from abc import ABC


class KeyDownHandler(ABC):
    def __init__(self):
        self._on_key_down = None

    def set_key_down(self, func):
        self._on_key_down = func
