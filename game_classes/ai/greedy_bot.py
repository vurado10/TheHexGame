import random
import time

from game_classes.ai import ai_helper
from game_classes.ai.bot import Bot
from game_classes.game_domain.match import Match


class GreedyBot(Bot):
    def __init__(self, match: Match, player_name):
        super().__init__(match, player_name)

        self.__field = match.field
        self.__last_cell_index = -1
        self.__direction = \
            self._match.get_direction_by_player_name_dict()[player_name]
        self.__player_profile = match.get_player_by_name(player_name)
        self.__stop_cells = self._match.get_stop_cells_by_direction(
            self.__direction)

    def make_move(self) -> int:
        if self.__last_cell_index == -1:
            start_cells = \
                self._match.get_start_cells_by_direction(self.__direction)

            self.__last_cell_index = start_cells[
                random.randint(0, len(start_cells))]

            return self.__last_cell_index

        adjacent_cells = self.__field.get_adjacent_cells(
            self.__last_cell_index)

        paths = []

        def check_for_free(cell):
            return not self.__field.is_occupied(cell)

        for adjacent_cell in adjacent_cells:
            tmp_path = self.__field.get_path(adjacent_cell,
                                             self.__stop_cells,
                                             check_for_free)
            if tmp_path:
                paths.append(tmp_path)

        min_length = len(min(paths, key=lambda path: len(path)))
        paths = list(filter(lambda path: len(path) == min_length, paths))

        if paths:
            path_index = random.randint(0, len(paths) - 1)
            self.__last_cell_index = paths[path_index][0]
        else:
            self.__last_cell_index = \
                ai_helper.get_random_valid_cell_index(self._match,
                                                      self._player_name)

        time.sleep(0.1)

        return self.__last_cell_index
