import pygame
from gui_lib import utilities
from gui_lib.figures.rectangle import Rectangle
from gui_lib.painters.rectangle_painter import RectanglePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class TextInput(Widget):
    def __init__(self, position: Vector2,
                 width_px, height_px,
                 max_length=20,
                 bg_color=RgbColors.DARK_RED):
        super().__init__(position, [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])

        self._bg_figure = Rectangle(position, width_px, height_px)
        self._bg_painter = RectanglePainter(bg_color,
                                            bg_color,
                                            bg_color,
                                            1.0)

        self._max_length = max_length
        self._label = Label("", RgbColors.WHITE)
        self._label.position = Vector2(5, self._label.position.y)
        self.add_child(self._label)

        self._is_active = False
        self._on_activate = []
        self._on_deactivate = []

        def on_key_down_text_input(text_input: TextInput, event):
            if event.key == pygame.K_RETURN:
                text_input.deactivate()
            else:
                text = self._label.text
                alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
                if event.key == pygame.K_SPACE \
                        and len(text) + 1 < self._max_length:
                    self._label.set_text(text + " ")
                elif event.key == pygame.K_BACKSPACE:
                    self._label.set_text(text[:-1])
                elif event.unicode.casefold() in alphabet \
                        and len(text) + 1 < self._max_length:
                    self._label.set_text(text + event.unicode)

        def on_click_text_input(text_input: TextInput, event):
            if text_input.is_active():
                return

            text_input.activate()

        self.add_handler(pygame.MOUSEBUTTONDOWN, on_click_text_input)
        self.add_handler(pygame.KEYDOWN, on_key_down_text_input)

    @property
    def text(self) -> str:
        return self._label.text

    @text.setter
    def text(self, value: str):
        self._label.set_text(value)

    def set_max_length(self, value):
        self._max_length = value

    def add_on_activate(self, func):
        """func(TextInput text_input)"""
        self._on_activate.append(func)

    def add_on_deactivate(self, func):
        """func(TextInput text_input)"""
        self._on_deactivate.append(func)

    def activate(self):
        utilities.execute_all_funcs(self._on_activate, self)
        self._is_active = True

    def deactivate(self):
        utilities.execute_all_funcs(self._on_deactivate, self)
        self._is_active = False

    def is_active(self) -> bool:
        return self._is_active

    def update_self_on(self, surface: Surface):
        self._bg_painter.draw(surface, self._bg_figure)

    def is_valid_event(self, event: Event) -> bool:
        is_clicked = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            is_clicked = self._bg_figure.is_point_inside(Vector2(x, y))

        return is_clicked or self.is_active()
