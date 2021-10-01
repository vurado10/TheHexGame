from abc import ABC, abstractmethod
from gui_lib.figures.figure import Figure
from gui_lib.painters.painter import Painter
from pygame.surface import Surface


class GuiElement(ABC):
    def __init__(self, figure: Figure, painter: Painter):
        self._figure = figure
        self._painter = painter

    @abstractmethod
    def update_on(self, surface: Surface):
        pass
