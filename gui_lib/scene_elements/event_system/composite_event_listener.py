from typing import List

from gui_lib.scene_elements.event_system.event_listener import EventListener
from pygame.event import Event


class CompositeEventListener(EventListener):
    def __init__(self, listening_events_types: List[int] = None):
        super().__init__()
        if listening_events_types is not None:
            for event_type in listening_events_types:
                self.add_handler(event_type, lambda *args, **kwargs: None)

        self._children_listeners = []

    def add_child_listener(self, listener: EventListener):
        self._children_listeners.append(listener)

    def add_children_listeners(self, listeners: List[EventListener]):
        for listener in listeners:
            self._children_listeners.append(listener)

    def notify(self, event: Event):
        for child in self._children_listeners:
            child.notify(event)

    def is_valid_event(self, event: Event) -> bool:
        return True
