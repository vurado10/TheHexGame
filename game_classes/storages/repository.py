import os.path
from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, directory_path: str):
        if not os.path.isdir(directory_path):
            os.makedirs(directory_path)

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
