import pygame
from game_classes import color_theme, environment
from game_classes.color_theme import PLAYER1_COLOR, PLAYER2_COLOR
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.rating_system.rating_recorder import RatingRecorder
from game_classes.scenes.ai_settings_helper import AiSettingsHelper
from game_classes.scenes.match_scene import MatchScene
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.storages.players_repository import PlayersRepository
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.text_input_sync_container import \
    TextInputSyncContainer
from pygame.math import Vector2
from pygame.surface import Surface


class MatchCreatingScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(color_theme.SCENE_BG_COLOR)

        self.__first_player_name_input = \
            WidgetsFactory.create_titled_text_input(Vector2(100, 50),
                                                    "First player nickname")
        self.__second_player_name_input = \
            WidgetsFactory.create_titled_text_input(Vector2(100, 150),
                                                    "Second player nickname")

        self.__status_label = WidgetsFactory.create_label(Vector2(350, 470),
                                                          "")
        self.__status_label.hide()

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
                                                    "10 / 0.5",
                                                    "0.5 / 5"])

        self.__ai_types, self.__first_ai_input, self.__second_ai_input = \
            WidgetsFactory.create_ai_options(Vector2(400, 250))

        self.__back_button = \
            WidgetsFactory.create_rect_button(Vector2(100, 460), "Back")

        self.__start_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460), "Start game")

        self.__back_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       MatchCreatingScene.go_back)

        self.__start_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        self.start_game)

        self.add_gui_elements([
            self.__name_inputs_form,
            self.__status_label,
            self.__field_size_radio_box,
            self.__timer_radio_box,
            self.__first_ai_input,
            self.__second_ai_input,
            self.__back_button,
            self.__start_button
        ])

    @staticmethod
    def go_back(*args):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        app.create_and_set_scene("main menu", MainMenuScene)

    def start_game(self, *args):
        self.__status_label.hide()

        width, height = \
            map(int, self.__field_size_radio_box.get_value().split("x"))

        players_rep = PlayersRepository(environment.PLAYERS_REP_PATH)
        matches_rep = MatchesRepository(environment.MATCHES_REP_PATH,
                                        players_rep)

        player1, player2 = self.__load_players(players_rep)

        game_time, move_time = self.parse_time()

        try:
            match = Match(matches_rep.generate_id(),
                          HexField(width, height),
                          [player1, player2],
                          {player1.name: Directions.HORIZONTAL,
                           player2.name: Directions.VERTICAL},
                          time_for_game=game_time,
                          time_for_move=move_time)
        except ValueError as e:
            self.__show_error(e.args[0])
            return

        ai_names, bots = \
            (AiSettingsHelper(self.__ai_types)
                .create_bots(match,
                             self.__first_ai_input.get_value(),
                             self.__second_ai_input.get_value()))

        match_scene = MatchScene(app.screen,
                                 match,
                                 RatingRecorder(players_rep),
                                 matches_rep,
                                 ai_names,
                                 bots)

        app.register_and_show_scene("game", match_scene)

    def parse_time(self) -> tuple[float, float]:
        game_time, move_time = self.__timer_radio_box.get_value().split(" / ")

        return float(game_time) * 60, float(move_time) * 60

    def __load_players(self, players_rep) -> list[PlayerProfile]:
        return [
            MatchCreatingScene.__load_player(
                self.__first_player_name_input.text,
                players_rep, 0),
            MatchCreatingScene.__load_player(
                self.__second_player_name_input.text,
                players_rep, 1)
        ]

    @staticmethod
    def __load_player(name, players_rep, move_order: int) -> PlayerProfile:
        color = PLAYER1_COLOR if move_order == 0 else PLAYER2_COLOR
        try:
            player = players_rep.get_by_id(name)
            player.color = color
        except ValueError:
            player = PlayerProfile(name, 0)
            players_rep.save(player)

        return player

    def __show_error(self, text=""):
        self.__status_label.set_text("Error: " + text)
        self.__status_label.show()
        self.__status_label.set_font_color(RgbColors.LIGHT_RED)
