from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, directory_path: str):
        self._directory_path = directory_path

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_all_ids(self) -> list[str]:
        pass

    @abstractmethod
    def generate_id(self) -> str:
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def save(self, obj):
        pass
