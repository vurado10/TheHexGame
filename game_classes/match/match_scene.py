import pygame
from game_classes.match.cell_button import CellButton
from game_classes.match.directions import Directions
from game_classes.match.hex_field import HexField
from game_classes.match.hex_field_gui_element import HexFieldGuiElement
from game_classes.match.judge import Judge
from game_classes.settings.hex_field_profile import HexFieldProfile
from game_classes.settings.player_profile import PlayerProfile
from gui_lib import app
from gui_lib.figures.rectangle_figure import RectangleFigure
from gui_lib.painters.described_figure_painter import DescribedFigurePainter
from gui_lib.rgb_colors import RgbColors
from gui_lib.scene import Scene
from gui_lib.scene_elements.button import Button
from pygame.math import Vector2
from pygame.surface import Surface


class MatchScene(Scene):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        self.set_bg_color(RgbColors.DARK_BLUE)

        profile = HexFieldProfile(PlayerProfile("Player1",
                                                RgbColors.WHITE),
                                  PlayerProfile("Player2",
                                                RgbColors.LIGHT_GREEN),
                                  Directions.HORIZONTAL,
                                  Directions.VERTICAL,
                                  self.get_bg_color(),
                                  RgbColors.BLACK,
                                  RgbColors.WHITE,
                                  0.7)

        self.__field = HexField(11, 11)
        self.__judge = Judge(self.__field,
                             profile.get_players_in_turn_order(),
                             profile.get_direction_by_player_dict())

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__judge.make_turn(cell_index)

        self.__hex_field_gui_element = HexFieldGuiElement(
            self.__field,
            Vector2(225, 50),
            round(self.size[0] / 1.3),
            round(self.size[1] / 1.3),
            profile,
            cell_on_click)

        self.__pause_button = Button(RectangleFigure(Vector2(50, 40),
                                                     Vector2(40, 40), 0),
                                     [DescribedFigurePainter(
                                         RgbColors.LIGHT_GREEN,
                                         RgbColors.BLACK,
                                         RgbColors.LIGHT_GREEN,
                                         1)])
        self.__pause_button.label_builder.set_text("Pause")
        self.__pause_button.label_builder.set_font_color(RgbColors.WHITE)
        self.__pause_button.label_builder.set_font_size(24)

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "pause"))

        def on_win(winner: PlayerProfile):
            self.__pause_button.label_builder.set_text(f"winner: {winner.name}")

        self.__judge.add_on_win(on_win)

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__hex_field_gui_element)
