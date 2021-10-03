from typing import List
from gui_lib.figures.figure import Figure
from gui_lib.painters.painter import Painter
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from gui_lib.scene_elements.text_elements.text_element import TextElement
from pygame.surface import Surface


class Label(GuiElement, TextElement):
    def __init__(self, figure: Figure, states_painters: List[Painter]):
        # BUG: figure - ограничивающая фигура, если её размер слишком мал,
        # то надпись будет неправильно отображаться при перерисовке"""
        
        GuiElement.__init__(self,
                            figure,
                            states_painters)
        TextElement.__init__(self)

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        label = self.label_builder.build()
        surface.blit(label,
                     (self._figure.center.x - label.get_width() / 2,
                      self._figure.center.y - label.get_height() / 2))
