class RgbColor:
    def __init__(self, r: int, g: int, b: int):
        for value in [r, g, b]:
            if value < 0 or value > 255:
                raise Exception("rgb color channel must be from 0 to 255")

        self.r = r
        self.g = g
        self.b = b

    def convert_to_tuple(self):
        return self.r, self.g, self.b
