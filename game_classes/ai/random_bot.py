import random
import time

from game_classes.game_domain.match import Match


class RandomBot:
    # TODO: replace field with match
    def __init__(self, match: Match):
        self.__match = match
        self.__field = self.__match.field

    def make_move(self):
        # TODO: delete event recursion
        cell_index = self.get_random_cell_index()
        while not self.__match.make_move(cell_index) \
                and not self.__match.is_over():
            cell_index = self.get_random_cell_index()

    def get_random_cell_index(self):
        return random.randint(0, self.__field.width * self.__field.height - 1)
