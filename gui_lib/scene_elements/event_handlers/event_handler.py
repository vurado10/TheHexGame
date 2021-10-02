from abc import ABC, abstractmethod
from typing import List

from pygame.event import Event


class EventHandler(ABC):
    def __init__(self, event_types: List[int]):
        self._handling_event_types = list(event_types)
        self._handlers_functions = []

    def handle(self, event: Event):
        if not self.is_valid_event(event):
            return

        for func in self._handlers_functions:
            func(self, event)

    def get_handling_event_types(self):
        for event_type in self._handling_event_types:
            yield event_type

    @abstractmethod
    def is_valid_event(self, event: Event) -> bool:
        """Проверяет, произошло ли событие с данным объектом"""
        pass
