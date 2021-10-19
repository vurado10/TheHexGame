import pygame
from game_classes import color_theme
from game_classes.ai.random_bot import RandomBot
from game_classes.color_theme import PLAYER1_COLOR, PLAYER2_COLOR
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.scenes.match_scene import MatchScene
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
            WidgetsFactory.create_titled_text_input(Vector2(100, 50),
                                                    "First player nickname")
        self.__second_player_name_input = \
            WidgetsFactory.create_titled_text_input(Vector2(100, 150),
                                                    "Second player nickname")

        self.__first_player_name_input.text = "Player_1"
        self.__second_player_name_input.text = "Player_2"
        self.__first_player_name_input.set_max_length(12)
        self.__second_player_name_input.set_max_length(12)

        self.__name_inputs_form = TextInputSyncContainer({
            "First player": self.__first_player_name_input,
            "Second player": self.__second_player_name_input
        })

        self.__field_size_radio_box = \
            WidgetsFactory.create_titled_radio_box(Vector2(400, 50),
                                                   "Choose field size",
                                                   ["5x5",
                                                    "11x11",
                                                    "14x14",
                                                    "19x19"])

        self.__timer_radio_box = \
            WidgetsFactory.create_titled_radio_box(Vector2(400, 150),
                                                   "Choose a timer setting "
                                                   "(game time in min "
                                                   "/ move time in min)",
                                                   ["inf / inf",
                                                    "inf / 2",
                                                    "10 / inf",
                                                    "60 / inf",
                                                    "10 / 1"])

        self.__first_ai_radio_box = \
            WidgetsFactory.create_titled_radio_box(Vector2(400, 250),
                                                   "First player "
                                                   "AI setting",
                                                   ["No AI",
                                                    "Random",
                                                    "Level 1"])

        self.__second_ai_radio_box = \
            WidgetsFactory.create_titled_radio_box(Vector2(400, 350),
                                                   "Second player "
                                                   "AI setting",
                                                   ["No AI",
                                                    "Random",
                                                    "Level 1"])

        self.__back_button = \
            WidgetsFactory.create_rect_button(Vector2(100, 460), "Back")

        self.__start_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460), "Start game")

        self.__back_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SettingsScene.go_back)

        self.__start_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        self.start_game)

        self.add_gui_elements([
            self.__name_inputs_form,
            self.__field_size_radio_box,
            self.__timer_radio_box,
            self.__first_ai_radio_box,
            self.__second_ai_radio_box,
            self.__back_button,
            self.__start_button
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
        width, height = \
            map(int, self.__field_size_radio_box.get_value().split("x"))

        player1 = PlayerProfile(self.__first_player_name_input.text,
                                PLAYER1_COLOR)
        player2 = PlayerProfile(self.__second_player_name_input.text,
                                PLAYER2_COLOR)

        match = Match("0",
                      HexField(width, height),
                      [player1, player2],
                      {player1.name: Directions.HORIZONTAL,
                       player2.name: Directions.VERTICAL})

        app.create_and_set_scene("game", MatchScene, match=match)

        ai_input1 = self.__first_ai_radio_box.get_value()
        ai_input2 = self.__second_ai_radio_box.get_value()
        bot = RandomBot(match)

        def ai1_move(current_player, next_player):
            if next_player.name == player1.name:
                bot.make_move()

        def ai2_move(current_player, next_player):
            if next_player.name == player2.name:
                bot.make_move()

        if ai_input2 == "Random":
            match.add_on_switch_move_owner(ai2_move)

        if ai_input1 == "Random":
            match.add_on_switch_move_owner(ai1_move)

            bot.make_move()
