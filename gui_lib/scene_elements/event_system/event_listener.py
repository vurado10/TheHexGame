from abc import ABC, abstractmethod
from pygame.event import Event


class EventListener(ABC):
    def __init__(self):
        self.__handling_event_types = set()
        self._handlers_functions_by_event_type = {}

    def notify(self, event: Event):
        if not self.is_valid_event(event):
            return

        try:
            for func in self._handlers_functions_by_event_type[event.type]:
                func(self, event)
        except KeyError:
            return

    def get_handling_events_types(self):
        for event_type in self.__handling_event_types:
            yield event_type

    def add_handler(self, event_type, handler_func):
        if event_type not in self._handlers_functions_by_event_type:
            self._handlers_functions_by_event_type[event_type] = []

        self._handlers_functions_by_event_type[event_type].append(handler_func)
        self.__handling_event_types.add(event_type)

    def remove_handler(self, event_type, handler_func):
        if event_type not in self._handlers_functions_by_event_type:
            self._handlers_functions_by_event_type[event_type] = []

        self._handlers_functions_by_event_type[event_type].remove(handler_func)

        if len(self._handlers_functions_by_event_type[event_type]) == 0:
            self.__handling_event_types.remove(event_type)

    @abstractmethod
    def is_valid_event(self, event: Event) -> bool:
        """Проверяет, произошло ли событие с данным объектом"""
        pass
