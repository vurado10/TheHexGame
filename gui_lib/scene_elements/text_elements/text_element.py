from abc import ABC, abstractmethod


class TextElement(ABC):
    @property
    @abstractmethod
    def label_builder(self):
        return None
