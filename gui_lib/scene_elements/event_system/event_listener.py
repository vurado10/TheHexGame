from abc import ABC, abstractmethod
from typing import List

from pygame.event import Event


class EventListener(ABC):
    def __init__(self):
        self.__handling_event_types = []
        self._handlers_functions = []

    def notify(self, event: Event):
        if not self.is_valid_event(event):
            return

        for func in self._handlers_functions:
            func(self, event)

    def get_handling_events_types(self):
        for event_type in self.__handling_event_types:
            yield event_type

    def add_handler(self, handler_func):
        self._handlers_functions.append(handler_func)

    def remove_handler(self, handler_func):
        self._handlers_functions.remove(handler_func)

    def add_listening_type(self, event_type: int):
        self.__handling_event_types.append(event_type)

    @abstractmethod
    def is_valid_event(self, event: Event) -> bool:
        """Проверяет, произошло ли событие с данным объектом"""
        pass
