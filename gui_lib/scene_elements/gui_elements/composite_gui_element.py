from typing import List

from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.math import Vector2
from pygame.surface import Surface


class CompositeGuiElement(GuiElement):
    def __init__(self,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 bg_color: RgbColor = RgbColors.BLACK):
        center = (position
                  + Vector2(width_px / 2, 0)
                  + Vector2(0, height_px / 2))

        GuiElement.__init__(self,
                            RectangleFigure(center, Vector2(), 0.0),
                            [DescribedFigurePainter(bg_color,
                                                    bg_color,
                                                    bg_color,
                                                    1.0)])
        self._position = Vector2(position)
        self._width_px = width_px
        self._height_px = height_px
        self._children = []

    def add_child_element(self, element: GuiElement):
        element.center += self._position
        self._children.append(element)

    def add_children_elements(self, elements: List[GuiElement]):
        for element in elements:
            self.add_child_element(element)

    def update_on(self, surface: Surface):
        for child in self._children:
            child.update_on(surface)
