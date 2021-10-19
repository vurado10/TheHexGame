from game_classes import color_theme
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib.scene import Scene
from pygame.math import Vector2
from pygame.surface import Surface


class SceneWithList(Scene):
    def __init__(self,
                 screen: Surface,
                 prev_scene_name: str,
                 prev_scene_type,
                 values):
        super().__init__(screen)

        self.set_bg_color(color_theme.SCENE_BG_COLOR)

        self._list_view = WidgetsFactory.create_list_view(Vector2(100, 30),
                                                          values)

        self._back_button = \
            WidgetsFactory.create_scene_switcher_button(Vector2(100, 460),
                                                        "Back",
                                                        prev_scene_name,
                                                        prev_scene_type)

        self.add_gui_elements([
            self._list_view,
            self._back_button
        ])
