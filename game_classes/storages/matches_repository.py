from game_classes.game_domain.match import Match
from game_classes.storages.players_repository import PlayersRepository
from game_classes.storages.repository import Repository


class MatchesRepository(Repository):
    def __init__(self, files_path: str, players_repository: PlayersRepository):
        super().__init__(files_path)

        self.__players_repository = players_repository

    def generate_id(self) -> str:
        return "Game"

    def get_by_id(self, match_id: str) -> Match:
        pass

    def save_with_id(self, match: Match, match_id: str):
        # TODO: ValueError if match_id isn't correct
        pass

    def save(self, match: Match):
        print(match)
