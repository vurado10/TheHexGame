from game_classes.color_theme import (
    BUTTON_BG_COLOR,
    BUTTON_TEXT_COLOR,
    SCENE_BG_COLOR
)
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from pygame.math import Vector2
from pygame.surface import Surface


class MenuScene(Scene):
    def __init__(self,
                 screen: Surface,
                 title: str = "",
                 buttons_titles: list[str] = None):
        super().__init__(screen)

        self.set_bg_color(SCENE_BG_COLOR)

        element_x = 100
        title_font_size = 56
        title_margin_top = 60
        title_margin_bottom = 40
        button_margin_bottom = 15
        self._buttons_size = (100, 50)

        self._title = Label(title, font_size=title_font_size)
        self._title.position = Vector2(element_x, title_margin_top)
        self.add_gui_element(self._title)

        if buttons_titles is None:
            buttons_titles = []

        self._buttons = {}
        button_y = (self._title.position.y
                    + self._title.height
                    + title_margin_bottom)
        for button_title in buttons_titles:
            button = self.create_button(Vector2(element_x, button_y),
                                        button_title)

            self.add_gui_element(button)
            self._buttons[button_title] = button

            button_y += button.height + button_margin_bottom

    def create_button(self, position: Vector2, text: str):
        return RectButton(position,
                          self._buttons_size[0],
                          self._buttons_size[1],
                          bg_color=BUTTON_BG_COLOR,
                          text_color=BUTTON_TEXT_COLOR,
                          text=text)
