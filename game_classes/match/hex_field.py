import collections
from typing import List, Tuple, Set
from game_classes import utilities
from game_classes.match.cell_states import CellStates
from game_classes.settings.player_profile import PlayerProfile


class HexField:
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.__cells_states = [CellStates.NEUTRAL] * (self.width * self.height)
        self.__cells_owners = {}
        self.__on_cell_state_changing_funcs = []

    def add_on_cell_owner_changing(self, func):
        """func(int cell_index, Player current_owner, Player next_owner)
        current_owner is None if cell doesn't have any owners"""

        self.__on_cell_state_changing_funcs.append(func)

    def is_occupied(self, cell_index: int):
        try:
            return self.__cells_states[cell_index] == CellStates.OCCUPIED
        except IndexError:
            raise IndexError(f'on {cell_index}')

    def get_owner(self, cell_index: int) -> PlayerProfile:
        try:
            return self.__cells_owners[cell_index]
        except KeyError:
            raise KeyError(f"No owner on index: {cell_index}")

    def set_owner(self, cell_index: int, owner: PlayerProfile):
        current_owner = (self.get_owner(cell_index)
                         if self.is_occupied(cell_index)
                         else None)

        utilities.execute_all_funcs(self.__on_cell_state_changing_funcs,
                                    cell_index,
                                    current_owner,
                                    owner)

        self.__cells_owners[cell_index] = owner
        self.__cells_states[cell_index] = CellStates.OCCUPIED

    def get_vertical_opposite_cells(self) -> List[Tuple[int, int]]:
        result = []
        for i in range(self.width):
            result.append((i, i + self.width * (self.height - 1)))

        return result

    def get_horizontal_opposite_cells(self) -> List[Tuple[int, int]]:
        result = []
        for j in range(self.height):
            result.append((self.width * j, self.width * (j + 1) - 1))

        return result

    def get_adjacent_cells(self, cell_index) -> List[int]:
        candidates = [
                cell_index - self.width,
                cell_index - self.width + 1,
                cell_index - 1,
                cell_index + 1,
                cell_index + self.width - 1,
                cell_index + self.width
        ]

        row_correct_cells = []

        row_offset = -1
        for i in range(len(candidates)):
            if (self.get_row(candidates[i])
                    == self.get_row(cell_index) + row_offset):
                row_correct_cells.append(candidates[i])

            if i % 2 != 0:
                row_offset += 1

        return list(filter(
            lambda index: 0 <= index < self.width * self.height,
            row_correct_cells))

    def get_row(self, cell_index):
        return cell_index // self.width

    def get_all_cells_in_row(self, row_index) -> List[int]:
        return list(
            range(self.width * row_index, self.width * (row_index + 1)))

    def get_all_cells_in_column(self, column_index) -> List[int]:
        return list(
            range(column_index, self.width * self.height, self.width))

    def check_path_existing_for_owner(self,
                                      owner: PlayerProfile,
                                      start: int,
                                      stop_cells: Set[int]) -> bool:
        deque = collections.deque()
        if self.is_occupied(start) and self.get_owner(start) is owner:
            if start in stop_cells:
                return True
            deque.append(start)
        used = set()

        while len(deque) != 0:
            current_cell = deque.popleft()
            used.add(current_cell)
            for adjacent_cell in self.get_adjacent_cells(current_cell):
                if (self.is_occupied(adjacent_cell)
                        and self.get_owner(adjacent_cell) is owner):
                    if adjacent_cell in stop_cells:
                        return True

                    if adjacent_cell not in used:
                        deque.append(adjacent_cell)

        return False
