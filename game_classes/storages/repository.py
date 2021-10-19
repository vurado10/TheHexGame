from abc import ABC, abstractmethod


class Repository(ABC):
    def __init__(self, file_path: str):
        self._file_path = file_path

    @abstractmethod
    def get_id(self, obj) -> str:
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def save(self, obj):
        pass
