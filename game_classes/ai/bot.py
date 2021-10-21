import pygame
import threading
from abc import ABC, abstractmethod
from game_classes.ai.bot_events_types import BotEventsTypes
from game_classes.game_domain.match import Match


class Bot(ABC):
    def __init__(self, match: Match, player_name):
        self._match = match
        self._field = self._match.field
        self._player_name = player_name
        self._make_move_request_event = threading.Event()

    @abstractmethod
    def make_move(self) -> int:
        pass

    def send_calc_request(self):
        self._make_move_request_event.set()

    def start(self):
        while True:
            self._make_move_request_event.wait()

            # TODO: make "bot stop" event

            # TODO: add exception handling (if event queue is full,
            #  pygame.event.post will throw an exception)

            pygame.event.post(pygame.event.Event(BotEventsTypes.CALC_FINISH,
                                                 cell_index=self.make_move(),
                                                 player_name=
                                                 self._player_name))

            self._make_move_request_event.clear()
