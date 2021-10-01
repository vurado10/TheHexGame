from abc import ABC
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler


class MouseClickHandler(EventHandler, ABC):
    def __init__(self):
        super().__init__()
        self._on_click_handlers = []

    def add_on_click(self, func):
        self._on_click_handlers.append(func)

    def remove_on_click(self, func):
        self._on_click_handlers.remove(func)
