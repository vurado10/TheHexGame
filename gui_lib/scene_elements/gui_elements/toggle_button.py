import pygame
from gui_lib.painters.rectangle_painter import RectanglePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from pygame.event import Event
from pygame.math import Vector2


class ToggleButton(RectButton):
    def __init__(self,
                 title: str,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 active_bg_color: RgbColor,
                 inactive_bg_color: RgbColor):
        self.__active_painter = RectanglePainter(active_bg_color,
                                                 active_bg_color,
                                                 active_bg_color,
                                                 .8)

        self.__inactive_painter = RectanglePainter(inactive_bg_color,
                                                   active_bg_color,
                                                   inactive_bg_color,
                                                   .7)

        super().__init__(position,
                         width_px,
                         height_px,
                         RgbColors.WHITE,
                         RgbColors.WHITE,
                         text=title)

        self._figure_painter = self.__inactive_painter

        self.__active_text_color = inactive_bg_color
        self.__inactive_text_color = active_bg_color

        self._label.set_font_color(self.__inactive_text_color)

        self.__is_active = False

        def toggle_on_click(sender: ToggleButton, event: Event):
            if sender.is_active():
                sender.deactivate()
                return

            sender.activate()

        self.add_handler(pygame.MOUSEBUTTONDOWN, toggle_on_click)

    def activate(self) -> None:
        self.__is_active = True
        self._figure_painter = self.__active_painter
        self._label.set_font_color(self.__active_text_color)

    def deactivate(self) -> None:
        self.__is_active = False
        self._figure_painter = self.__inactive_painter
        self._label.set_font_color(self.__inactive_text_color)

    def is_active(self) -> bool:
        return self.__is_active
