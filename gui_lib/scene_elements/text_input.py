from typing import List

import pygame
from gui_lib.figures.figure import Figure
from gui_lib.scene_elements.event_handlers.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class TextInput(GuiElement, EventListener, TextElement):
    def __init__(self, figure: Figure, states_painters: List):
        GuiElement.__init__(self,
                            figure,
                            states_painters)
        EventListener.__init__(self)
        TextElement.__init__(self)

        self._is_active = False

        self.add_listening_type(pygame.MOUSEBUTTONDOWN)
        self.add_listening_type(pygame.KEYDOWN)

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def is_active(self) -> bool:
        return self._is_active

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))

    def is_valid_event(self, event: Event) -> bool:
        is_clicked = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            is_clicked = self._figure.is_point_inside(Vector2(x, y))

        return is_clicked or self.is_active()

