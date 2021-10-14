import pygame
from game_classes.color_theme import *
from game_classes.match.cell_button import CellButton
from game_classes.match.directions import Directions
from game_classes.match.engine import Engine
from game_classes.match.hex_field import HexField
from game_classes.match.hex_field_gui_element import HexFieldGuiElement
from game_classes.settings.hex_field_profile import HexFieldProfile
from game_classes.settings.player_profile import PlayerProfile
from gui_lib import app
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from gui_lib.scene_elements.label import Label
from gui_lib.scene_elements.line import Line
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

        self.__field = HexField(4, 4)
        self.__judge = Engine(self.__field,
                              profile.get_players_in_turn_order(),
                              profile.get_direction_by_player_dict())

        self.__pause_button = Button(RectangleFigure(Vector2(50, 40),
                                                     Vector2(40, 40),
                                                     0),
                                     [DescribedFigurePainter(
                                         RgbColors.DARK_GREEN,
                                         RgbColors.BLACK,
                                         RgbColors.DARK_GREEN,
                                         1)])
        self.__pause_button.label_builder.set_text("Pause")
        self.__pause_button.label_builder.set_font_color(RgbColors.DARK_BLUE)
        self.__pause_button.label_builder.set_font_size(20)

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "pause"))

        self.__turn_owner_label = Label(RectangleFigure(self
                                                        .__pause_button
                                                        .center
                                                        + Vector2(25, 100),
                                                        Vector2(),
                                                        0.0),
                                        [DescribedFigurePainter(
                                            self._bg_color,
                                            self._bg_color,
                                            self._bg_color,
                                            1.0)])
        self.__turn_owner_label.label_builder.set_font_color(
            RgbColors.DARK_GREEN)
        self.__turn_owner_label.label_builder.set_font_size(24)

        self.update_turn_owner_label()

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__judge.make_move(cell_index)
            self.update_turn_owner_label()

        self.__hex_field_gui_element = HexFieldGuiElement(
            self.__field,
            Vector2(225, 50),
            round(self.size[0] / 1.3),
            round(self.size[1] / 1.3),
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
                 .add_child_gui_element(Line(path_centers, WIN_LINE_COLOR)))
            # app.set_current_scene("game over")

        self.__judge.add_on_win(on_win)

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__turn_owner_label)
        self.add_gui_element(self.__hex_field_gui_element)

    def update_turn_owner_label(self):
        turn_owner = self.__judge.get_turn_owner()
        self.__turn_owner_label.label_builder.set_font_color(turn_owner.color)
        self.__turn_owner_label.label_builder.set_text(
            f"Turn: {turn_owner.name}")
