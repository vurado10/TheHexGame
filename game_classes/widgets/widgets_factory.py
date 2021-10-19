from game_classes import color_theme
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from gui_lib.scene_elements.gui_elements.titled_text_input import \
    TitledTextInput
from pygame.math import Vector2


class WidgetsFactory:
    @staticmethod
    def create_rect_button(position: Vector2, text: str):
        return RectButton(position,
                          100,
                          50,
                          bg_color=color_theme.BUTTON_BG_COLOR,
                          text_color=
                          color_theme.BUTTON_TEXT_COLOR,
                          text=text)

    @staticmethod
    def create_titled_text_input(position: Vector2, title: str):
        return TitledTextInput(
            position,
            input_bg_color=color_theme.TEXT_INPUT_BG,
            input_text_color=color_theme.TEXT_INPUT_CONTENT,
            title_color=color_theme.TITLE_COLOR,
            title=title
        )
