import threading
import time


class IntervalTimer:
    def __init__(self, interval, function):
        self.__interval = interval
        self.__function = function
        self.__is_pause = False
        self.__pause_event = threading.Event()

    # TODO: add cancel

    def start(self):
        self.__pause_event.set()
        threading.Thread(target=self.__start_main_loop).start()

    def pause(self):
        self.__pause_event.clear()

    def resume(self):
        self.__pause_event.set()

    def __start_main_loop(self):
        while True:
            time.sleep(self.__interval)
            self.__pause_event.wait()
            self.__function()
