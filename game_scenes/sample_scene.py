from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from pygame.math import Vector2
from pygame.surface import Surface


class SampleScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        state_1 = DescribedFigurePainter(RgbColors.BLACK,
                                         RgbColors.WHITE,
                                         RgbColors.BLACK, 0.95)

        state_2 = DescribedFigurePainter(RgbColors.BLACK,
                                         RgbColors.WHITE,
                                         RgbColors.WHITE, 1)

        button = Button(RectangleFigure(Vector2(250, 250),
                                        Vector2(50, 50),
                                        0.0),
                        [state_1, state_2])

        button.label_builder.set_font_color(RgbColors.LIGHT_GREEN)

        def click_func(bt, evt):
            nonlocal self
            bt.switch_to_next_state()
            bt.update_on(self._screen)

        button.add_on_click(click_func)

        self.add_event_handler(button)
