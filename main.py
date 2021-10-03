from game_scenes.sample_scene import SampleScene
from gui_lib import app

if __name__ == "__main__":
    app.init_app((960, 540))

    # hex_field = HexField(game_scene, 11, 11, RgbColors.WHITE,
    #                      RgbColors.BLACK, RgbColors.WHITE, RgbColors.BLACK)
    # hex_field.show()

    app.add_scene("main", SampleScene(app.screen))
    app.set_current_scene("main")
    app.show_scene()

    app.start_main_loop()

