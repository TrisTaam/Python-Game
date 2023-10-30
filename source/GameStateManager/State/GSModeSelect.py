from source import DATA, WConnect, GSM, GameConfig
from source.GameObject.GameButton import GameButton
from source.GameObject.SoundButton import SoundButton
from source.GameObject.Sprite import Sprite
from source.GameStateManager.GameStateBase import GameStateBase
from source.GameStateManager.StateTypes import StateTypes


class GSModeSelect(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        self.logo = Sprite()
        self.current_time = 0.0
        self.is_perform_transition = True
        self.btn_list = []
        self.sound_btn = SoundButton()

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
        self.is_perform_transition = True
        self.current_time = 0.0
        self.background = DATA.get_texture("bg")
        self.logo.texture = DATA.get_texture("logo")
        self.logo.origin = (self.logo.size[0] / 2, self.logo.size[1] / 2)
        self.logo.position = (GameConfig.SCREEN_WIDTH / 2, GameConfig.SCREEN_HEIGHT / 2)
        # Easy button
        easy_btn = GameButton("btnEasy", (65.0, 36.0))
        easy_btn.init()
        easy_btn.position = (640.0, 500.0)
        easy_btn.set_on_click(lambda: (
            # GameRule.setMode(EASY);
            GSM.change_state(StateTypes.PLAY),
        ))
        self.btn_list.append(easy_btn)

        # Normal button
        normal_btn = GameButton("btnNormal", (89.0, 32.0))
        normal_btn.init()
        normal_btn.position = (640.0, 540.0)
        normal_btn.set_on_click(lambda: (
            # GameRule.setMode(NORMAL);
            GSM.change_state(StateTypes.PLAY),
        ))
        self.btn_list.append(normal_btn)

        # Hard button
        hard_btn = GameButton("btnHard", (65.0, 32.0))
        hard_btn.init()
        hard_btn.position = (640.0, 580.0)
        hard_btn.set_on_click(lambda: (
            # GameRule.setMode(HARD);
            GSM.change_state(StateTypes.PLAY),
        ))
        self.btn_list.append(hard_btn)

        self.sound_btn.init()

    def update(self, delta_time: float):
        super().update(delta_time)
        if self.is_perform_transition:
            self.current_time += delta_time
            if self.current_time < GameConfig.TRANSITION_DURATION * 2:
                pass
            else:
                self.is_perform_transition = False
            return

        # Menu update
        for btn in self.btn_list:
            btn.update(delta_time)

        self.sound_btn.update(delta_time)

    def render(self):
        super().render()
        WConnect.get_window().blit(self.background, (0, 0))
        WConnect.get_window().blit(self.logo.texture, self.logo.absolute_position)

        # Menu render
        for btn in self.btn_list:
            btn.render()

        self.sound_btn.render()

    def update_color(self):
        pass
