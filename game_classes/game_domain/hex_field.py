import collections
from typing import List, Tuple, Set
from gui_lib import utilities
from game_classes.game_domain.cell_states import CellStates
from game_classes.game_domain.player_profile import PlayerProfile


class HexField:
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.__cells_states = [CellStates.NEUTRAL] * (self.width * self.height)
        self.__cells_owners = {}
        self.__on_cell_state_changing_funcs = []

    @property
    def size(self) -> int:
        return self.width * self.width

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
            raise ValueError(f"No owner on index: {cell_index}")

    def set_owner(self, cell_index: int, owner: PlayerProfile):
        current_owner = (self.get_owner(cell_index)
                         if self.is_occupied(cell_index)
                         else None)

        self.__cells_owners[cell_index] = owner
        self.__cells_states[cell_index] = CellStates.OCCUPIED

        utilities.execute_all_funcs(self.__on_cell_state_changing_funcs,
                                    cell_index,
                                    current_owner,
                                    owner)

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

    def get_path_for_owner(self,
                           owner: PlayerProfile,
                           start: int,
                           stop_cells: Set[int]):
        deque = collections.deque()
        if self.is_occupied(start) and self.get_owner(start) is owner:
            if start in stop_cells:
                return [start]
            deque.append(start)
        used = set()
        tracking_result = {start: None}

        while len(deque) != 0:
            current_cell = deque.popleft()
            used.add(current_cell)
            cells_for_check = ([current_cell]
                               + self.get_adjacent_cells(current_cell))
            for checking_cell in cells_for_check:
                if (self.is_occupied(checking_cell)
                        and self.get_owner(checking_cell) is owner):
                    if checking_cell not in used:
                        if checking_cell not in tracking_result:
                            tracking_result[checking_cell] = current_cell

                        if checking_cell in stop_cells:
                            return HexField._get_path_from_tracking(
                                tracking_result, checking_cell)

                        deque.append(checking_cell)

        return []

    # def save(self):
    #     with open("hex_field_state.json", "w") as file:
    #         file.write(self.serialize())
    #
    # def serialize(self):
    #     data = {
    #         "states": self.__cells_states,
    #         "owners": self.__cells_owners,
    #         "width": self.width,
    #         "height": self.height
    #     }
    #
    #     return json.dumps(data)
    #
    # def load(self):
    #     pass

    @staticmethod
    def _get_path_from_tracking(tracking_result, stop_cell):
        result = []
        current_cell = stop_cell
        while current_cell is not None:
            result.append(current_cell)
            current_cell = tracking_result[current_cell]

        return list(reversed(result))
