import math
import unittest
from gui_lib.figures import hexagon_figure
from pygame.math import Vector2


class HexagonFigureTests(unittest.TestCase):
    def test_vertexes_calculation_without_rotation(self):
        figure = hexagon_figure.Hexagon(Vector2(), 1, 0.0)
        vertexes = figure.vertexes
        self.assertSequenceEqual(vertexes, [Vector2(0.5, -0.866025),
                                            Vector2(-0.5, -0.866025),
                                            Vector2(-1, 0),
                                            Vector2(-0.5, 0.866025),
                                            Vector2(0.5, 0.866025),
                                            Vector2(1, 0)])

    def test_vertexes_calculation_rotation_30(self):
        figure = hexagon_figure.Hexagon(Vector2(),
                                        1,
                                        math.pi / 6)
        vertexes = figure.vertexes
        self.assertSequenceEqual(vertexes, [Vector2(6.12323e-17, -1),
                                            Vector2(-0.866025, -0.5),
                                            Vector2(-0.866025, 0.5),
                                            Vector2(-1.83697e-16, 1),
                                            Vector2(0.866025, 0.5),
                                            Vector2(0.866025, -0.5)])


if __name__ == "__main__":
    unittest.main()
