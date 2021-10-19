from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.text_input import TextInput
from pygame.math import Vector2


class TitledTextInput(TextInput):
    def __init__(self,
                 position: Vector2,
                 input_width_px=160,
                 input_height_px=25,
                 input_max_length=20,
                 title="",
                 input_bg_color=RgbColors.DARK_RED,
                 input_text_color=RgbColors.WHITE,
                 title_color=RgbColors.DARK_GREEN):
        super().__init__(position,
                         input_width_px,
                         input_height_px,
                         input_max_length,
                         input_bg_color)

        self._label.set_font_color(input_text_color)

        self.__title_label = Label(title, title_color)
        self.__title_label.position = Vector2(0, -30)

        self.add_child(self.__title_label)
