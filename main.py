from game_classes.scenes.main_menu_scene import MainMenuScene
from gui_lib import app

if __name__ == "__main__":
    app.init_app((960, 540))

    app.create_and_set_scene("main menu", MainMenuScene)

    app.start_main_loop()
