import math
import pygame
from game_classes import color_theme
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.widgets.arrow_widget import ArrowWidget
from game_classes.widgets.cell_button import CellButton
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_color import RgbColor
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class HexFieldWidget(Widget):
    def __init__(self,
                 match: Match,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 cell_on_click_func):
        """cell_on_click_func(CellButton button,
                              Event event,
                              int cell_index)"""
        super().__init__(position, [pygame.MOUSEBUTTONDOWN])

        self.__match = match
        self.__field = self.__match.field

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
            ArrowWidget(
                self._position + Vector2(cells_geometry[0][0].x, 0) + offset1,
                cells_geometry[self.__field.width - 1][0]
                - cells_geometry[0][0],
                self.__get_color_by_direction(Directions.HORIZONTAL))
        ]

        cell_default_painter = HexagonPainter(
            color_theme.CELL_BG,
            color_theme.CELL_BORDER,
            color_theme.CELL_BG,
            0.9)

        self.__cell_by_index = {}

        painter_by_player_name = {
            self.__match.get_player(0).name:
                HexFieldWidget.__create_painter_for_player(
                    color_theme.PLAYER1_COLOR),
            self.__match.get_player(1).name:
                HexFieldWidget.__create_painter_for_player(
                    color_theme.PLAYER2_COLOR),
        }

        for cell_geometry in cells_geometry:
            cell_center, cell_size, cell_rotation = cell_geometry

            cell_button = CellButton(cell_center,
                                     cell_size,
                                     cell_rotation,
                                     self.position)

            index = len(self.__cells_buttons)
            self.__cell_by_index[index] = cell_button

            if self.__match.field.is_occupied(index):
                painter = painter_by_player_name[
                    self.__match.field.get_owner(index).name]
                cell_button.set_painter(painter)
            else:
                cell_button.set_painter(cell_default_painter)

            cell_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                    HexFieldWidget.__attach_index(
                                        cell_on_click_func,
                                        index))

            self.__cells_buttons.append(cell_button)

        def on_cell_owner_changing(cell_index: int,
                                   current_owner: PlayerProfile,
                                   next_owner: PlayerProfile):
            button = self.__cells_buttons[cell_index]
            button.set_painter(painter_by_player_name[next_owner.name])

        self.__field.add_on_cell_owner_changing(on_cell_owner_changing)

        self.add_children(self.__cells_buttons)
        self.add_children(self.__markers)

    def get_cell_by_index(self, index):
        return self.__cell_by_index[index]

    def update_self_on(self, surface: Surface):
        pass

    def is_valid_event(self, event: Event) -> bool:
        return True

    def __get_color_by_direction(self, direction: int):
        player_name = self.__match.get_player_by_direction(direction).name

        if self.__match.get_move_order_index_by_player_name(
                player_name) == 0:
            return color_theme.PLAYER1_COLOR

        return color_theme.PLAYER2_COLOR

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
    def __create_painter_for_player(player_color: RgbColor,
                                    padding_factor=0.8):
        return HexagonPainter(
                color_theme.CELL_BG,
                color_theme.CELL_BORDER,
                player_color,
                padding_factor)

    @staticmethod
    def __attach_index(on_click_func, cell_index: int):
        def wrap(button: CellButton, event, index=cell_index):
            on_click_func(button, event, index)

        return wrap
