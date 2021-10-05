import unittest

from game_classes.match.hex_field import HexField


class HexFieldTests(unittest.TestCase):
    def test_get_adjacent_cells_when_border_cell(self):
        field = HexField(11, 11)
        test_suits = [
            ([1, 11], field.get_adjacent_cells(0)),
            ([9, 20, 21], field.get_adjacent_cells(10)),
            ([99, 100, 111], field.get_adjacent_cells(110)),
            ([109, 119], field.get_adjacent_cells(120))
        ]

        for expected, result in test_suits:
            self.assertCountEqual(result,
                                  expected,
                                  msg=f"expected: {expected}, "
                                      f"but was: {result}")

    def test_get_adjacent_cells_when_inner_cell(self):
        field = HexField(11, 11)
        result = field.get_adjacent_cells(12)
        expected = [1, 2, 11, 13, 22, 23]

        self.assertCountEqual(result,
                              expected,
                              msg=f"expected: {expected}, but was: {result}")