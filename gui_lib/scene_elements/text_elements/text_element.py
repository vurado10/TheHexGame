from abc import ABC, abstractmethod

from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.text_elements.label_builder import LabelBuilder


class TextElement(ABC):
    def __init__(self):
        self._label_builder = LabelBuilder("text", "Arial",
                                           24, RgbColors.WHITE)

    @property
    def label_builder(self):
        return self._label_builder
