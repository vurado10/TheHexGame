import pygame
from gui_lib.figures.rectangle import Rectangle
from gui_lib.painters.rectangle_painter import RectanglePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class TextInput(Widget):
    def __init__(self, position: Vector2, width_px, height_px):
        super().__init__(position, [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])

        self._bg_figure = Rectangle(position, width_px, height_px)
        self._bg_painter = RectanglePainter(RgbColors.DARK_RED,
                                            RgbColors.DARK_RED,
                                            RgbColors.DARK_RED,
                                            1.0)
        self._label = Label("placeholder", RgbColors.WHITE)
        self.add_child(self._label)

        self._is_active = False

        def on_key_down_text_input(text_input: TextInput, event):
            if event.key == pygame.K_RETURN:
                text_input.deactivate()
            else:
                text = self._label.label_builder.text
                alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"

                if event.key == pygame.K_SPACE:
                    self._label.set_text(text + " ")
                elif event.key == pygame.K_BACKSPACE:
                    self._label.set_text(text[:-1])
                elif event.unicode.casefold() in alphabet:
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

    def activate(self):
        self._is_active = True

    def deactivate(self):
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

