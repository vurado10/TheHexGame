import pygame
from game_classes.menu_scene import MenuScene
from gui_lib import app
from pygame.event import Event
from pygame.surface import Surface


class MainMenuScene(MenuScene):
    def __init__(self, screen: Surface):
        super().__init__(screen,
                         "The Hex",
                         ["Start New", "Load", "Settings", "Rating", "Exit"])

        self._buttons["Start New"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          lambda *args: app.set_current_scene(
                                              "game"))

        self._buttons["Load"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          lambda *args: app.set_current_scene(
                                              "savings list"))

        self._buttons["Settings"].add_handler(pygame.MOUSEBUTTONDOWN,
                                              lambda *args:
                                              app.set_current_scene(
                                                  "settings"))

        self._buttons["Rating"].add_handler(pygame.MOUSEBUTTONDOWN,
                                            lambda *args:
                                            app.set_current_scene("rating"))

        self._buttons["Exit"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          lambda *args: pygame.event.post(
                                              Event(pygame.QUIT)))
