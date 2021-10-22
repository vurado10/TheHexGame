from game_classes.game_domain.match import Match
from game_classes.game_domain.player_profile import PlayerProfile
from gui_lib.rgb_color import RgbColor
from gui_lib.rgb_colors import RgbColors

SCENE_BG_COLOR = RgbColors.DARK_BLUE
BUTTON_BG_COLOR = RgbColors.DARK_GREEN
BUTTON_TEXT_COLOR = RgbColors.DARK_BLUE
TEXT_INPUT_BG = RgbColors.DARK_GREEN
TEXT_INPUT_CONTENT = RgbColors.DARK_BLUE
TITLE_COLOR = RgbColors.DARK_GREEN
PLAYER1_COLOR = RgbColor.create_from_string("AFA825")
PLAYER2_COLOR = RgbColor.create_from_string("C25353")
WIN_LINE_COLOR = RgbColor.create_from_string("206676")
CELL_BG = RgbColors.BLACK
CELL_BORDER = RgbColors.WHITE


def get_player_color(move_order: int):
    if move_order == 0:
        return PLAYER1_COLOR
    elif move_order == 1:
        return PLAYER2_COLOR

    raise ValueError(f"No color for move order: {move_order}")


def get_color_by_player_profile(match: Match, player: PlayerProfile):
    return get_player_color(
        match.get_move_order_index_by_player_name(player.name))
