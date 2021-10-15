from game_classes.color_theme import (
    BUTTON_BG_COLOR,
    BUTTON_TEXT_COLOR,
    SCENE_BG_COLOR
)
from gui_lib import app
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from gui_lib.scene_elements.gui_elements.label import Label
from pygame.math import Vector2
from pygame.surface import Surface


class MenuScene(Scene):
    def __init__(self,
                 screen: Surface,
                 title: str = "",
                 buttons_titles: list[str] = None):
        super().__init__(screen)

        self.set_bg_color(SCENE_BG_COLOR)

        element_center_x = app.screen.get_width() / 2
        title_font_size = 56
        title_margin_top = 110
        title_margin_bottom = 40
        button_size = Vector2(50, 50)
        button_margin_bottom = 15

        self._title = Label.create(title, font_size=title_font_size)
        self._title.center = Vector2(element_center_x, title_margin_top)
        self.add_gui_element(self._title)

        if buttons_titles is None:
            buttons_titles = []

        self._buttons = {}
        button_center_y = (self._title.center.y
                           + title_font_size * 1.338307 / 2
                           + title_margin_bottom
                           + button_size.x / 2)
        for button_title in buttons_titles:
            button_center = Vector2(element_center_x, button_center_y)

            button = AbstractButton.create(button_title,
                                           button_size,
                                           bg_color=BUTTON_BG_COLOR,
                                           font_color=BUTTON_TEXT_COLOR)
            button.center = button_center
            self.add_gui_element(button)
            self._buttons[button_title] = button

            button_center_y += button_size.x + button_margin_bottom
