from typing import Dict, List
from gui_lib.scene_elements.event_system.event_listener import EventListener


class EventManager:
    def __init__(self):
        self._listeners_by_event_type: Dict[int, List[EventListener]]

        self._listeners_by_event_type = dict()

    def add_listener(self, event_listener: EventListener):
        for event_type in event_listener.get_handling_events_types():
            if event_type not in self._listeners_by_event_type:
                self._listeners_by_event_type[event_type] = []

            self._listeners_by_event_type[event_type].append(
                event_listener)

    def get_listeners_by_event_type(self, event_type: int):
        if event_type not in self._listeners_by_event_type:
            self._listeners_by_event_type[event_type] = []

        for listener in self._listeners_by_event_type[event_type]:
            yield listener

    def handle_events_queue(self, events):
        for event in events:
            listeners = self.get_listeners_by_event_type(
                event.type)

            for listener in listeners:
                if listener.is_working():
                    listener.notify(event)
