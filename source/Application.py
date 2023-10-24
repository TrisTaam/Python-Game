import sys

import pygame as pg

import GameConfig
from source import WConnect, GSM
from source.GameStateManager.StateTypes import StateTypes


class Application:
    def __init__(self):
        self.window = None

    def __del__(self):
        if self.window is None:
            del self.window

    def init(self):
        pg.init()
        pg.display.set_caption(GameConfig.GAME_TITLE)
        self.window = pg.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        WConnect.set_window(self.window)
        GSM.change_state(StateTypes.INTRO)

    def run(self):
        self.init()
        clock = pg.time.Clock()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            delta_time = clock.tick(GameConfig.FRAMERATE_LIMIT) / 1000.0
            self.update(delta_time)
            self.render()

    def update(self, delta_time: float):
        if GSM.need_to_change_state():
            GSM.perform_state_change()
        GSM.active_state.update(delta_time)

    def render(self):
        GSM.active_state.render()
        pg.display.flip()
