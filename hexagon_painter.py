from painter import Painter

class HexagonPainter(Painter):
    def __init__(self, center: Vector2, radius: int):
        self.center = center
        self.radius = radius

    def draw(self):
        pass