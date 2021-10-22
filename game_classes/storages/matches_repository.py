import json
import os
from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.storages.players_repository import PlayersRepository
from game_classes.storages.repository import Repository


class MatchesRepository(Repository):
    def __init__(self, directory_path: str,
                 players_repository: PlayersRepository):
        super().__init__(directory_path)

        self.__players_rep = players_repository

    def get_all(self):
        pass

    def get_all_ids(self) -> list[str]:
        return [
            "save 1908",
            "save 5672",
            "save 138",
            "save 7088",
            "save 7927",
            "save 2814",
            "save 854",
            "save 1330",
            "save 2328",
            "save 4397",
            "save 1639",
            "save 4933",
            "save 441",
            "save 1407",
            "save 6977",
        ]

    def generate_id(self) -> str:
        return "Game"

    def get_by_id(self, match_id: str) -> Match:
        print(match_id)
        player1 = PlayerProfile("player_from_repo1", 0)
        player2 = PlayerProfile("player_from_repo2", 0)

        return Match(match_id, HexField(25, 25), [player1, player2],
                     {player1.name: Directions.HORIZONTAL,
                      player2.name: Directions.VERTICAL},
                     time_for_game=180,
                     time_for_move=10)

    def save_with_id(self, match: Match, match_id: str):
        if "\\" in match_id or "/" in match_id:
            raise ValueError(f"It's impossible to "
                             f"use '\\' or '/' in name of saving")

        data = MatchesRepository.__convert_match_to_serializable_dict(match)
        json.dump(data, open(os.path.join(self._directory_path,
                                          match_id + ".json"),
                             "w"))

    def save(self, match: Match):
        raise NotImplemented

    @staticmethod
    def __convert_match_to_serializable_dict(match):
        return {
            "game id": match.game_id,
            "field":
                MatchesRepository.__convert_hex_field_to_serializable_dict(
                    match.field),
            "players": [match.get_player(0).name, match.get_player(1).name],
            "direction by player name":
                match.get_direction_by_player_name_dict(),
            "current player index": match._current_player_index,
            "is over": match.is_over(),
            "is pause": match.is_pause(),
            "is starting": match._is_starting,
            "winner path": match.winner_path,
            "remaining game sec": match.get_remaining_game_sec(),
            "remaining move sec": match.get_remaining_move_sec()
        }

    @staticmethod
    def __convert_hex_field_to_serializable_dict(field: HexField):
        cells_owners = field.get_cells_owners()
        cells_owners_names = list()
        for cell_index in cells_owners:
            cells_owners_names.append([cell_index,
                                       cells_owners[cell_index].name])

        return {
            "width": field.width,
            "height": field.height,
            "cells states": field.get_cell_states(),
            "cells owners names": cells_owners_names
        }
