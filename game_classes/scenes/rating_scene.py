from game_classes.scenes.scene_with_list import SceneWithList
from pygame.surface import Surface


class RatingScene(SceneWithList):
    def __init__(self, screen: Surface):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        super().__init__(screen,
                         "main menu",
                         MainMenuScene,
                         ["player" + str(i)
                          for i in range(6)])