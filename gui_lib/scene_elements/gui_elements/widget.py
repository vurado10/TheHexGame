from abc import abstractmethod, ABC
from typing import List
from gui_lib.scene_elements.event_system.event_listener import EventListener
from gui_lib.scene_elements.gui_elements.gui_element import GuiElement
from pygame.event import Event
from pygame.math import Vector2
from pygame.surface import Surface


class Widget(GuiElement, EventListener, ABC):
    def __init__(self,
                 position: Vector2,
                 listening_events_types: List[int] = None):
        GuiElement.__init__(self)
        EventListener.__init__(self)

        if listening_events_types is not None:
            for event_type in listening_events_types:
                self.add_handler(event_type, lambda *args, **kwargs: None)

        self._children = []
        self._position = Vector2(position)

    # TODO: get/set methods instead properties
    @property
    def position(self):
        return Vector2(self._position)

    @position.setter
    def position(self, value: Vector2):
        self.set_position(value)

    def set_position(self, value):
        prev_position = self._position
        self._position = Vector2(value)

        for child in self._children:
            child.position += self._position - prev_position

    @property
    def children(self):
        return list(self._children)

    def add_child(self, widget):
        widget.position += self._position
        self._children.append(widget)

    def add_children(self, widgets: list):
        for widget in widgets:
            self.add_child(widget)

    def update_on(self, surface: Surface):
        if self.is_hide():
            return

        self.update_self_on(surface)

        for child in self._children:
            child.update_on(surface)

    def notify(self, event: Event):
        if not self.is_working():
            return

        if not self.is_valid_event(event):
            return

        EventListener.notify(self, event)

        for child in self._children:
            child.notify(event)

    def hide(self):
        self._is_hide = True
        self._is_working = False

    def show(self):
        self._is_hide = False
        self._is_working = True

    def is_valid_event(self, event: Event) -> bool:
        return False

    def update_self_on(self, surface: Surface):
        pass
