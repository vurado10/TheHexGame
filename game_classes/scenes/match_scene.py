from game_classes import environment
import pygame
from game_classes.ai.bot import Bot
from game_classes.color_theme import *
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.rating_system.rating_recorder import RatingRecorder
from game_classes.scenes.pause_scene import PauseScene
from game_classes.ai.bot_listener import BotListener
from game_classes.scenes.saving_scene import SavingScene
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.widgets.cell_button import CellButton
from game_classes.widgets.hex_field_widget import HexFieldWidget
from game_classes.widgets.widgets_factory import WidgetsFactory
from gui_lib import app, utilities
from gui_lib.interval_timer import IntervalTimer
from gui_lib.scene import Scene
from gui_lib.scene_elements.gui_elements.label import Label
from gui_lib.scene_elements.gui_elements.line import Line
from pygame.math import Vector2
from pygame.surface import Surface


class MatchScene(Scene):
    def __init__(self,
                 screen: Surface,
                 match: Match,
                 rating_recorder: RatingRecorder,
                 matches_repository: MatchesRepository,
                 ai_names: list[str],
                 bots: list[Bot] = None):
        super().__init__(screen)

        self.__match = match
        self.__ai_names = list(ai_names)

        self.__pause_button = None
        self.__move_owner_label = None
        self.__hex_field_gui_element = None
        self.__freeze_button = None
        self.__game_timer_label = None
        self.__move_timer_label = None

        self.__bots = list(bots) if bots is not None else []
        self.__label_update_timer = \
            IntervalTimer(0.2, self.update_timer_labels)
        self.__is_freeze = False
        self.__rating_recorder = rating_recorder
        self.__matches_rep = matches_repository

        self.add_gui_element(BotListener(self.__match))

        self.create_gui()

    @property
    def match(self):
        return self.__match

    def on_show(self):
        for bot in self.__bots:
            bot.unlock_sending_response()

        if not self.__match.has_timer():
            return

        if not self.__match.is_over():
            if self.__match.is_pause():
                self.__match.resume_game()
                self.__label_update_timer.resume()
            else:
                self.__match.start_game()
                self.__label_update_timer.start()

    def on_hide(self):
        self.freeze()

    def freeze(self):
        self.__is_freeze = True
        try:
            self.__match.pause_game()
        # TODO: create new exception class for timer errors
        except Exception:
            pass

        if self.__label_update_timer:
            self.__label_update_timer.pause()

        for bot in self.__bots:
            bot.lock_sending_response()

    def unfreeze(self):
        self.__is_freeze = False

        try:
            self.__match.resume_game()
        # TODO: create new exception class for timer errors
        except Exception:
            pass

        if self.__label_update_timer:
            self.__label_update_timer.resume()

        for bot in self.__bots:
            bot.unlock_sending_response()

    def update_move_owner_label(self, owner):
        turn_owner = owner
        self.__move_owner_label.set_font_color(turn_owner.color)
        self.__move_owner_label.set_text(
            f"Move: {turn_owner.name}")

    def update_timer_labels(self):
        game_time_text = \
            utilities.format_time("Game time",
                                  self.__match.get_remaining_game_sec())
        move_time_text = \
            utilities.format_time("Move time",
                                  self.__match.get_remaining_move_sec())

        self.__game_timer_label.set_text(game_time_text)
        self.__move_timer_label.set_text(move_time_text)

    def show_winner(self, winner: PlayerProfile, winner_path: list[int]):
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

    def create_gui(self):
        self.set_bg_color(SCENE_BG_COLOR)

        self.__create_pause_button()
        self.__create_labels()
        self.__create_field_widget()

        def on_stop():
            self.__move_owner_label.set_text("Game is over")
            self.__rating_recorder.save_ratings_for_players(self.__match)

        self.__match.add_on_game_over(on_stop)

        if self.__match.is_over():
            self.show_winner(self.__match.get_move_owner(),
                             self.__match.winner_path)
        else:
            self.__match.add_on_win(self.show_winner)

        if environment.FREEZE_BUTTON:
            self.__create_freeze_button()

        self.add_gui_elements([
            self.__pause_button,
            self.__move_owner_label,
            self.__game_timer_label,
            self.__move_timer_label,
            self.__hex_field_gui_element
        ])

    def __create_field_widget(self):
        def cell_on_click(button: CellButton,
                          event,
                          cell_index):
            move_owner = self.__match.get_move_owner().name

            if move_owner not in self.__ai_names:
                self.__match.make_move(cell_index, move_owner)

        self.__hex_field_gui_element = HexFieldWidget(
            self.__match,
            Vector2(180, 40),
            round(self.size[0] / 1.2),
            round(self.size[1] / 1.2),
            cell_on_click)

    def __create_pause_button(self):
        self.__pause_button = \
            WidgetsFactory.create_rect_button(Vector2(20, 10), "Pause menu")

        def on_switch_to_pause_menu(*args):
            title = ""
            pause_button_text = self.__pause_button.label.text.casefold()
            if pause_button_text == "pause menu":
                title = "Pause"
            elif pause_button_text == "continue":
                title = "Game is over"

            app.create_and_set_scene(
                "pause",
                PauseScene,
                title=title)

        self.__pause_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                        on_switch_to_pause_menu)

    def __create_labels(self):
        self.__move_owner_label = Label("")
        self.__move_owner_label.position = (self.__pause_button.position
                                            + Vector2(0, 200))

        self.__move_owner_label.set_font_size(20)

        self.update_move_owner_label(self.__match.get_move_owner())

        self.__match.add_on_switch_move_owner(
            lambda current, next_player:
            self.update_move_owner_label(next_player))

        last_label_position = self.__move_owner_label.position + Vector2(0, 50)
        self.__game_timer_label = \
            WidgetsFactory.create_label(last_label_position, "")

        last_label_position += Vector2(0, 25)
        self.__move_timer_label = \
            WidgetsFactory.create_label(last_label_position, "")

        self.update_timer_labels()

    def __create_freeze_button(self):
        self.__freeze_button = \
            WidgetsFactory.create_rect_button(Vector2(20, 70), "Freeze")

        def on_freeze_click(*args):
            if not self.__is_freeze:
                self.freeze()
                return
            self.unfreeze()

        self.__freeze_button.add_handler(pygame.MOUSEBUTTONDOWN,
                                         on_freeze_click)

        self.add_gui_element(self.__freeze_button)
