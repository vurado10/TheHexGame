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

    def generate_id(self) -> str:
        return "Game1"

    def get_by_id(self, match_id: str) -> Match:
        if not match_id:
            raise ValueError(f"No game match with id: {match_id}")

        try:
            with open(self.get_saving_name_by_match_id(match_id), "r") as file:
                data = json.loads(file.read())
                player_by_name = {
                    data["players"][0]:
                        self.__players_rep.get_by_id(data["players"][0]),
                    data["players"][1]:
                        self.__players_rep.get_by_id(data["players"][1])
                }
                # TODO: why match id calls game id?
                game_id = data["game id"]
                players = list(player_by_name.values())
                field = MatchesRepository.create_hex_field(data["field"],
                                                           player_by_name)
                match = Match(game_id,
                              field,
                              players,
                              data["direction by player name"],
                              data["remaining game sec"],
                              data["remaining move sec"])

                match._current_player_index = data["current player index"]
                match._is_over = data["is over"]
                if data["is starting"] and not match.is_over():
                    match.start_game()
                    match.pause_game()
                    # TODO: is_pause is always true. Is it correct?
                    # TODO: it works,
                    #  because saving from pause menu
                match._winner_path = data["winner path"]

                return match
        except FileNotFoundError:
            raise ValueError(f"No match with id: {match_id}")

    def save_with_id(self, match: Match, match_id: str):
        if "\\" in match_id or "/" in match_id:
            raise ValueError(f"It's impossible to "
                             f"use '\\' or '/' in name of saving")

        data = MatchesRepository.__convert_match_to_serializable_dict(match)
        json.dump(data, open(self.get_saving_name_by_match_id(match_id), "w"))

    def save(self, match: Match):
        raise NotImplemented

    @staticmethod
    def create_hex_field(data, owner_by_name: dict[str, PlayerProfile]):
        field = HexField(data["width"], data["height"])

        field.set_cell_states(data["cells states"])

        cell_owners_names = data["cells owners names"]
        cell_owners = {}
        for cell_index, owner_name in cell_owners_names:
            cell_owners[cell_index] = owner_by_name[owner_name]
        field.set_cells_owners(cell_owners)

        return field


    def get_saving_name_by_match_id(self, match_id: str):
        return os.path.join(self._directory_path, match_id + ".json")

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
