from abc import ABC, abstractmethod
from pygame.event import Event


class EventHandler(ABC):
    def __init__(self):
        self._handlingEventTypes = []
        self._handlers_functions = []

    def handle(self, event: Event):
        for func in self._handlers_functions:
            func(self, event)
