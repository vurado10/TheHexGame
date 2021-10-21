from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, files_path: str):
        self._file_path = files_path

    @abstractmethod
    def generate_id(self) -> str:
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def save(self, obj):
        pass
