import sys
import pygame
from gui_lib.scene import Scene


class EventManager:
    def __init__(self, scene: Scene = None):
        self.__scene = scene

    def set_scene(self, scene: Scene):
        self.__scene = scene

    def handle_events_queue(self, events):
        if self.__scene is None:
            return

        for event in events:
            handlers = self.__scene.get_event_handlers_by_event_type(
                event.type)

            for handler in handlers:
                handler.handle(event)
