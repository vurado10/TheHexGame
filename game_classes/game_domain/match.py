import math
import threading
from game_classes import environment
from typing import List, Dict
from gui_lib import utilities
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.player_profile import PlayerProfile
from gui_lib.interval_timer import IntervalTimer


class Match:
    """Game match model"""
    def __init__(self,
                 game_id: str,
                 field: HexField,
                 players: List[PlayerProfile],
                 direction_by_player_name: Dict[str, int],
                 time_for_game: float = math.inf,
                 time_for_move: float = math.inf):
        """first player - horizontal moving, second player - vertical moving"""
        if len(players) != 2:
            raise ValueError(
                "players list must have 2 Player objects")

        if players[0].name == players[1].name:
            raise ValueError("players must have different names, "
                             f"but their names are: {players[0].name}")

        # TODO: can't get private fields when deserialization,
        #  so they are protected
        self._game_id = game_id
        self._field = field
        self._players = list(players)
        self._direction_by_player_name = dict(direction_by_player_name)
        self._current_player_index = 0
        self._is_over = False
        self._is_pause = False
        self._is_starting = False
        self._winner_path = []

        self._on_switch_move_owner_funcs = []
        self._on_game_over_funcs = []
        self._on_win_funcs = []

        self.__timer = None
        self.__remaining_game_sec = time_for_game
        self.__time_for_game = time_for_game
        self.__time_for_move = time_for_move
        self.__remaining_move_sec = self.__time_for_move

        if self.has_timer():
            self.__timer = IntervalTimer(1.0,
                                         lambda: self.handle_timer_tick(1.0))
            if environment.LOG:
                print(f"Match generated: {self.__timer.thread.name}")

    @property
    def game_id(self) -> str:
        return self._game_id

    @property
    def field(self) -> HexField:
        return self._field

    @property
    def winner_path(self):
        return list(self._winner_path)

    def get_player_by_name(self, name):
        if self._players[0].name == name:
            return self._players[0]
        elif self._players[1].name == name:
            return self._players[1]

        raise ValueError(f"No player in match with name: {name}")

    def has_winner(self):
        return len(self._winner_path) != 0

    def get_start_cells_by_direction(self, direction: int):
        if direction == Directions.HORIZONTAL:
            return self._field.get_all_cells_in_column(0)
        elif direction == Directions.VERTICAL:
            return self._field.get_all_cells_in_row(0)

        raise ValueError(f"No start cells for direction: {direction}")

    def get_stop_cells_by_direction(self, direction: int):
        if direction == Directions.HORIZONTAL:
            return self._field.get_all_cells_in_column(self._field.width - 1)
        if direction == Directions.VERTICAL:
            return self._field.get_all_cells_in_row(self._field.height - 1)

        raise ValueError(f"No stop cells for direction: {direction}")

    def handle_timer_tick(self, interval):
        self.__remaining_game_sec -= interval
        if environment.LOG:
            print(f"on tick {threading.current_thread().name} "
                  f"{self.__remaining_game_sec}\n")
        self.__remaining_move_sec -= interval

        if self.__remaining_game_sec < 1e-5:
            self.stop_game()
            return

        if self.__remaining_move_sec < 1e-5:
            self.__remaining_move_sec = self.__time_for_move
            self.switch_move_owner()

    def get_players_in_turn_order(self):
        return list(self._players)

    def get_direction_by_player_name_dict(self):
        return dict(self._direction_by_player_name)

    def get_player_by_direction(self, direction: int):
        if self._direction_by_player_name[self._players[0].name] == direction:
            return self._players[0]
        elif (self._direction_by_player_name[self._players[1].name]
              == direction):
            return self._players[1]

    # TODO: code repeating
    def get_move_order_by_direction(self, direction: int):
        if self._direction_by_player_name[self.get_player(0).name] \
                == direction:
            return 0
        elif self._direction_by_player_name[self.get_player(1).name] \
                == direction:
            return 1

    def get_player(self, move_order_index: int) -> PlayerProfile:
        return self._players[move_order_index]

    def get_current_move_order_index(self):
        return self._current_player_index

    def get_move_order_index_by_player_name(self, name):
        if self._players[0].name == name:
            return 0
        elif self._players[1].name == name:
            return 1

        raise ValueError(f"No player with name {name}")

    def add_on_switch_move_owner(self, func):
        """func(Player current_player, Player next_player)"""
        self._on_switch_move_owner_funcs.append(func)

    def add_on_win(self, func):
        """func(Player winner, list[Vector2] winner_path)"""
        self._on_win_funcs.append(func)

    def add_on_game_over(self, func):
        """func()"""
        self._on_game_over_funcs.append(func)

    def has_timer(self):
        return (self.__time_for_game < math.inf
                or self.__time_for_move < math.inf)

    def is_over(self):
        return self._is_over

    def switch_move_owner(self):
        prev_index = self._current_player_index
        self._current_player_index = \
            (self._current_player_index + 1) % len(self._players)

        self.__remaining_move_sec = self.__time_for_move

        utilities.execute_all_funcs(self._on_switch_move_owner_funcs,
                                    self._players[prev_index],
                                    self._players[
                                        self._current_player_index])

    def is_valid_move(self, cell_index, player_name):
        current_player = self._players[self._current_player_index]
        if (self._is_over
                or self._field.is_occupied(cell_index)
                or current_player.name != player_name):
            return False

        return True

    def make_move(self, cell_index, player_name: str) -> bool:
        # TODO: is_over must be here
        if not self.is_valid_move(cell_index, player_name):
            return False

        self._field.set_owner(cell_index,
                              self._players[self._current_player_index])

        self.try_register_win()

        if not self.is_over():
            self.switch_move_owner()

        return True

    def try_register_win(self):
        winner_path = self.get_winner_path()

        if winner_path:
            self.register_win(self.get_move_owner(), winner_path)

    def get_winner_path(self):
        current_direction = \
            self._direction_by_player_name[self.get_move_owner().name]

        start_cells = self.get_start_cells_by_direction(current_direction)
        stop_cells = self.get_stop_cells_by_direction(current_direction)

        for start_cell in start_cells:
            path_for_owner = self._field.get_path_for_owner(
                self.get_move_owner(),
                start_cell,
                set(stop_cells))

            if len(path_for_owner) != 0:
                return path_for_owner

        return []

    def is_pause(self):
        return self._is_pause

    def start_game(self):
        if self.is_over():
            raise Exception("Game is over")

        if self.is_pause():
            raise Exception("Game on pause")

        if self._is_starting:
            raise Exception("Can't start a game twice")

        if self.__timer:
            self._is_starting = True
            self.__timer.start()
        else:
            raise Exception("No any timers in the game")

    def stop_game(self):
        if self.is_over():
            raise Exception("Game is over")

        self._is_over = True
        self._is_pause = False

        if self.__timer:
            self.__timer.pause()

        self.try_register_win()

        utilities.execute_all_funcs(self._on_game_over_funcs)

    def pause_game(self):
        if self.__timer:
            self._is_pause = True
            self.__timer.pause()
        else:
            raise Exception("No timer in match")

    def resume_game(self):
        if self.__timer:
            self._is_pause = False
            self.__timer.resume()
        else:
            raise Exception("No timer in match")

    def get_remaining_game_sec(self) -> float:
        return self.__remaining_game_sec

    def get_remaining_move_sec(self) -> float:
        return self.__remaining_move_sec

    def register_win(self, winner: PlayerProfile, winner_path: list):
        if not self.is_over():
            self.stop_game()

        self._winner_path = winner_path
        utilities.execute_all_funcs(self._on_win_funcs,
                                    winner,
                                    winner_path)

    def get_move_owner(self) -> PlayerProfile:
        return self._players[self._current_player_index]
