import time
import unittest

from gui_lib.interval_timer import IntervalTimer


class IntervalTimerTests(unittest.TestCase):
    def test_interval_timer(self):
        # TODO: write correct tests
        k = 1000

        def foo():
            nonlocal k
            k -= 1
            print(k)

        timer = IntervalTimer(1.0, foo)
        timer.start()

        time.sleep(10.0)
        timer.pause()

        self.assertTrue(True)
