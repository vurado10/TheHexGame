from game_classes.storages.repository import Repository


class PlayersRepository(Repository):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def get_id(self, obj) -> str:
        pass

    def get_by_id(self, obj_id):
        pass

    def save(self, obj):
        pass
