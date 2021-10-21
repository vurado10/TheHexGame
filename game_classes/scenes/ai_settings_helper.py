import threading

from game_classes import environment
from game_classes.ai.bot import Bot
from game_classes.ai.random_bot import RandomBot


class AiSettingsHelper:
    def __init__(self, ai_types: list[str]):
        self.__ai_types = list(ai_types)

    def create_bots(self, match,
                    type1: str, type2: str) -> tuple[list[str], list[Bot]]:
        ai_names = []
        bots = []

        bot1 = self.create_bot(type1, match, 0)
        if bot1:
            bot1.send_calc_request()  # TODO: to match scene
            ai_names.append(match.get_player(0).name)
            bots.append(bot1)

        bot2 = self.create_bot(type2, match, 1)
        if bot2:
            ai_names.append(match.get_player(1).name)
            bots.append(bot2)

        return ai_names, bots

    def create_bot(self, ai_type, match, move_order: int) -> [None, Bot]:
        player_name = match.get_player(move_order).name

        if ai_type == self.__ai_types[1]:
            bot = RandomBot(match, player_name)
        elif ai_type == self.__ai_types[2]:
            bot = RandomBot(match, player_name)
        else:
            return None

        def ai_move(current_player, next_player):
            if next_player.name == player_name:
                bot.send_calc_request()

        match.add_on_switch_move_owner(ai_move)
        t = threading.Thread(target=bot.start)
        if environment.LOG:
            print(f"create bot generated {t.name}")
        t.start()

        return bot
