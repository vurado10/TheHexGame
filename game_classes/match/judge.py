from typing import List
from game_classes import utilities
from game_classes.match.hex_field import HexField
from game_classes.match.player import Player


class Judge:
    """Checks for compliance with the rules of the game"""

    def __init__(self, field: HexField, players: List[Player]):
        """first player - horizontal moving, second player - vertical moving"""
        if len(players) > 2:
            raise ValueError(
                "players list must have at least 2 Player objects")

        self.__field = field
        self.__players = list(players)
        self.__current_player_index = 0
        self.__on_switch_turn_owner_funcs = []
        self.__on_win_funcs = []

    def add_on_switch_turn_owner(self, func):
        """func(Player current_player, Player next_player)"""
        self.__on_switch_turn_owner_funcs.append(func)

    def add_on_win(self, func):
        """func(Player winner)"""
        self.__on_win_funcs.append(func)

    def switch_turn_owner(self):
        next_index = (self.__current_player_index + 1) % len(self.__players)

        utilities.execute_all_funcs(self.__on_switch_turn_owner_funcs,
                                    self.__players[
                                        self.__current_player_index],
                                    self.__players[next_index])

        self.__current_player_index = next_index

    def make_turn(self, cell_index):
        if self.__field.is_occupied(cell_index):
            return

        current_player = self.__players[self.__current_player_index]

        self.__field.set_owner(cell_index,
                               current_player)

        if self.is_win():
            self.register_win(current_player)
            return

        self.switch_turn_owner()

    def is_win(self) -> [None, Player]:
        if self.__current_player_index == 1:
            start_cells = self.__field.get_all_cells_in_row(0)
            stop_cells = self.__field.get_all_cells_in_row(
                self.__field.height - 1)
        else:
            start_cells = self.__field.get_all_cells_in_column(0)
            stop_cells = self.__field.get_all_cells_in_column(
                self.__field.width - 1)

        for start_cell in start_cells:
            if self.__field.check_path_existing_for_owner(
                    self.__players[self.__current_player_index],
                    start_cell,
                    set(stop_cells)):
                return True

        return False

    def register_win(self, winner: Player):
        utilities.execute_all_funcs(self.__on_win_funcs,
                                    winner)
