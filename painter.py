from abc import ABC, abstractmethod


class Painter(ABC):
    @abstractmethod
    def draw(self, figure, is_filled: bool):
        pass
