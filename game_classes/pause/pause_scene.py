import pygame
from gui_lib import app
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from pygame.math import Vector2
from pygame.surface import Surface


class PauseScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.__pause_button = Button(RectangleFigure(Vector2(50, 40),
                                                     Vector2(40, 40), 0),
                                     [DescribedFigurePainter(
                                         RgbColors.DARK_GREEN,
                                         RgbColors.DARK_GREEN,
                                         RgbColors.DARK_GREEN,
                                         1)])
        self.__pause_button.label_builder.set_text("Resume")
        self.__pause_button.label_builder.set_font_color(RgbColors.DARK_BLUE)
        self.__pause_button.label_builder.set_font_size(20)

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "main"))

        self.add_gui_element(self.__pause_button)
