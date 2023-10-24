from source.GameStateManager.GameStateBase import GameStateBase


class GSUpgrade(GameStateBase):
    def __int__(self):
        self.background = None
        self.alpha_color = None
        self.btn_back = None
        self.current_time = None

    def __del__(self):
        pass

    def exit(self):
        super().exit()

    def pause(self):
        super().pause()

    def resume(self):
        super().resume()

    def init(self):
        super().init()

    def update(self, delta_time: float):
        super().update(delta_time)

    def render(self):
        super().render()

    def update_color(self):
        pass
