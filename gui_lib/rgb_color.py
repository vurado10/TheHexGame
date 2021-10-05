class RgbColor:
    def __init__(self, r: int, g: int, b: int):
        for value in [r, g, b]:
            if value < 0 or value > 255:
                raise Exception("rgb color channel must be from 0 to 255")

        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def create_from_string(hex_str: str):
        if len(hex_str) != 6:
            raise ValueError("Hex str length must be 6")

        return RgbColor(int(hex_str[:2], 16),
                        int(hex_str[2:4], 16),
                        int(hex_str[4:6], 16))

    def convert_to_tuple(self):
        return self.r, self.g, self.b
