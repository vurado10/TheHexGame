from typing import List

import pygame
from gui_lib.figures.figure import Figure
from gui_lib.scene_elements.event_handlers.key_down_handler import \
    KeyDownHandler
from gui_lib.scene_elements.event_handlers.mouse_click_handler import \
    MouseClickHandler
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame.surface import Surface


class TextInput(GuiElement, MouseClickHandler, KeyDownHandler, TextElement):
    def __init__(self, figure: Figure, states_painters: List):
        GuiElement.__init__(self,
                            figure,
                            states_painters)
        MouseClickHandler.__init__(self, figure)
        KeyDownHandler.__init__(self)
        TextElement.__init__(self)

        # TODO: destroy kostyl!
        self._handling_event_types = [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))
