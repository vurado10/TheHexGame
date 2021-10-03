import threading
import time
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
                        [state_2])

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
                elif event.key == pygame.K_BACKSPACE:
                    text_input.label_builder.set_text(text_input.label_builder.text[:-1])
                else:
                    text_input.label_builder.set_text(text_input.label_builder.text + pygame.key.name(event.key))

        ti.add_handler(on_click_text_input)
        ti.add_handler(on_key_down_text_input)

        def click_func(bt: Button, evt):
            nonlocal lb, ti
            lb.label_builder.set_text(ti.label_builder.text)
            bt.position += Vector2(-15, -15)
            bt.switch_to_next_state()

        def wt(bt: Button, evt):
            def click_func(bt: Button, evt):
                nonlocal lb, ti
                lb.label_builder.set_text(ti.label_builder.text)
                bt.position += Vector2(1, 1)
                bt.switch_to_next_state()
            while True:
                click_func(bt, evt)
                time.sleep(0.1)

        t = threading.Thread(target=wt, args=(button, None))
        t.start()

        button.add_handler(click_func)

        self.add_gui_event_handler(button)
        self.add_gui_element(lb)
        self.add_gui_event_handler(ti)
