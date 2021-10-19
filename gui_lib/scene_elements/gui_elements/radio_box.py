import pygame
from game_classes import color_theme
from gui_lib.scene_elements.gui_elements.toggle_button import ToggleButton
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class RadioBox(Widget):
    def __init__(self, position: Vector2, variants_values: list[str]):
        super().__init__(position, [pygame.MOUSEBUTTONDOWN])

        self.__toggle_by_value = {}

        is_first = True
        last_position = Vector2(0, 0)
        for value in variants_values:
            button = ToggleButton(value,
                                  last_position,
                                  80,
                                  30,
                                  color_theme.BUTTON_BG_COLOR,
                                  color_theme.SCENE_BG_COLOR)

            last_position += Vector2(80 + 10, 0)

            if is_first:
                is_first = False
                button.activate()

            self.__toggle_by_value[value] = button

        self.__toggles = list(self.__toggle_by_value.values())

        self.add_children(self.__toggles)

    def get_value(self) -> str:
        for value in self.__toggle_by_value:
            if self.__toggle_by_value[value].is_active():
                return value

    def is_valid_event(self, event: Event) -> bool:
        return True

    def notify(self, event: Event):
        valid_toggles = [
            toggle
            for toggle in
            filter(lambda t: t.is_valid_event(event), self.__toggles)
        ]

        if valid_toggles:
            for toggle in self.__toggles:
                toggle.deactivate()

                if toggle.is_valid_event(event):
                    toggle.activate()
