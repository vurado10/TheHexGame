import abc

class Painter(metaclass=abc.ABCmeta):
    @abc.abstractmethod
    def draw(self):
        pass