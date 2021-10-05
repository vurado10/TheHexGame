from typing import List
from game_classes import utilities
from game_classes.match.hex_field import HexField
from game_classes.match.player import Player


class Judge:
    """Checks for compliance with the rules of the game"""

    def __init__(self, field: HexField, players: List[Player]):
        if len(players) > 2:
            raise ValueError(
                "players list must have at least 2 Player objects")

        self.__field = field
        self.__players = list(players)
        self.__current_player_index = len(self.__players) - 1
        self.__on_switch_turn_owner_funcs = []

    def add_on_switch_turn_owner(self, func):
        """func(Player current_player, Player next_player)"""
        self.__on_switch_turn_owner_funcs.append(func)

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

        self.__field.set_owner(cell_index,
                               self.__players[self.__current_player_index])

        self.switch_turn_owner()
