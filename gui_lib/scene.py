import sys
from typing import Tuple, Dict, List
import pygame
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.event_handlers.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.event import Event
from pygame.surface import Surface


class Scene(EventListener):
    def is_valid_event(self, event: Event) -> bool:
        return event.type == pygame.QUIT

    def __init__(self, screen: Surface):
        super().__init__()
        self.add_listening_type(pygame.QUIT)
        self.add_handler(lambda e, ev: sys.exit())
        self._screen = screen
        self._gui_elements = []
        self._event_handlers_by_event_type: Dict[int, List[EventListener]]

        self._listeners_by_event_type = {
            pygame.QUIT: [self] # TODO: exit event handler
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

    def add_gui_event_handler(self, event_handler: EventListener):
        if isinstance(event_handler, GuiElement):
            self.add_gui_element(event_handler)

        self.add_event_handler(event_handler)

    def add_event_handler(self, event_handler: EventListener):
        for event_type in event_handler.get_handling_event_types():
            if event_type not in self._listeners_by_event_type:
                self._listeners_by_event_type[event_type] = []

            self._listeners_by_event_type[event_type].append(
                event_handler)

    def get_event_handlers_by_event_type(self, event_type: int):
        if event_type not in self._listeners_by_event_type:
            self._listeners_by_event_type[event_type] = []

        for handler in self._listeners_by_event_type[event_type]:
            yield handler

    def update(self):
        self._screen.fill(self._bg_color.convert_to_tuple())

        for element in self._gui_elements:
            element.update_on(self._screen)
