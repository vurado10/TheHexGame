from game_classes import utilities
from game_classes.match.cell_states import CellStates
from game_classes.match.player import Player


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
        return self.__cells_states[cell_index] == CellStates.OCCUPIED

    def get_owner(self, cell_index: int) -> Player:
        try:
            return self.__cells_owners[cell_index]
        except KeyError:
            raise KeyError(f"No owner on index: {cell_index}")

    def set_owner(self, cell_index: int, owner: Player):
        current_owner = (self.get_owner(cell_index)
                         if self.is_occupied(cell_index)
                         else None)

        utilities.execute_all_funcs(self.__on_cell_state_changing_funcs,
                                    cell_index,
                                    current_owner,
                                    owner)

        self.__cells_owners[cell_index] = owner
        self.__cells_states[cell_index] = CellStates.OCCUPIED
