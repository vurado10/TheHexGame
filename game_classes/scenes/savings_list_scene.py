import pygame
from game_classes import environment
from game_classes.rating_system.rating_recorder import RatingRecorder
from game_classes.scenes.ai_settings_helper import AiSettingsHelper
from game_classes.scenes.match_scene import MatchScene
from game_classes.scenes.scene_with_list import SceneWithList
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.storages.players_repository import PlayersRepository
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from pygame.math import Vector2
from pygame.surface import Surface


class SavingsListScene(SceneWithList):
    def __init__(self, screen: Surface):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        self.__players_rep = PlayersRepository(environment.PLAYERS_REP_PATH)
        self.__matches_rep = MatchesRepository(environment.MATCHES_REP_PATH,
                                               self.__players_rep)

        super().__init__(screen,
                         "main menu",
                         MainMenuScene,
                         self.__matches_rep.get_all_ids())

        # TODO: code repeating
        self.__ai_types, self.__first_ai_input, self.__second_ai_input = \
            WidgetsFactory.create_ai_options(Vector2(500, 150))

        self.__loading_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460),
                                              "Load")

        self.__loading_button.add_handler(pygame.MOUSEBUTTONDOWN, self.load)

        self.add_gui_elements([
            self.__loading_button,
            self.__first_ai_input,
            self.__second_ai_input
        ])

    def load(self, *args):
        try:
            match = \
                self.__matches_rep.get_by_id(
                    self._list_view.get_chosen_value())
        except ValueError:
            return

        ai_names, bots = \
            (AiSettingsHelper(self.__ai_types)
                .create_bots(match,
                             self.__first_ai_input.get_value(),
                             self.__second_ai_input.get_value()))

        match_scene = MatchScene(app.screen,
                                 match,
                                 RatingRecorder(self.__players_rep),
                                 self.__matches_rep,
                                 ai_names,
                                 bots)

        app.register_and_show_scene("game", match_scene)

