from abc import ABC

import pygame
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler


class KeyDownHandler(EventHandler, ABC):
    def __init__(self):
        super().__init__([pygame.KEYDOWN])

    def add_on_key_down(self, func):
        self._handlers_functions.append(func)

    def remove_on_key_down(self, func):
        self._handlers_functions.remove(func)
