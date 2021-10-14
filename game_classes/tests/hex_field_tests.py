import unittest

from game_classes.match.hex_field import HexField


class HexFieldTests(unittest.TestCase):
    @staticmethod
    def make_std_msg(expected, result):
        return f"expected: {expected}, but was: {result}"

    def test_get_adjacent_cells_when_border_cell(self):
        field = HexField(11, 11)
        test_suits = [
            ([1, 11], field.get_adjacent_cells(0)),
            ([9, 20, 21], field.get_adjacent_cells(10)),
            ([99, 100, 111], field.get_adjacent_cells(110)),
            ([109, 119], field.get_adjacent_cells(120))
        ]

        for expected, result in test_suits:
            msg = HexFieldTests.make_std_msg(expected, result)
            self.assertCountEqual(result,
                                  expected,
                                  msg=msg)

    def test_get_adjacent_cells_when_inner_cell(self):
        field = HexField(11, 11)
        result = field.get_adjacent_cells(12)
        expected = [1, 2, 11, 13, 22, 23]

        msg = HexFieldTests.make_std_msg(expected, result)
        self.assertCountEqual(result,
                              expected,
                              msg=msg)

    def test_get_path_from_tracking(self):
        input_data = {0: None, 1: 0, 2: 3, 3: 1}
        result = HexField._get_path_from_tracking(input_data, 3)
        expected = [0, 1, 3]

        msg = HexFieldTests.make_std_msg(expected, result)

        self.assertSequenceEqual(result, expected, msg=msg)
