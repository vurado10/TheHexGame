import time
import random

from game_classes.ai import ai_helper
from game_classes.ai.bot import Bot
from game_classes.game_domain.match import Match


class RandomBot(Bot):
    def __init__(self, match: Match, player_name, delay: float = 0.05):
        super().__init__(match, player_name)

        self.__delay = delay

    def make_move(self) -> int:
        cell_index = ai_helper.get_random_valid_cell_index(self._match,
                                                           self._player_name)

        time.sleep(self.__delay)

        return cell_index
