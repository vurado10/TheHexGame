from game_classes.loading.savings_list_scene import SavingsListScene
from game_classes.main_menu.main_menu_scene import MainMenuScene
from game_classes.match.game_over_scene import GameOverScene
from game_classes.match.match_scene import MatchScene
from game_classes.pause.pause_scene import PauseScene
from game_classes.rating.RatingScene import RatingScene
from game_classes.settings.settings_scene import SettingsScene
from gui_lib import app

if __name__ == "__main__":
    app.init_app((960, 540))

    app.add_scene("game", MatchScene(app.screen))
    app.add_scene("game over", GameOverScene(app.screen))
    app.add_scene("main menu", MainMenuScene(app.screen))
    app.add_scene("settings", SettingsScene(app.screen))
    app.add_scene("rating", RatingScene(app.screen))
    app.add_scene("savings list", SavingsListScene(app.screen))
    app.add_scene("pause", PauseScene(app.screen))
    app.set_current_scene("main menu")
    # app.add_scene("sample", SampleScene(app.screen))
    # app.set_current_scene("sample")

    app.start_main_loop()
