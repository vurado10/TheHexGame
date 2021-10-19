from typing import List, Dict

from game_classes.game_domain.player_profile import PlayerProfile
from gui_lib.painters.hexagon_painter import HexagonPainter
from gui_lib.rgb_color import RgbColor


class HexFieldProfile:
    def __init__(self,
                 player1: PlayerProfile,
                 player2: PlayerProfile,
                 direction1: int,
                 direction2: int,
                 bg_color: RgbColor,
                 bg_color_cell: RgbColor,
                 border_color_cell: RgbColor,
                 cell_padding_factor: float):
        if direction1 == direction2:
            raise ValueError("Your can't play in one direction")

        self.bg_color = bg_color
        self.bg_color_cell = bg_color_cell
        self.border_color_cell = border_color_cell
        self.cell_padding_factor = cell_padding_factor

        self.__players = [
            player1,
            player2
        ]

        self.__index_by_player = {
            player1: 0,
            player2: 1
        }

        self.__direction_by_player = {
            player1: direction1,
            player2: direction2
        }

    def get_player(self, index):
        return self.__players[index]

    def get_index_by_player(self, player: PlayerProfile):
        return self.__index_by_player[player]

    def get_player_by_direction(self, key_direction: int):
        for player, direction in self.__direction_by_player.items():
            if direction == key_direction:
                return player

        raise IndexError("No player with such direction")

    def get_direction_by_player(self, player: PlayerProfile):
        return self.__direction_by_player[player]

    def get_direction_by_player_dict(self) -> Dict[PlayerProfile, int]:
        return dict(self.__direction_by_player)

    def get_players_in_turn_order(self) -> List[PlayerProfile]:
        return list(self.__players)

    def get_painter_for_player(self, player: PlayerProfile):
        return HexagonPainter(
                self.bg_color_cell,
                self.border_color_cell,
                player.color,
                self.cell_padding_factor)

