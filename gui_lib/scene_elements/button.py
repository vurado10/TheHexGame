import pygame
from typing import List
from gui_lib.figures.figure import Figure
from gui_lib.scene_elements.event_handlers.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame import Surface
from pygame.event import Event
from pygame.math import Vector2


class Button(GuiElement, EventListener, TextElement):
    def __init__(self, figure: Figure, states_painters: List):
        GuiElement.__init__(self,
                            figure,
                            states_painters)
        EventListener.__init__(self)
        TextElement.__init__(self)

        self.add_listening_type(pygame.MOUSEBUTTONDOWN)

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self._figure.is_point_inside(Vector2(x, y))
