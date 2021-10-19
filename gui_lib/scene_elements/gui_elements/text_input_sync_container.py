import pygame
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class TextInputSyncContainer(Widget):
    def __init__(self,
                 text_input_by_name: dict):
        super().__init__(Vector2(0, 0),
                         [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])
        self.__input_by_name = dict(text_input_by_name)
        self.__text_inputs = list(self.__input_by_name.values())

        self.add_children(self.__text_inputs)

    def activate_input(self, name: str):
        for text_input in self.__text_inputs:
            text_input.deactivate()

        self.__input_by_name[name].activate()

    def notify(self, event: Event):
        if event.type == pygame.KEYDOWN:
            Widget.notify(self, event)
            return
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for text_input in self.__text_inputs:
                text_input.deactivate()

                if text_input.is_valid_event(event):
                    text_input.activate()

    def is_valid_event(self, event: Event) -> bool:
        return True
