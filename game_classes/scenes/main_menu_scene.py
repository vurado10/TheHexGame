import pygame
from game_classes.scenes.match_scene import MatchScene
from game_classes.scenes.menu_scene import MenuScene
from game_classes.scenes.settings_scene import SettingsScene
from gui_lib import app
from pygame.event import Event
from pygame.surface import Surface


class MainMenuScene(MenuScene):
    def __init__(self, screen: Surface):
        super().__init__(screen,
                         "The Hex",
                         ["Start New", "Load", "Rating", "Exit"])

        self._buttons["Start New"].add_handler(pygame.MOUSEBUTTONDOWN,
                                               MainMenuScene.start_new_game)

        self._buttons["Load"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          lambda *args: app.set_current_scene(
                                              "savings list"))

        # self._buttons["Settings"].add_handler(pygame.MOUSEBUTTONDOWN,
        #                                       lambda *args:
        #                                       app.set_current_scene(
        #                                           "settings"))

        self._buttons["Rating"].add_handler(pygame.MOUSEBUTTONDOWN,
                                            lambda *args:
                                            app.set_current_scene("rating"))

        self._buttons["Exit"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          lambda *args: pygame.event.post(
                                              Event(pygame.QUIT)))

    @staticmethod
    def start_new_game(*args):
        app.create_and_set_scene("settings", SettingsScene)
