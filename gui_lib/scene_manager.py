class SceneManager:
    def __init__(self, next_scene):
        self._current_scene = None
        self._next_scene = next_scene
        self._on_scene_changing = None

    def start(self):
        self._current_scene.hide()
        self._current_scene = self._next_scene
        self._next_scene = None
        self._current_scene.show()

    def set_next_scene(self, next_scene):
        self._next_scene = next_scene

    def set_handler_on_scene_changing(self, func):
        self._on_scene_changing = func
