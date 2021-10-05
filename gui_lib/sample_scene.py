import pygame.key
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from gui_lib.scene_elements.label import Label
from gui_lib.scene_elements.text_input import TextInput
from pygame.math import Vector2
from pygame.surface import Surface


class SampleScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        state_1 = DescribedFigurePainter(RgbColors.BLACK,
                                         RgbColors.WHITE,
                                         RgbColors.BLACK, 0.9)

        state_2 = DescribedFigurePainter(RgbColors.BLACK,
                                         RgbColors.WHITE,
                                         RgbColor(50, 50, 50), 1.5)

        state_label = DescribedFigurePainter(RgbColors.BLACK,
                                             RgbColors.BLACK,
                                             RgbColors.BLACK, 1)

        button = Button(RectangleFigure(Vector2(250, 250),
                                        Vector2(50, 50),
                                        0.0),
                        [state_1, state_2])

        button.label_builder.set_font_color(RgbColors.LIGHT_GREEN)
        button.label_builder.set_text("Button")

        lb = Label(RectangleFigure(Vector2(100, 50), Vector2(100, 100), 0.0),
                   [state_label])
        lb.label_builder.set_font_color(RgbColors.LIGHT_GREEN)
        lb.label_builder.set_text("Hello, Pygame!")

        ti = TextInput(
            RectangleFigure(Vector2(450, 250), Vector2(100, 100), 0.0),
            [state_1, state_2])

        def click_func(bt: Button, evt):
            nonlocal lb, ti
            lb.label_builder.set_text(ti.label_builder.text)
            bt.switch_to_next_state()

        button.add_handler(pygame.MOUSEBUTTONDOWN, click_func)

        self.add_gui_element(button)
        self.add_gui_element(lb)
        self.add_gui_element(ti)
