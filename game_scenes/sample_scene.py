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
                                         RgbColor(50, 50, 50), 1)

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

        def on_click_text_input(text_input: TextInput, event):
            nonlocal self
            if text_input.is_active():
                return

            text_input.activate()
            text_input.switch_to_next_state()
            text_input.update_on(self._screen)

        def on_key_down_text_input(text_input: TextInput, event):
            nonlocal self
            # TODO: no try-except!
            try:
                key = event.key
            except:
                return
            if event.key == pygame.K_KP_ENTER:
                text_input.deactivate()
                text_input.switch_to_next_state()
            else:
                if event.key == pygame.K_SPACE:
                    text_input.label_builder.set_text(text_input.label_builder.text + " ")
                else:
                    text_input.label_builder.set_text(text_input.label_builder.text + pygame.key.name(event.key))
            text_input.update_on(self._screen)

        ti.add_on_click(on_click_text_input)
        ti.add_on_key_down(on_key_down_text_input)

        def click_func(bt, evt):
            nonlocal self, lb, ti
            lb.label_builder.set_text(ti.label_builder.text)
            lb.update_on(self._screen)
            bt.switch_to_next_state()
            bt.update_on(self._screen)

        button.add_on_click(click_func)

        self.add_gui_event_handler(button)
        self.add_gui_element(lb)
        self.add_gui_event_handler(ti)
