import math
import pygame
from typing import List, Dict
from game_classes.match.cell_button import CellButton
from game_classes.match.hex_field import HexField
from game_classes.match.player import Player
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene_elements.button import Button
from gui_lib.scene_elements.event_system.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class HexFieldGuiElement(GuiElement, EventListener):
    def __init__(self,
                 hex_field: HexField,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 cell_default_painter: DescribedFigurePainter,
                 painter_by_player: Dict[Player, DescribedFigurePainter],
                 cell_on_click_func,
                 bg_size: Vector2,
                 bg_painters: List[DescribedFigurePainter]):
        """cell_on_click_func(CellButton button,
                              Event event,
                              int cell_index)"""

        center = (position
                  + Vector2(width_px / 2, 0)
                  + Vector2(0, height_px / 2))

        GuiElement.__init__(self,
                            RectangleFigure(center, bg_size, 0.0),
                            bg_painters)
        EventListener.__init__(self)

        # It allow to catch mouse click events on hex filed composite
        # and delegate them to cell buttons
        self.add_handler(pygame.MOUSEBUTTONDOWN, lambda *args: None)

        self.__field = hex_field
        self.__position = position
        self.__width_px = width_px
        self.__height_px = height_px

        self.__cells_buttons = []

        radius = min(self.__height_px
                     / (2 + 3 * (self.__field.height - 1) / 2),
                     2 * self.__width_px
                     / (3 ** (1 / 2) * (3 * self.__field.width - 1)))

        h = radius * 3 ** (1 / 2) / 2

        cells_geometry = list(
            self.__generate_cells_geometry_parameters(radius, h))

        first_cell_center = cells_geometry[0][0]
        last_cell_center = cells_geometry[-1][0]

        marker_1_figure = RectangleFigure(first_cell_center
                                          + Vector2(h
                                                    * (self.__field.height / 2
                                                       - 3),
                                                    self.__height_px / 2),
                                          Vector2(20, 20),
                                          math.pi / 3)
        marker_2_figure = RectangleFigure(last_cell_center
                                          + Vector2(-h * self.__field.width,
                                                    50),
                                          Vector2(20, 20),
                                          0)

        self.__markers = [
            Button(marker_1_figure, [
                DescribedFigurePainter(
                    RgbColors.WHITE,
                    RgbColors.WHITE,
                    RgbColors.WHITE,
                    1)
            ]),
            Button(marker_2_figure, [
                DescribedFigurePainter(
                    RgbColors.LIGHT_GREEN,
                    RgbColors.LIGHT_GREEN,
                    RgbColors.LIGHT_GREEN,
                    1)
            ])
        ]

        for marker in self.__markers:
            marker.label_builder.set_text("")

        for cell_geometry in cells_geometry:
            cell_center, cell_size, cell_rotation = cell_geometry

            cell_button = CellButton(cell_center,
                                     cell_size,
                                     cell_rotation,
                                     cell_default_painter)
            cell_button.label_builder.set_text(str(len(self.__cells_buttons)))

            cell_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                    HexFieldGuiElement.__attach_index(
                                        cell_on_click_func,
                                        len(self.__cells_buttons)))

            self.__cells_buttons.append(cell_button)

        def on_cell_owner_changing(cell_index: int,
                                   current_owner: Player,
                                   next_owner: Player):
            button = self.__cells_buttons[cell_index]
            button.set_painter(painter_by_player[next_owner])

        self.__field.add_on_cell_owner_changing(on_cell_owner_changing)

    def notify(self, event: Event):
        for button in self.__cells_buttons:
            button.notify(event)

    def is_valid_event(self, event: Event) -> bool:
        return True

    def update_on(self, surface: Surface):
        self.draw_current_state(surface)

        for marker in self.__markers:
            marker.update_on(surface)

        for button in self.__cells_buttons:
            button.update_on(surface)

    def __generate_cells_geometry_parameters(self, outside_radius, cell_h):

        # TODO: move radius and h to HexFigure attributes
        radius = outside_radius
        h = cell_h

        hex_field_offset_x = Vector2(self.__position.x, 0)
        hex_field_offset_y = Vector2(0, self.__position.y)
        last_center = (Vector2(h, radius)
                       + hex_field_offset_y
                       + hex_field_offset_x)

        for i in range(self.__field.height):
            for j in range(self.__field.width):
                yield (Vector2(last_center),
                       Vector2(radius, radius),
                       math.pi / 6)

                last_center += Vector2(2 * h, 0)
            last_center = (Vector2(h * (i + 2), last_center.y + 3 * radius / 2)
                           + hex_field_offset_x)

    @staticmethod
    def __attach_index(on_click_func, cell_index: int):
        def wrap(button: CellButton, event, index=cell_index):
            on_click_func(button, event, index)

        return wrap
