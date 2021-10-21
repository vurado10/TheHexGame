import time
import random
from game_classes.ai.bot import Bot
from game_classes.game_domain.match import Match


class RandomBot(Bot):
    def __init__(self, match: Match, player_name, delay: float = 0.1):
        super().__init__(match, player_name)

        self.__delay = delay

    def make_move(self) -> int:
        cell_index = self.get_random_cell_index()
        while not self._match.is_valid_move(cell_index, self._player_name) \
                and not self._match.is_over():
            cell_index = self.get_random_cell_index()

        time.sleep(self.__delay)

        return cell_index

    def get_random_cell_index(self):
        return random.randint(0, self._field.width * self._field.height - 1)
