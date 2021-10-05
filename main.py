from game_classes.match.game_over_scene import GameOverScene
from game_classes.match.match_scene import MatchScene
from game_classes.pause.pause_scene import PauseScene
from gui_lib import app

if __name__ == "__main__":
    app.init_app((960, 540))

    app.add_scene("main", MatchScene(app.screen))
    app.add_scene("game over", GameOverScene(app.screen))
    app.add_scene("pause", PauseScene(app.screen))
    app.set_current_scene("main")

    app.start_main_loop()
