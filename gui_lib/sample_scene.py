import pygame.key
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from gui_lib.scene_elements.gui_elements.text_input import TextInput
from pygame.math import Vector2
from pygame.surface import Surface


class SampleScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(RgbColors.DARK_BLUE)

        button = RectButton(Vector2(250, 250),
                            70, 50,
                            RgbColors.DARK_GREEN, RgbColors.DARK_BLUE)

        button.label.set_text("Button")

        lb = Label("Hello, Pygame!")
        lb.position = Vector2(100, 50)

        ti = TextInput(Vector2(300, 50), 100, 25)

        def click_func(bt: AbstractButton, evt):
            lb.set_text(ti.text)

        button.add_handler(pygame.MOUSEBUTTONDOWN, click_func)

        self.add_gui_element(ti)
        self.add_gui_element(button)
        self.add_gui_element(lb)
