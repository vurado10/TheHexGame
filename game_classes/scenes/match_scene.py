import pygame
from game_classes.color_theme import *
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.scenes.pause_scene import PauseScene
from game_classes.widgets.cell_button import CellButton
from game_classes.widgets.hex_field_widget import HexFieldWidget
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.line import Line
from pygame.math import Vector2
from pygame.surface import Surface


class MatchScene(Scene):
    def __init__(self,
                 screen: Surface,
                 match: Match):
        super().__init__(screen)

        self.__match = match
        self.__pause_button = None
        self.__move_owner_label = None
        self.__hex_field_gui_element = None

        self.load_gui()

    def update_move_owner_label(self, owner):
        turn_owner = owner
        self.__move_owner_label.set_font_color(turn_owner.color)
        self.__move_owner_label.set_text(
            f"Move: {turn_owner.name}")

    def load_gui(self):
        self.set_bg_color(SCENE_BG_COLOR)

        self.__pause_button = \
            WidgetsFactory.create_rect_button(Vector2(20, 10), "Pause")

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        lambda *args: app.create_and_set_scene(
                                            "pause",
                                            PauseScene,
                                            title="It's not pause menu"))

        self.__move_owner_label = Label("")
        self.__move_owner_label.position = (self.__pause_button.position
                                            + Vector2(0, 200))

        self.__move_owner_label.set_font_size(20)

        self.update_move_owner_label(self.__match.get_move_owner())

        self.__match.add_on_switch_move_owner(
            lambda current, next_player:
            self.update_move_owner_label(next_player))

        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            self.__match.make_move(cell_index)

        self.__hex_field_gui_element = HexFieldWidget(
            self.__match,
            Vector2(180, 40),
            round(self.size[0] / 1.2),
            round(self.size[1] / 1.2),
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
            self.__pause_button.set_text("Continue")
            self.__move_owner_label.set_font_color(
                winner.color)
            self.__move_owner_label.set_text(
                f"Winner: {winner.name}")

        self.__match.add_on_win(on_win)
        self.__match.try_register_win()

        self.add_gui_element(self.__pause_button)
        self.add_gui_element(self.__move_owner_label)
        self.add_gui_element(self.__hex_field_gui_element)
