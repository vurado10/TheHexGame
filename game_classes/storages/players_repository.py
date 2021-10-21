from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.storages.repository import Repository
from gui_lib.rgb_color import RgbColor


class PlayersRepository(Repository):
    def __init__(self, directory_path: str):
        super().__init__(directory_path)

    def get_all(self) -> list[PlayerProfile]:
        return [
            PlayerProfile("player1", RgbColor(0, 0, 0), 0),
            PlayerProfile("player2", RgbColor(0, 0, 0), 0),
            PlayerProfile("player3", RgbColor(0, 0, 0), 0),
            PlayerProfile("player4", RgbColor(0, 0, 0), 0),
            PlayerProfile("player5", RgbColor(0, 0, 0), 0),
            PlayerProfile("player6", RgbColor(0, 0, 0), 0),
            PlayerProfile("player20", RgbColor(0, 0, 0), 1988),
            PlayerProfile("player21", RgbColor(0, 0, 0), 9660),
            PlayerProfile("player22", RgbColor(0, 0, 0), 8521),
            PlayerProfile("player23", RgbColor(0, 0, 0), 6513),
            PlayerProfile("player24", RgbColor(0, 0, 0), 4664),
            PlayerProfile("player25", RgbColor(0, 0, 0), 5222),
            PlayerProfile("player26", RgbColor(0, 0, 0), 9078),
            PlayerProfile("player27", RgbColor(0, 0, 0), 1296),
            PlayerProfile("player28", RgbColor(0, 0, 0), 474),
            PlayerProfile("player29", RgbColor(0, 0, 0), 394),
            PlayerProfile("player30", RgbColor(0, 0, 0), 2661),
            PlayerProfile("player31", RgbColor(0, 0, 0), 4137),
            PlayerProfile("player32", RgbColor(0, 0, 0), 7750),
            PlayerProfile("player33", RgbColor(0, 0, 0), 3911),
            PlayerProfile("player34", RgbColor(0, 0, 0), 9759),
        ]

    def get_all_ids(self) -> list[str]:
        pass

    def generate_id(self) -> str:
        raise NotImplemented

    def get_by_id(self, name: str) -> PlayerProfile:
        return PlayerProfile(name, RgbColor(0, 0, 0), 0)

    def save(self, player: PlayerProfile):
        print(f"{player}: {player.score}")
