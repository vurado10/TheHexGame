import pygame
from typing import List
from gui_lib.figures.figure import Figure
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.event_system.event_listener import EventListener
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

        self.add_handler(pygame.MOUSEBUTTONDOWN, lambda *args: None)

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))

    def is_valid_event(self, event: Event) -> bool:
        x, y = pygame.mouse.get_pos()

        return self._figure.is_point_inside(Vector2(x, y))

    @staticmethod
    def create(text: str,
               size=Vector2(40, 40),
               font_color=RgbColors.DARK_BLUE,
               font_size=20,
               bg_color=RgbColors.DARK_GREEN):
        button = Button(RectangleFigure(Vector2(),
                               Vector2(size), 0),
               [DescribedFigurePainter(
                   bg_color,
                   bg_color,
                   bg_color,
                   1)])
        button.label_builder.set_font_size(font_size)
        button.label_builder.set_font_color(font_color)
        button.label_builder.set_text(text)

        return button
