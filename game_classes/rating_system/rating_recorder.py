from game_classes.storages.players_repository import PlayersRepository


class RatingRecorder:
    def __init__(self, players_repository: PlayersRepository):
        self.__players_rep = players_repository

    def save_ratings_for_players(self, match):
        player1 = self.__players_rep.get_by_id(match.get_player(0).name)
        player2 = self.__players_rep.get_by_id(match.get_player(1).name)

        player1.score += \
            RatingRecorder.__calculate_rating_for_player(match, player1)

        player2.score += \
            RatingRecorder.__calculate_rating_for_player(match, player2)

        self.__players_rep.save(player1)
        self.__players_rep.save(player2)

    @staticmethod
    def __calculate_rating_for_player(match, player) -> int:
        if match.is_over() and match.get_move_owner().name == player.name:
            winner_path_len = len(match.winner_path)

            return round(match.field.size * 7 / winner_path_len) \
                if winner_path_len != 0 else 0

        return 0

