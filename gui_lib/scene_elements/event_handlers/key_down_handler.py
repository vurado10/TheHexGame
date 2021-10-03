import pygame
from abc import ABC
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler
from pygame.event import Event


class KeyDownHandler(EventHandler, ABC):
    def __init__(self):
        super().__init__([pygame.KEYDOWN])
        self._is_active = False

    def add_on_key_down(self, func):
        self._handlers_functions.append(func)

    def remove_on_key_down(self, func):
        self._handlers_functions.remove(func)

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def is_active(self) -> bool:
        return self._is_active

    def is_valid_event(self, event: Event) -> bool:
        return self.is_active()
