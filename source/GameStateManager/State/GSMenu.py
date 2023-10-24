from source import WConnect, DATA
from source.GameStateManager.GameStateBase import GameStateBase


class GSMenu(GameStateBase):
    def __init__(self):
        super().__init__()
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
        self.background = DATA.get_texture("bg")

    def update(self, delta_time: float):
        super().update(delta_time)

    def render(self):
        super().render()
        WConnect.get_window().blit(self.background, (0, 0))

    def update_color(self):
        pass
