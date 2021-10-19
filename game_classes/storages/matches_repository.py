from game_classes.game_domain.match import Match
from game_classes.storages.players_repository import PlayersRepository
from game_classes.storages.repository import Repository


class MatchesRepository(Repository):
    def __init__(self, file_path: str, players_repository: PlayersRepository):
        super().__init__(file_path)

        self.__players_repository = players_repository

    def get_id(self, obj) -> str:
        pass

    def get_by_id(self, match_id: int) -> Match:
        pass

    def save(self, match: Match):
        pass
