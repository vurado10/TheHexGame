import sys
import threading

import pygame
from typing import Tuple
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.event_system.event_listener import EventListener
from gui_lib.scene_elements.event_system.event_manager import EventManager
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.event import Event
from pygame.surface import Surface


class Scene(EventListener):
    def __init__(self, screen: Surface, settings_file_path=""):
        super().__init__()
        self.event_manager = EventManager()

        def exit_game(e, v):
            pygame.quit()
            # Is it need to stop the bots?
            sys.exit(0)

        self.add_handler(pygame.QUIT, exit_game)
        self.event_manager.add_listener(self)

        self._screen = screen
        self._gui_elements = []

        self._bg_color = RgbColors.BLACK

        self._settings_file_path = settings_file_path

    @property
    def size(self) -> Tuple[int, int]:
        return self._screen.get_size()

    @property
    def settings_file_path(self) -> str:
        return self._settings_file_path

    def is_valid_event(self, event: Event) -> bool:
        return True

    def set_bg_color(self, color: RgbColor):
        self._bg_color = color

    def get_bg_color(self) -> RgbColor:
        return self._bg_color

    def get_gui_elements(self):
        for element in self._gui_elements:
            yield element

    def add_gui_element(self, element: GuiElement):
        self._gui_elements.append(element)

        if isinstance(element, EventListener):
            self.event_manager.add_listener(element)

    def add_gui_elements(self, elements: list[GuiElement]):
        for element in elements:
            self.add_gui_element(element)

    def on_show(self):
        pass

    def on_hide(self):
        pass

    def update(self):
        """Update every GuiElement on the scene"""
        self._screen.fill(self._bg_color.convert_to_tuple())

        for element in self._gui_elements:
            if element.is_hide():
                continue

            element.update_on(self._screen)
