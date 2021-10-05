import pygame
from game_classes.match.cell_button import CellButton
from game_classes.match.hex_field import HexField
from game_classes.match.hex_field_gui_element import HexFieldGuiElement
from game_classes.match.judge import Judge
from game_classes.match.player import Player
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

        players = [Player("Player1"), Player("Player2")]

        self.__field = HexField(11, 11)
        self.__judge = Judge(self.__field,
                             players)

        hex_field_bg_painter = DescribedFigurePainter(RgbColors.BLACK,
                                               RgbColors.BLACK,
                                               RgbColors.BLACK,
                                               1)

        neutral_state = DescribedFigurePainter(RgbColors.BLACK,
                                               RgbColors.WHITE,
                                               RgbColors.BLACK,
                                               0.9)

        player1_state = DescribedFigurePainter(RgbColors.BLACK,
                                               RgbColors.WHITE,
                                               RgbColors.WHITE,
                                               0.7)

        player2_state = DescribedFigurePainter(RgbColors.BLACK,
                                               RgbColors.WHITE,
                                               RgbColors.LIGHT_GREEN,
                                               0.7)

        painter_by_player = {
            players[0]: player1_state,
            players[1]: player2_state
        }

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__judge.make_turn(cell_index)

        self.__hex_field_gui_element = HexFieldGuiElement(
            self.__field,
            Vector2(225, 50),
            round(self.size[0] / 1.3),
            round(self.size[1] / 1.3),
            neutral_state,
            painter_by_player,
            cell_on_click,
            Vector2(50, 50),
            [hex_field_bg_painter]
        )

        self.__pause_button = Button(RectangleFigure(Vector2(50, 40),
                                                     Vector2(40, 40), 0),
                                     [DescribedFigurePainter(
                                         RgbColors.LIGHT_GREEN,
                                         RgbColors.BLACK,
                                         RgbColors.LIGHT_GREEN,
                                         1)])
        self.__pause_button.label_builder.set_text("Pause")
        self.__pause_button.label_builder.set_font_color(RgbColors.BLACK)
        self.__pause_button.label_builder.set_font_size(24)

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "pause"))

        def on_win(winner: Player):
            self.__pause_button.label_builder.set_text("Win!")

        self.__judge.add_on_win(on_win)

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__hex_field_gui_element)
