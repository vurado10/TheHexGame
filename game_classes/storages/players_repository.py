from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.storages.repository import Repository
from gui_lib.rgb_color import RgbColor


class PlayersRepository(Repository):
    def __init__(self, files_path: str):
        super().__init__(files_path)

    def get_all(self) -> list[PlayerProfile]:
        pass

    def generate_id(self) -> str:
        pass

    def get_by_id(self, name: str) -> PlayerProfile:
        return PlayerProfile(name, RgbColor(0, 0, 0), 0)

    def save(self, player: PlayerProfile):
        print(f"{player}: {player.score}")
