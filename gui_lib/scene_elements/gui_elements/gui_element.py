from abc import ABC, abstractmethod
from pygame.surface import Surface


class GuiElement(ABC):
    """Object drawing every frame of scene"""
    def __init__(self):
        self._is_hide = False

    def is_hide(self):
        return self._is_hide

    def show(self):
        self._is_hide = False

    def hide(self):
        self._is_hide = True

    @abstractmethod
    def update_on(self, surface: Surface):
        pass
