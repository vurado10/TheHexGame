import pygame
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from gui_lib.scene_elements.gui_elements.toggle_button import ToggleButton
from gui_lib.scene_elements.gui_elements.toggles_sync_container import \
    TogglesSyncContainer
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class ListView(Widget):
    def __init__(self,
                 position: Vector2,
                 width_px: int = 300,
                 values: list[str] = None,
                 page_length: int = 10,
                 active_item_color: RgbColor = RgbColors.BLACK,
                 inactive_item_color: RgbColor = RgbColors.WHITE):
        super().__init__(position, [pygame.MOUSEBUTTONDOWN])

        self.__height_px = 0
        self.__width_px = width_px
        self.__current_page = 0
        self.__page_length = page_length
        self.__chosen_value = None
        self.__value_index_by_item_index = {}

        self.__prev_button = RectButton(Vector2(),
                                        80,
                                        25,
                                        active_item_color,
                                        inactive_item_color,
                                        "Previous")

        self.__next_button = RectButton(Vector2(100, 0),
                                        80,
                                        25,
                                        active_item_color,
                                        inactive_item_color,
                                        "Next")

        self.__prev_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       self.go_to_prev_page)

        self.__next_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                       self.go_to_next_page)

        self.__values = [] if values is None else list(values)
        self.__items = []
        space_between_items = 5
        last_position = Vector2()
        for i in range(self.__page_length):
            button = ToggleButton("", last_position,
                                  self.__width_px, 25,
                                  active_item_color, inactive_item_color)
            self.__value_index_by_item_index[i] = i
            self.__items.append(button)

            button.add_handler(pygame.MOUSEBUTTONDOWN,
                               lambda *args: self.set_chosen_value())

            last_position += Vector2(0, button.height + space_between_items)

        self.__height_px = round(last_position.y - space_between_items)

        try:
            self.set_page(self.__current_page)
        except ValueError:
            pass

        sync_container = TogglesSyncContainer(self.__width_px,
                                              self.__height_px,
                                              self.__items)

        sync_container.position = Vector2(self.__prev_button.position.x,
                                self.__next_button.position.y
                                + self.__next_button.height
                                + 15)

        sync_container.add_handler(pygame.MOUSEBUTTONDOWN,
                                   lambda *args: self.unset_chosen_value())

        self.add_children([self.__prev_button, self.__next_button])
        self.add_child(sync_container)

    @property
    def width(self) -> int:
        return self.__width_px

    @property
    def height(self) -> int:
        return self.__height_px

    def unset_chosen_value(self):
        self.__chosen_value = None

    def set_chosen_value(self):
        for index, item in enumerate(self.__items):
            if item.is_active():
                self.__chosen_value = self.__value_index_by_item_index[index]
                return

    def get_chosen_value(self) -> [None, str]:
        return self.__chosen_value

    def set_page(self, page_index: int):
        if page_index < 0:
            raise ValueError(f"page_index must be non negative,"
                             f" but was: {page_index}")

        first_value_index = page_index * self.__page_length

        values = self.__values[first_value_index:
                               first_value_index + self.__page_length]

        if not values:
            raise ValueError(f"No page with index: {page_index}")

        self.unset_chosen_value()
        for index, item in enumerate(self.__items):
            self.__value_index_by_item_index[index] = first_value_index + index
            item.deactivate()
            item.hide()

        for index, value in enumerate(values):
            self.__items[index].set_text(value)
            self.__items[index].show()

    def go_to_prev_page(self, *args):
        try:
            self.set_page(self.__current_page - 1)
            self.__current_page -= 1
        except ValueError:
            pass

    def go_to_next_page(self, *args):
        try:
            self.set_page(self.__current_page + 1)
            self.__current_page += 1
        except ValueError:
            pass

    def is_valid_event(self, event: Event) -> bool:
        return True
