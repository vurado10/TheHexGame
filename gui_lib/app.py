import pygame
import sys
from typing import Dict, Tuple
from gui_lib.scene import Scene
from gui_lib.scene_manager import SceneManager
from pygame.surface import Surface
from pygame.time import Clock

fps = 30
scene_manager: SceneManager
screen: Surface
__current_scene_name: str
__scenes: Dict[str, Scene]
__clock: Clock


def init_app(screen_size: Tuple[int, int]):
    global screen, __clock, scene_manager, __scenes

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    __clock = Clock()
    scene_manager = SceneManager()
    __scenes = dict()


def on_exit(): sys.exit(0)


def add_scene(name: str, scene: Scene):
    __scenes[name] = scene


def set_current_scene(name: str):
    global __current_scene_name

    __current_scene_name = name


def show_scene():
    scene_manager.set_next_scene(__scenes[__current_scene_name])
    scene_manager.switch_scenes()


def start_main_loop():
    while True:
        __clock.tick(fps)

        events = pygame.event.get()

        # TODO: quit_handler
        if pygame.QUIT in [e.type for e in events]:
            on_exit()

        # if pygame.MOUSEBUTTONDOWN in [e.type for e in events]:
        #     scene_manager.event_manager.handle_events_queue(events)
        scene_manager.event_manager.handle_events_queue(events)

        pygame.display.flip()
