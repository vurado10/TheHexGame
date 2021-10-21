from game_classes.ai.bot_events_types import BotEventsTypes
from game_classes.game_domain.match import Match
from gui_lib.scene_elements.gui_elements.widget import Widget
from pygame.event import Event
from pygame.math import Vector2


class BotListener(Widget):
    def __init__(self, match: Match):
        super().__init__(Vector2(0, 0), [BotEventsTypes.CALC_FINISH])

        self.__match = match

        self.add_handler(BotEventsTypes.CALC_FINISH,
                         self.handle_on_calc_finish)

    def is_valid_event(self, event: Event) -> bool:
        return True

    def handle_on_calc_finish(self, listener, event):
        self.__match.make_move(event.cell_index, event.player_name)


