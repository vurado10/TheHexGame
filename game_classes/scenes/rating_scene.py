from game_classes import environment
from game_classes.game_domain.player_profile import PlayerProfile
from game_classes.scenes.scene_with_list import SceneWithList
from game_classes.storages.players_repository import PlayersRepository
from pygame.surface import Surface


class RatingScene(SceneWithList):
    def __init__(self, screen: Surface):
        from game_classes.scenes.main_menu_scene import MainMenuScene

        players = PlayersRepository(environment.PLAYERS_REP_PATH).get_all()

        super().__init__(screen,
                         "main menu",
                         MainMenuScene,
                         RatingScene.__get_list_view_values(players))

    @staticmethod
    def __get_list_view_values(players: list[PlayerProfile]):
        sorted_players = sorted(players, key=lambda p: p.score, reverse=True)

        return list(map(lambda p: f"{p.name}: {p.score}", sorted_players))
