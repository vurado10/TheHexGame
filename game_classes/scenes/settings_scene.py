import pygame
from game_classes import color_theme
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.radio_box import RadioBox
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from gui_lib.scene_elements.gui_elements.text_input_sync_container import \
    TextInputSyncContainer
from gui_lib.scene_elements.gui_elements.titled_text_input import \
    TitledTextInput
from pygame.math import Vector2
from pygame.surface import Surface


class SettingsScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(color_theme.SCENE_BG_COLOR)

        self.__first_player_name_input = \
            WidgetsFactory.create_rect_button(Vector2(100, 50),
                                              "First player name")
        self.__second_player_name_input = \
            WidgetsFactory.create_rect_button(Vector2(100, 120),
                                              "Second player name")

        self.__first_player_name_input.text = "name1"
        self.__second_player_name_input.text = "name2"

        self.__name_inputs = TextInputSyncContainer({
            "First player": self.__first_player_name_input,
            "Second player": self.__second_player_name_input
        })

        self.__field_size_radio_box, self.__field_size_radio_box_title \
            = SettingsScene.create_radio_box_with_title(Vector2(400, 50),
                                                        "Choose field size",
                                                        ["5x5",
                                                         "11x11",
                                                         "14x14",
                                                         "19x19"])

        self.__timer_radio_box, self.__timer_radio_box_title = \
            SettingsScene.create_radio_box_with_title(Vector2(400, 150),
                                                      "Choose a timer setting "
                                                      "(game time in min "
                                                      "/ move time in min)",
                                                      ["inf / inf",
                                                       "inf / 2",
                                                       "10 / inf",
                                                       "60 / inf",
                                                       "10 / 1"])

        self.__first_ai_radio_box, self.__first_ai_radio_box_title = \
            SettingsScene.create_radio_box_with_title(Vector2(400, 250),
                                                      "First player "
                                                      "AI setting",
                                                      ["No AI",
                                                       "Random",
                                                       "Level 1"])

        self.__second_ai_radio_box, self.__second_ai_radio_box_title = \
            SettingsScene.create_radio_box_with_title(Vector2(400, 350),
                                                      "Second player "
                                                      "AI setting",
                                                      ["No AI",
                                                       "Random",
                                                       "Level 1"])

        self.__back_button = \
            WidgetsFactory.create_rect_button(Vector2(100, 460), "Back")

        self.__back_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SettingsScene.go_back)

        self.__submit_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460), "Start game")

        self.__back_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SettingsScene.start_game)

        self.add_gui_elements([
            self.__name_inputs,
            self.__field_size_radio_box_title,
            self.__field_size_radio_box,
            self.__timer_radio_box,
            self.__timer_radio_box_title,
            self.__first_ai_radio_box,
            self.__first_ai_radio_box_title,
            self.__second_ai_radio_box,
            self.__second_ai_radio_box_title,
            self.__back_button,
            self.__submit_button
        ])

    @staticmethod
    def create_radio_box_with_title(radio_box_position: Vector2,
                                    title: str,
                                    variants_names: list[str]):
        radio_box = RadioBox(radio_box_position, variants_names)
        radio_box_title = Label(title)
        radio_box_title.position = \
            radio_box.position + Vector2(0, -30)

        return [radio_box, radio_box_title]

    @staticmethod
    def go_back(*args):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        app.create_and_set_scene("main menu", MainMenuScene)

    def start_game(self, *args):
        pass
