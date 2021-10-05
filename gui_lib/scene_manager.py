from gui_lib.scene import Scene


class SceneManager:
    def __init__(self, next_scene=None):
        self.current_scene = None
        self.next_scene = next_scene
        self._on_scene_changing = None

    def switch_scenes(self):
        if self._on_scene_changing is not None:
            self._on_scene_changing(self.current_scene, self.next_scene)

        if self.next_scene is None:
            raise Exception("It can't switch scenes. Next scene is None")

        self.current_scene = self.next_scene
        self.next_scene = None

    def set_next_scene(self, next_scene):
        self.next_scene = next_scene

    def set_handler_on_scene_changing(self, func):
        self._on_scene_changing = func
