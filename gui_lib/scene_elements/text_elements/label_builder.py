import pygame
from gui_lib.rgb_color import RgbColor
from pygame.surface import Surface


class LabelBuilder:
    def __init__(self,
                 text: str,
                 font_name: str,
                 font_size: int,
                 font_color: RgbColor):
        self.__text = text
        self.__font_name = font_name
        self.__font_size = font_size
        self.__font_color = font_color

    @property
    def text(self) -> str:
        return self.__text

    def set_text(self, text: str):
        self.__text = text

    def set_font_size(self, size: int):
        self.__font_size = size

    def set_font_color(self, color: RgbColor):
        self.__font_color = color

    def build(self) -> Surface:
        font = pygame.font.SysFont(self.__font_name, self.__font_size)

        return font.render(self.__text,
                           True,
                           self.__font_color.convert_to_tuple())
