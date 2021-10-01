from figure_size import FigureSize


class RadiusSize(FigureSize):
    def __init__(self, radius: int, rotation_angle_radians: float):
        self.radius = radius
        self.rotation_angle_radians = rotation_angle_radians


