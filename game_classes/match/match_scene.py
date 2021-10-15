import pygame
from game_classes.color_theme import *
from game_classes.match.cell_button import CellButton
from game_classes.match.directions import Directions
from game_classes.match.engine import Engine
from game_classes.match.hex_field import HexField
from game_classes.match.hex_field_widget import HexFieldWidget
from game_classes.settings.hex_field_profile import HexFieldProfile
from game_classes.settings.player_profile import PlayerProfile
from gui_lib import app
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.abstract_button import AbstractButton
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.line import Line
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from pygame.math import Vector2
from pygame.surface import Surface


class MatchScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(SCENE_BG_COLOR)

        profile = HexFieldProfile(PlayerProfile("Player1", PLAYER1_COLOR),
                                  PlayerProfile("Player2", PLAYER2_COLOR),
                                  Directions.HORIZONTAL,
                                  Directions.VERTICAL,
                                  self._bg_color,
                                  RgbColors.BLACK,
                                  RgbColors.WHITE,
                                  0.7)

        self.__field = HexField(2, 2)
        self.__engine = Engine(self.__field,
                               profile.get_players_in_turn_order(),
                               profile.get_direction_by_player_dict())

        self.__pause_button = RectButton(Vector2(20, 10),
                                         round(3**(1 / 2) / 2 * 80),
                                         20,
                                         RgbColors.DARK_GREEN,
                                         RgbColors.DARK_BLUE)
        self.__pause_button.label.set_text("Pause")

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "pause"))

        self.__turn_owner_label = Label("", )
        self.__turn_owner_label.position = (self.__pause_button.position
                                            + Vector2(0, 100))

        self.__turn_owner_label.set_font_size(24)

        self.update_move_owner_label()

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__engine.make_move(cell_index)
            self.update_move_owner_label()

        self.__hex_field_gui_element = HexFieldWidget(
            self.__field,
            Vector2(180, 40),
            round(self.size[0] / 1.2),
            round(self.size[1] / 1.2),
            profile,
            cell_on_click)

        def on_win(winner: PlayerProfile, winner_path: list[int]):
            if len(winner_path) > 1:
                path_centers = list(
                    map(lambda i:
                        self
                        .__hex_field_gui_element
                        .get_cell_by_index(i)
                        .center,
                        winner_path))
                (self
                 .__hex_field_gui_element
                 .add_child(Line(path_centers, WIN_LINE_COLOR)))
            self.__pause_button.hide()
            self.__turn_owner_label.label_builder.set_font_color(
                winner.color)
            self.__turn_owner_label.label_builder.set_text(
                f"Winner: {winner.name}")

        self.__engine.add_on_win(on_win)

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__turn_owner_label)
        self.add_gui_element(self.__hex_field_gui_element)

    def update_move_owner_label(self):
        if self.__engine.is_game_over():
            return

        turn_owner = self.__engine.get_turn_owner()
        self.__turn_owner_label.label_builder.set_font_color(turn_owner.color)
        self.__turn_owner_label.label_builder.set_text(
            f"Turn: {turn_owner.name}")
