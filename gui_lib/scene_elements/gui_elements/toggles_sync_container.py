import pygame
from gui_lib.figures.rectangle import Rectangle
from gui_lib.scene_elements.gui_elements.toggle_button import ToggleButton
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class TogglesSyncContainer(Widget):
    def __init__(self, width_px, height_px, toggles: list[ToggleButton]):
        super().__init__(Vector2(0, 0), [pygame.MOUSEBUTTONDOWN])

        self.__toggles = list(toggles)

        self.__figure = Rectangle(self.position, width_px, height_px)

        self.add_children(self.__toggles)

    def set_position(self, value):
        Widget.set_position(self, value)
        self.__figure.position = value

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self.__figure.is_point_inside(Vector2(x, y))

    def notify(self, event: Event):
        if not self.is_valid_event(event):
            return
        
        for toggle in self.__toggles:
            toggle.deactivate()

        Widget.notify(self, event)


