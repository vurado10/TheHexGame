import pygame
from game_classes import color_theme
from game_classes.color_theme import SCENE_BG_COLOR
from gui_lib import app
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from pygame.math import Vector2
from pygame.surface import Surface


class SavingScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(SCENE_BG_COLOR)

        self.__back_button = RectButton(Vector2(80, 400),
                                        100,
                                        50,
                                        bg_color=color_theme.BUTTON_BG_COLOR,
                                        text_color=color_theme
                                        .BUTTON_TEXT_COLOR)

        self.__save_button = RectButton(Vector2(200, 400),
                                        100,
                                        50,
                                        bg_color=color_theme.BUTTON_BG_COLOR,
                                        text_color=color_theme
                                        .BUTTON_TEXT_COLOR)

        self.__back_button.label.set_text("Back")
        self.__save_button.label.set_text("Save")

        self.__save_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SavingScene.go_back)
        self.__save_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       SavingScene.save)

        self.add_gui_element(self.__back_button)
        self.add_gui_element(self.__save_button)

    @staticmethod
    def go_back(*args):
        app.set_current_scene("pause")

    @staticmethod
    def save(*args):
        app.get_scene_by_name("game").save_models()
        SavingScene.go_back()
