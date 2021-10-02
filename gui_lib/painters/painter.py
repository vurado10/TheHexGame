from abc import ABC, abstractmethod
from gui_lib.figures.figure import Figure
from gui_lib.rgb_color import RgbColor
from pygame import Surface


class Painter(ABC):
    def __init__(self,
                 bg_color: RgbColor,
                 border_color: RgbColor,
                 fill_color: RgbColor,
                 padding_factor: float):
        self._bg_color = bg_color
        self._border_color = border_color
        self._fill_color = fill_color
        self._padding_factor = padding_factor

    @abstractmethod
    def draw(self, surface: Surface, figure: Figure) -> None:
        pass


