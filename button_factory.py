from button import Button
from factory import Factory
from figure import Figure
from label import Label


class ButtonFactory(Factory):
    def __init__(self, figure: Figure, label: Label, on_click_function=None):
        self._figure = figure
        self._label = label
        self._on_click_function = on_click_function

    def create(self):
        button_obj = Button(self._figure, self._label)
        button_obj.on_click_function = self._on_click_function

        return button_obj
