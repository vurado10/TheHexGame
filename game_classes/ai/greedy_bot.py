from game_classes.ai.bot import Bot
from game_classes.game_domain.match import Match


class GreedyBot(Bot):
    def __init__(self, match: Match, player_name):
        super().__init__(match, player_name)

    def make_move(self) -> int:
        pass
