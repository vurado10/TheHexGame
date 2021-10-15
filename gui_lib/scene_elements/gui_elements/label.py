from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.widget import Widget
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class Label(Widget, TextElement):
    def __init__(self,
                 text,
                 font_color=RgbColors.DARK_GREEN,
                 font_size=20):
        Widget.__init__(self, Vector2(0, 0))
        TextElement.__init__(self)

        self.label_builder.set_font_size(font_size)
        self.label_builder.set_font_color(font_color)
        self.label_builder.set_text(text)

        self._image = self.label_builder.build()

    def set_text(self, text):
        self.label_builder.set_text(text)
        self._image = self.label_builder.build()

    def set_font_size(self, font_size):
        self.label_builder.set_font_size(font_size)
        self._image = self.label_builder.build()

    def set_font_color(self, color: RgbColor):
        self.label_builder.set_font_color(color)
        self._image = self.label_builder.build()

    def update_self_on(self, surface: Surface):
        surface.blit(self._image, tuple(self._position))

    def is_valid_event(self, event: Event) -> bool:
        return False
