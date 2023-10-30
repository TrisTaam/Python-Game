from source import WConnect, GameConfig, DATA, GSM
from source.GameObject.GameButton import GameButton
from source.GameObject.SoundButton import SoundButton
from source.GameStateManager.GameStateBase import GameStateBase


class GSPlay(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        self.current_time = 0.0
        self.sound_btn = SoundButton()
        self.home_btn = None
        self.is_perform_transition = True

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
        self.home_btn = GameButton("btnHome", (16.0, 16.0))
        self.home_btn.init()
        self.home_btn.scale = (3.0, 3.0)
        size = (self.home_btn.size[0] * self.home_btn.scale[0], self.home_btn.size[1] * self.home_btn.scale[1])
        self.home_btn.origin = (size[0] / 2, size[1] / 2)
        self.home_btn.position = (
            GameConfig.SCREEN_WIDTH - size[0] / 2 - 10.0, size[1] / 2 + 5.0)
        self.home_btn.set_on_click(lambda: (
            GSM.pop_state(),
            GSM.pop_state()
        ))
        self.sound_btn.init()
        self.is_perform_transition = True
        self.current_time = 0.0
        self.background = DATA.get_texture("bg")

    def update(self, delta_time: float):
        super().update(delta_time)
        if self.is_perform_transition:
            self.current_time += delta_time
            if self.current_time < GameConfig.TRANSITION_DURATION * 2:
                pass
            else:
                self.is_perform_transition = False
            return

        self.sound_btn.update(delta_time)
        self.home_btn.update(delta_time)
        self.shotgun.update(delta_time)

    def render(self):
        super().render()
        WConnect.get_window().blit(self.background, (0, 0))
        self.sound_btn.render()
        self.home_btn.render()

    def update_color(self):
        pass
