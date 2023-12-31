import sys

import pygame

from source import WConnect, DATA, GSM, GameConfig
from source.GameObject.GameButton import GameButton
from source.GameObject.SoundButton import SoundButton
from source.GameObject.Sprite import Sprite
from source.GameStateManager.GameStateBase import GameStateBase
from source.GameStateManager.StateTypes import StateTypes


class GSMenu(GameStateBase):
    def __init__(self):
        super().__init__()
        self.background = None
        self.logo = Sprite()
        self.btn_list = []
        self.sound_btn = SoundButton()
        self.current_time = 0.0
        self.is_perform_transition = True
        self.shotgun = Sprite()

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
        self.logo.texture = DATA.get_texture("logo")
        self.logo.origin = (self.logo.size[0] / 2, self.logo.size[1] / 2)
        self.logo.position = (GameConfig.SCREEN_WIDTH / 2, GameConfig.SCREEN_HEIGHT / 2)
        self.is_perform_transition = True
        self.current_time = 0.0

        # Play button
        play_btn = GameButton("btnPlay", (61.0, 36.0))
        play_btn.init()
        play_btn.position = (640.0, 500.0)
        play_btn.set_on_click(lambda: GSM.change_state(StateTypes.MODE_SELECT))
        self.btn_list.append(play_btn)

        # About button
        about_btn = GameButton("btnAbout", (79.0, 36.0))
        about_btn.init()
        about_btn.position = (640.0, 540.0)
        about_btn.set_on_click(lambda: GSM.change_state(StateTypes.ABOUT))
        self.btn_list.append(about_btn)

        # Exit button
        exit_btn = GameButton("btnExit", (61.0, 32.0))
        exit_btn.init()
        exit_btn.position = (640.0, 580.0)
        exit_btn.set_on_click(lambda: (pygame.quit(), sys.exit()))
        self.btn_list.append(exit_btn)

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
