from abc import ABC, abstractmethod


class EventHandler(ABC):
    def __init__(self):
        self._handlingEventTypes = []

    @abstractmethod
    def handle(self):
        pass
