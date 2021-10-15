import math
import pygame
from game_classes.match.arrow_gui_element import ArrowGuiElement
from game_classes.match.cell_button import CellButton
from game_classes.match.directions import Directions
from game_classes.match.hex_field import HexField
from game_classes.settings.hex_field_profile import HexFieldProfile
from game_classes.settings.player_profile import PlayerProfile
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class HexFieldWidget(Widget):
    def __init__(self,
                 hex_field: HexField,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 profile: HexFieldProfile,
                 cell_on_click_func):
        """cell_on_click_func(CellButton button,
                              Event event,
                              int cell_index)"""
        super().__init__(position, [pygame.MOUSEBUTTONDOWN])

        self.__field = hex_field

        self.__cells_buttons = []

        self._height_px = height_px
        self._width_px = width_px

        radius = min(self._height_px
                     / (2 + 3 * (self.__field.height - 1) / 2),
                     2 * self._width_px
                     / (3 ** (1 / 2) * (3 * self.__field.width - 1)))

        h = radius * 3 ** (1 / 2) / 2

        cells_geometry = list(
            self.__generate_cells_geometry_parameters(radius, h))

        offset1 = Vector2(0, -20)

        self.__markers = [
            ArrowGuiElement(
                self._position + Vector2(cells_geometry[0][0].x, 0) + offset1,
                cells_geometry[self.__field.width - 1][0]
                - cells_geometry[0][0],
                profile.get_player_by_direction(Directions.HORIZONTAL).color,
                profile.bg_color)
        ]

        cell_default_painter = HexagonPainter(
            profile.bg_color_cell,
            profile.border_color_cell,
            profile.bg_color_cell,
            0.9)

        self.__cell_by_index = {}

        for cell_geometry in cells_geometry:
            cell_center, cell_size, cell_rotation = cell_geometry

            cell_button = CellButton(cell_center,
                                     cell_size,
                                     cell_rotation)

            cell_button.set_painter(cell_default_painter)

            index = len(self.__cells_buttons)
            self.__cell_by_index[index] = cell_button

            cell_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                    HexFieldWidget.__attach_index(
                                        cell_on_click_func,
                                        index))

            self.__cells_buttons.append(cell_button)

        painter_by_player = {
            profile.get_player(0):
                profile.get_painter_for_player(profile.get_player(0)),
            profile.get_player(1):
                profile.get_painter_for_player(profile.get_player(1))
        }

        def on_cell_owner_changing(cell_index: int,
                                   current_owner: PlayerProfile,
                                   next_owner: PlayerProfile):
            button = self.__cells_buttons[cell_index]
            button.set_painter(painter_by_player[next_owner])

        self.__field.add_on_cell_owner_changing(on_cell_owner_changing)

        # self.add_children_elements(self.__markers)
        self.add_children(self.__cells_buttons)

    def get_cell_by_index(self, index):
        return self.__cell_by_index[index]

    def __generate_cells_geometry_parameters(self, outside_radius, cell_h):

        # TODO: move radius and h to HexFigure attributes
        radius = outside_radius
        h = cell_h

        last_center = (Vector2(h, radius))

        for i in range(self.__field.height):
            for j in range(self.__field.width):
                yield (Vector2(last_center),
                       Vector2(radius, radius),
                       math.pi / 6)

                last_center += Vector2(2 * h, 0)
            last_center = Vector2(h * (i + 2), last_center.y + 3 * radius / 2)

    @staticmethod
    def __attach_index(on_click_func, cell_index: int):
        def wrap(button: CellButton, event, index=cell_index):
            on_click_func(button, event, index)

        return wrap

    def update_self_on(self, surface: Surface):
        pass

    def is_valid_event(self, event: Event) -> bool:
        return True