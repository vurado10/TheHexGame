from abc import ABC
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler


class KeyDownHandler(EventHandler, ABC):
    def __init__(self):
        super().__init__()
        self._on_key_down_handlers = []

    def add_on_key_down(self, func):
        self._on_key_down_handlers.append(func)

    def remove_on_key_down(self, func):
        self._on_key_down_handlers.remove(func)
