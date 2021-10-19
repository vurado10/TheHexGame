from typing import List, Dict
from gui_lib import utilities
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.player_profile import PlayerProfile


class Match:
    """Game match model"""
    def __init__(self,
                 game_id: str,
                 field: HexField,
                 players: List[PlayerProfile],
                 direction_by_player_name: Dict[str, int]):
        """first player - horizontal moving, second player - vertical moving"""
        if len(players) != 2:
            raise ValueError(
                "players list must have 2 Player objects")

        if players[0].name == players[1].name:
            raise ValueError("players must have different names, "
                             f"but their names are {players[0].name}")

        self._game_id = game_id
        self._field = field
        self._players = list(players)
        self._direction_by_player_name = dict(direction_by_player_name)
        self._current_player_index = 0
        self._on_switch_move_owner_funcs = []
        self._on_win_funcs = []
        self._is_over = False
        self._winner_path = []

    @property
    def field(self):
        return self._field

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

    def get_player(self, move_order_index: int):
        return self._players[move_order_index]

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

    def is_over(self):
        return self._is_over

    def switch_move_owner(self):
        prev_index = self._current_player_index
        self._current_player_index = \
            (self._current_player_index + 1) % len(self._players)

        utilities.execute_all_funcs(self._on_switch_move_owner_funcs,
                                    self._players[prev_index],
                                    self._players[
                                        self._current_player_index])

    def make_move(self, cell_index) -> bool:
        if self._is_over or self._field.is_occupied(cell_index):
            return False

        current_player = self._players[self._current_player_index]

        self._field.set_owner(cell_index, current_player)

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

        if current_direction == Directions.VERTICAL:
            start_cells = self._field.get_all_cells_in_row(0)
            stop_cells = self._field.get_all_cells_in_row(
                self._field.height - 1)
        else:
            start_cells = self._field.get_all_cells_in_column(0)
            stop_cells = self._field.get_all_cells_in_column(
                self._field.width - 1)

        for start_cell in start_cells:
            path_for_owner = self._field.get_path_for_owner(
                self.get_move_owner(),
                start_cell,
                set(stop_cells))

            if len(path_for_owner) != 0:
                return path_for_owner

        return []

    def register_win(self, winner: PlayerProfile, winner_path: list):
        self._is_over = True
        self._winner_path = winner_path
        utilities.execute_all_funcs(self._on_win_funcs,
                                    winner,
                                    winner_path)

    def get_move_owner(self) -> PlayerProfile:
        return self._players[self._current_player_index]

    # def save(self):
    #     with open("hex_field_state.json", "w") as file:
    #         file.write(self.serialize())
    #
    # def serialize(self):
    #     data = {
    #         "field": self._field.serialize(),
    #         "is_over": self._is_over,
    #         "winner_path": self._winner_path,
    #     }
    #
    #     return json.dumps(data)
