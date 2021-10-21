import pygame
from game_classes.scenes.menu_scene import MenuScene
from gui_lib import app
from pygame.surface import Surface


class PauseScene(MenuScene):
    def __init__(self, screen: Surface, title: str = "Pause"):
        super().__init__(screen, title, ["Resume", "Save", "Main Menu"])

        self._buttons["Resume"].add_handler(pygame.MOUSEBUTTONDOWN,
                                         lambda *args: app.set_current_scene(
                                             "game"))

        self._buttons["Save"].add_handler(pygame.MOUSEBUTTONDOWN,
                                          PauseScene.handle_on_save)

        self._buttons["Main Menu"].add_handler(pygame.MOUSEBUTTONDOWN,
                                         lambda *args: app.set_current_scene(
                                             "main menu"))

    @staticmethod
    def handle_on_save(*args):
        app.set_current_scene("saving")
