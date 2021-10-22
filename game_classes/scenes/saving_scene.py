import pygame
from game_classes.color_theme import SCENE_BG_COLOR
from game_classes.game_domain.match import Match
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from pygame.math import Vector2
from pygame.surface import Surface


class SavingScene(Scene):
    def __init__(self, screen: Surface,
                 match: Match,
                 matches_repository: MatchesRepository):
        super().__init__(screen)

        self.__match = match
        self.__matches_rep = matches_repository

        self.set_bg_color(SCENE_BG_COLOR)

        self.__back_button = \
            WidgetsFactory.create_rect_button(Vector2(100, 460), "Back")

        self.__save_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460), "Save")

        self.__save_file_name_input = WidgetsFactory.create_titled_text_input(
            Vector2(100, 50),
            "Name of match")

        self.__save_file_name_input.text = self.__matches_rep.generate_id()

        self.__back_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SavingScene.go_back)
        self.__save_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       self.save)

        self.__status_label = WidgetsFactory.create_label(Vector2(350, 470),
                                                          "")

        self.__status_label.set_font_size(24)

        self.__status_label.hide()

        self.add_gui_elements([
            self.__save_file_name_input,
            self.__back_button,
            self.__save_button,
            self.__status_label
        ])

    @staticmethod
    def go_back(*args):
        app.set_current_scene("pause")

    def show_success(self, text=""):
        self.__status_label.set_font_color(RgbColors.LIGHT_GREEN)
        self.__status_label.set_text("Success: " + text)
        self.__status_label.show()

    def show_error(self, text=""):
        self.__status_label.set_font_color(RgbColors.LIGHT_RED)
        self.__status_label.set_text("Error: " + text)
        self.__status_label.show()

    def save(self, *args):
        match_name = self.__save_file_name_input.text
        try:
            self.__matches_rep.save_with_id(self.__match, match_name)
            self.show_success(f"match was saved with name: {match_name}")
        except ValueError:
            self.show_error(f"you can't save match with name: {match_name}")
