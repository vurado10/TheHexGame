def convert_negative_to_zero(x):
    return x if x >= 0 else 0


def sign(x: int):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


class Vector2:
    def __init__(self, x=0, y=0):
        if type(x) != int or type(y) != int:
            raise TypeError
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.add(self, other)

    def __mul__(self, factor):
        return self.mul(self, factor)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iadd__(self, other):
        return self.__add__(other)

    def __imod__(self, factor):
        return self.mod(self, factor)

    def __ne__(self, other):
        return not (self == other)

    def __sub__(self, other):
        return Vector2.add(self, other * (-1))

    def __isub__(self, other):
        return self.__sub__(other)

    def __copy__(self):
        return Vector2(self.x, self.y)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    @staticmethod
    def add(v1, v2):
        return Vector2(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def mul(v1, factor):
        return Vector2(v1.x * factor, v1.y * factor)

    @staticmethod
    def mod(v1, factor):
        return Vector2(v1.x % factor, v1.y % factor)

    @staticmethod
    def abs(v):
        return Vector2(abs(v.x), abs(v.y))

    def norm(self):
        return Vector2(sign(self.x), sign(self.y))

    def convert_negative_to_zero(self):
        return Vector2(convert_negative_to_zero(self.x), convert_negative_to_zero(self.y))

    @property
    def horizontal(self):
        return Vector2(self.x, 0)

    @property
    def vertical(self):
        return Vector2(0, self.y)


class Vector2Constants:
    ZERO = Vector2(0, 0)
    UP = Vector2(0, 1)
    DOWN = Vector2(0, -1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    EDITOR_UP = DOWN
    EDITOR_DOWN = UP
