import pygame
from game_classes.color_theme import *
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.scenes.settings.hex_field_profile import HexFieldProfile
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.widgets.cell_button import CellButton
from game_classes.widgets.hex_field_widget import HexFieldWidget
from gui_lib import app
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.line import Line
from gui_lib.scene_elements.gui_elements.rect_button import RectButton
from pygame.math import Vector2
from pygame.surface import Surface


class MatchScene(Scene):
    def __init__(self,
                 screen: Surface,
                 matches_repository: MatchesRepository,
                 match_id: int):
        super().__init__(screen)

        self.__match = matches_repository.get_by_id(match_id)
        self.__pause_button = None
        self.__turn_owner_label = None
        self.__hex_field_gui_element = None

        # self.load_models()
        self.load_gui()

    def update_move_owner_label(self):
        if self.__match.is_over():
            return

        turn_owner = self.__match.get_turn_owner()
        self.__turn_owner_label.set_font_color(turn_owner.color)
        self.__turn_owner_label.set_text(
            f"Turn: {turn_owner.name}")

    # def load_models(self):
    #     player1 = PlayerProfile("Player1", PLAYER1_COLOR)
    #     player2 = PlayerProfile("Player2", PLAYER2_COLOR)
    #
    #     self.__match = Match(HexField(11, 11),
    #                          [player1, player2],
    #                          {player1: Directions.HORIZONTAL,
    #                           player2: Directions.VERTICAL}, "1")

    def load_gui(self):
        players = self.__match.get_players_in_turn_order()
        directions = self.__match.get_direction_by_player_name_dict()

        profile = HexFieldProfile(players[0],
                                  players[1],
                                  directions[players[0]],
                                  directions[players[1]],
                                  self._bg_color,
                                  RgbColors.BLACK,
                                  RgbColors.WHITE,
                                  0.7)

        self.set_bg_color(SCENE_BG_COLOR)

        self.__pause_button = RectButton(Vector2(20, 10),
                                         90,
                                         50,
                                         RgbColors.DARK_GREEN,
                                         RgbColors.DARK_BLUE)
        self.__pause_button.label.set_text("Pause")

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.set_current_scene(
                                            "pause"))

        self.__turn_owner_label = Label("")
        self.__turn_owner_label.position = (self.__pause_button.position
                                            + Vector2(0, 100))

        self.__turn_owner_label.set_font_size(24)

        self.update_move_owner_label()

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__match.make_move(cell_index)
            self.update_move_owner_label()

        self.__hex_field_gui_element = HexFieldWidget(
            self.__match.field,
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
            self.__pause_button.label.set_text("Continue")
            self.__turn_owner_label.set_font_color(
                winner.color)
            self.__turn_owner_label.set_text(
                f"Winner: {winner.name}")

        self.__match.add_on_win(on_win)
        self.__match.try_register_win()

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__turn_owner_label)
        self.add_gui_element(self.__hex_field_gui_element)
