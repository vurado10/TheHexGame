import pygame
from game_classes import color_theme
from gui_lib import app
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.list_view import ListView
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from gui_lib.scene_elements.gui_elements.titled_radio_box import TitledRadioBox
from gui_lib.scene_elements.gui_elements.titled_text_input import \
    TitledTextInput
from pygame.math import Vector2


class WidgetsFactory:
    @staticmethod
    def create_label(position: Vector2, text: str):
        label = Label(text, font_color=color_theme.TITLE_COLOR)
        label.set_position(position)

        return label

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

    @staticmethod
    def create_titled_radio_box(position: Vector2,
                                title: str,
                                variants_names: list[str]):
        return TitledRadioBox(position,
                              variants_names,
                              title,
                              title_color=color_theme.TITLE_COLOR,
                              toggles_active_color=color_theme.BUTTON_BG_COLOR,
                              toggles_inactive_text_color=
                              color_theme.SCENE_BG_COLOR)

    @staticmethod
    def create_list_view(position: Vector2, values: list[str]):
        return ListView(position,
                        values=values,
                        active_item_color=color_theme.BUTTON_BG_COLOR,
                        inactive_item_color=color_theme.SCENE_BG_COLOR)

    @staticmethod
    def create_scene_switcher_button(position: Vector2,
                                     text: str,
                                     next_scene_name: str,
                                     next_scene_type):
        def go_next(*args,
                    scene_name=next_scene_name,
                    scene_type=next_scene_type):
            app.create_and_set_scene(scene_name, scene_type)

        button = WidgetsFactory.create_rect_button(position, text)
        button.add_handler(pygame.MOUSEBUTTONDOWN, go_next)

        return button

