import json
import os.path

from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.storages.repository import Repository


class PlayersRepository(Repository):
    def __init__(self, directory_path: str):
        super().__init__(directory_path)

    def get_all(self) -> list[PlayerProfile]:
        result = []
        for name in self.get_all_ids():
            result.append(self.get_by_id(name))

        return result

    def get_all_ids(self) -> list[str]:
        return list(map(lambda n: n[:-5], os.listdir(self._directory_path)))

    def generate_id(self) -> str:
        raise NotImplemented

    def get_by_id(self, name: str) -> PlayerProfile:
        try:
            with open(self.get_saving_name_by_player_name(name), "r") as file:
                data = json.loads(file.read())

                return PlayerProfile(data["name"], data["score"])
        except FileNotFoundError:
            raise ValueError(f"No player with name: {name}")

    def save(self, player: PlayerProfile):
        data = {
            "name": player.name,
            "score": player.score
        }

        json.dump(data, open(self.get_saving_name_by_player_name(player.name),
                             "w"))

    def get_saving_name_by_player_name(self, name: str):
        return os.path.join(self._directory_path,
                            name + ".json")
