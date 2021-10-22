import random


def get_random_cell_index(field):
    return random.randint(0, field.size - 1)


def get_random_valid_cell_index(match, player_name):
    """if there is no valid cell_index, it returns random cell index"""
    field = match.field

    cell_index = get_random_cell_index(field)
    while not match.is_valid_move(cell_index, player_name) \
            and not match.is_over():
        cell_index = get_random_cell_index(field)

    return cell_index
