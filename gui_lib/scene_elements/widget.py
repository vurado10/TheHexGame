from typing import List
from gui_lib.scene_elements.event_system.composite_event_listener import \
    CompositeEventListener
from gui_lib.scene_elements.gui_elements.composite_gui_element import \
    CompositeGuiElement
from pygame.math import Vector2


class Widget(CompositeGuiElement, CompositeEventListener):
    def __init__(self,
                 position: Vector2,
                 width_px: int,
                 height_px: int,
                 listening_events_types: List[int] = None):
        CompositeGuiElement.__init__(self, position, width_px, height_px)
        CompositeEventListener.__init__(self, listening_events_types)

    def add_children_widgets(self, widgets: list):
        self.add_children_elements(widgets)
        self.add_children_listeners(widgets)

