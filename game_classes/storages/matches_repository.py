from game_classes.game_domain.directions import Directions
from game_classes.game_domain.hex_field import HexField
from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.storages.players_repository import PlayersRepository
from game_classes.storages.repository import Repository
from gui_lib.rgb_colors import RgbColors


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
        player1 = PlayerProfile("player_from_repo1", RgbColors.WHITE, 0)
        player2 = PlayerProfile("player_from_repo2", RgbColors.BLACK, 0)

        return Match(match_id, HexField(25, 25), [player1, player2],
                     {player1.name: Directions.HORIZONTAL,
                      player2.name: Directions.VERTICAL},
                     time_for_game=180,
                     time_for_move=10)

    def save_with_id(self, match: Match, match_id: str):
        # TODO: ValueError if match_id isn't correct
        raise ValueError

    def save(self, match: Match):
        print(match)
