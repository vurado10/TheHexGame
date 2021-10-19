from game_classes.scenes.main_menu_scene import MainMenuScene
from game_classes.storages.matches_repository import MatchesRepository
from game_classes.storages.players_repository import PlayersRepository
from gui_lib import app

if __name__ == "__main__":
    app.init_app((960, 540))

    players_repository = PlayersRepository(".\\players")
    matches_repository = MatchesRepository(".\\matches", players_repository)

    app.create_and_set_scene("main menu", MainMenuScene)

    app.start_main_loop()
