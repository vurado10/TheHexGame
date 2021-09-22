import pygame.font
from pygame.math import Vector2
from rgb_color import RgbColor


class Label:
    def __init__(self,
                 surface: pygame.Surface,
                 position: Vector2,
                 text: str,
                 color: RgbColor,
                 font_name: str,
                 font_size: int):
        self._surface = surface
        self._position = position
        self._text = text
        self._color = color
        self._font = pygame.font.SysFont(font_name, font_size)

    @property
    def image(self):
        return self._font.render(self._text,
                                 True,
                                 self._color.convert_to_tuple())

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def show(self):
        img = self.image
        self._surface.blit(img,
                           (self._position.x - img.get_width() / 2,
                            self._position.y - img.get_height() / 2))
