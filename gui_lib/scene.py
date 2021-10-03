import sys
from typing import Tuple, Dict, List
import pygame
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.event_handlers.event_handler import EventHandler
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.surface import Surface


class Scene:
    def __init__(self, screen: Surface):
        self._screen = screen
        self._gui_elements = []
        self._event_handlers_by_event_type: Dict[int, List[EventHandler]]

        self._event_handlers_by_event_type = {
            pygame.QUIT: [] # TODO: exit event handler
        }
        self._bg_color = RgbColors.BLACK

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

    def add_gui_event_handler(self, event_handler: EventHandler):
        if isinstance(event_handler, GuiElement):
            self.add_gui_element(event_handler)

        self.add_event_handler(event_handler)

    def add_event_handler(self, event_handler: EventHandler):
        for event_type in event_handler.get_handling_event_types():
            if event_type not in self._event_handlers_by_event_type:
                self._event_handlers_by_event_type[event_type] = []

            self._event_handlers_by_event_type[event_type].append(
                event_handler)

    def get_event_handlers_by_event_type(self, event_type: int):
        if event_type not in self._event_handlers_by_event_type:
            self._event_handlers_by_event_type[event_type] = []

        for handler in self._event_handlers_by_event_type[event_type]:
            yield handler

    def update(self):
        self._screen.fill(self._bg_color.convert_to_tuple())

        for element in self._gui_elements:
            element.update_on(self._screen)
