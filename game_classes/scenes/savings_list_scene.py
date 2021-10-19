import pygame
from game_classes import color_theme
from game_classes.scenes.scene_with_list import SceneWithList
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from gui_lib.scene import Scene
from pygame.math import Vector2
from pygame.surface import Surface


class SavingsListScene(SceneWithList):
    def __init__(self, screen: Surface):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        super().__init__(screen,
                         "main menu",
                         MainMenuScene,
                         ["item" + str(i)
                          for i in range(57)])

        self.__loading_button = \
            WidgetsFactory.create_rect_button(Vector2(230, 460),
                                              "Load")

        self.__loading_button.add_handler(pygame.MOUSEBUTTONDOWN, self.load)

        self.add_gui_element(self.__loading_button)

    def load(self, *args):
        print(f"Loading {self._list_view.get_chosen_value()}")
