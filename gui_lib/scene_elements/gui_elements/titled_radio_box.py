from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.radio_box import RadioBox
from pygame.math import Vector2


class TitledRadioBox(RadioBox):
    def __init__(self,
                 position: Vector2,
                 variants_values: list[str],
                 title="",
                 title_color=RgbColors.DARK_GREEN,
                 toggles_active_color=RgbColors.DARK_RED,
                 toggles_inactive_text_color=RgbColors.WHITE):
        super().__init__(position, variants_values,
                         toggles_active_color, toggles_inactive_text_color)

        self.__title_label = Label(title, title_color)
        self.__title_label.position = Vector2(0, -30)

        self.add_child(self.__title_label)
