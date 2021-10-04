import os
import sys
import pygame
from typing import Tuple
from gui_lib.scene_elements.event_system.event_manager import EventManager
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.event_system.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.event import Event
from pygame.surface import Surface


class Scene(EventListener):
    def __init__(self, screen: Surface):
        super().__init__()
        self.event_manager = EventManager()

        def exit_game(e, v):
            pygame.quit()
            # sys.exit(0)
            os._exit(0)

        self.add_listening_type(pygame.QUIT)
        self.add_handler(exit_game)
        self.event_manager.add_listener(self)

        self._screen = screen
        self._gui_elements = []

        self._bg_color = RgbColors.BLACK

    def is_valid_event(self, event: Event) -> bool:
        return event.type == pygame.QUIT

    @property
    def size(self) -> Tuple[int, int]:
        return self._screen.get_size()

    def set_bg_color(self, color: RgbColor):
        self._bg_color = color

    def get_gui_elements(self):
        for element in self._gui_elements:
            yield element

    def add_gui_element(self, element: GuiElement):
        self._gui_elements.append(element)

        if isinstance(element, EventListener):
            self.event_manager.add_listener(element)

    def update(self):
        self._screen.fill(self._bg_color.convert_to_tuple())

        for element in self._gui_elements:
            element.update_on(self._screen)
