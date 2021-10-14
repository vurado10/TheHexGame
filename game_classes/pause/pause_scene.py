import pygame
from game_classes.menu_scene import MenuScene
from gui_lib import app
from pygame.surface import Surface


class PauseScene(MenuScene):
    def __init__(self, screen: Surface):
        super().__init__(screen, "Pause", ["Resume", "Main Menu"])

        self._buttons["Resume"].add_handler(pygame.MOUSEBUTTONDOWN,
                                         lambda *args: app.set_current_scene(
                                             "game"))

        self._buttons["Main Menu"].add_handler(pygame.MOUSEBUTTONDOWN,
                                         lambda *args: app.set_current_scene(
                                             "main menu"))
