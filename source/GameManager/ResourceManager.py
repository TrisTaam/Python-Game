import pygame
import os

from source.GameManager.Singleton import Singleton


class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self.is_preloaded = False
        self.is_sound_enable = True
        self.map_texture = {}
        self.map_font = {}
        self.map_sound = {}
        self.custom_cursor = None
        self.path = os.getcwd() + "\\Data\\"
        self.texture_path = self.path + "\\Texture\\"
        self.font_path = self.path + "\\Font\\"
        self.sound_path = self.path + "\\Sound\\"

    def __del__(self):
        self.map_texture.clear()

    def add_texture(self, name: str):
        texture = pygame.image.load(self.texture_path + name + ".png").convert_alpha()
        if texture in self.map_texture:
            return
        self.map_texture[name] = texture

    def remove_texture(self, name: str):
        if name in self.map_texture:
            del self.map_texture[name]

    def get_texture(self, name: str):
        if name in self.map_texture:
            return self.map_texture[name]
        self.add_texture(name)
        return self.get_texture(name)

    def has_texture(self, name: str) -> bool:
        return name in self.map_texture

    def add_font(self, name: str):
        font_name, font_size = name.split("_")
        font_size = int(font_size)
        font = pygame.font.Font(self.font_path + font_name + ".ttf", font_size)
        if font in self.map_font:
            return
        self.map_font[name] = font

    def remove_font(self, name: str):
        if name in self.map_font:
            del self.map_font[name]

    def get_font(self, name: str) -> pygame.font.Font:
        if name in self.map_font:
            return self.map_font[name]
        self.add_font(name)
        return self.get_font(name)

    def has_font(self, name: str) -> bool:
        return name in self.map_font

    def add_sound(self, name: str):
        sound = pygame.mixer.Sound(self.sound_path + name + ".wav")
        if sound in self.map_sound:
            return
        self.map_sound[name] = sound

    def remove_sound(self, name: str):
        if name in self.map_sound:
            del self.map_sound[name]

    def get_sound(self, name: str):
        if name in self.map_sound:
            return self.map_sound[name]
        self.add_sound(name)
        return self.get_sound(name)

    def has_sound(self, name: str) -> bool:
        return name in self.map_sound

    def play_sound(self, name: str):
        if self.is_sound_enable:
            self.get_sound(name).play()

    def is_enable_sound(self) -> bool:
        return self.is_sound_enable

    def enable_sound(self):
        self.is_sound_enable = True

    def disable_sound(self):
        self.is_sound_enable = False

    def preload(self):
        if self.is_preloaded:
            return
            # FONT
        self.add_font("Silver")
        # SOUND
        sound_list = [
            "cash",
            "drop1",
            "drop2",
            "drop3",
            "shoot",
            "smb_gameover",
            "smb_stage_clear",
        ]
        for sound in sound_list:
            self.add_sound(sound)
        # TEXTURE
        texture_list = [
            "bg-about",
            "bg-dead",
            "bg-end",
            "bg",
            "bg2",
            "intro",
            "logo",
            "chess/Board",
            "chess/CashCounter",
            "chess/MoveBox",
            "chess/card/B_Cardbox",
            "chess/card/W_Cardbox",
            "chess/gun/Bullet-empty",
            "chess/gun/Bullet-filled",
            "chess/gun/Shotgun",
            "chess/piece/B_Bishop",
            "chess/piece/B_King",
            "chess/piece/B_Knight",
            "chess/piece/B_Pawn",
            "chess/piece/B_Queen",
            "chess/piece/B_Rook",
            "chess/piece/W_Bishop",
            "chess/piece/W_King",
            "chess/piece/W_Knight",
            "chess/piece/W_Pawn",
            "chess/piece/W_Queen",
            "chess/piece/W_Rook",
            "cursor/point",
            "cursor/shoot",
            "cursor/target",
            "gui/btnAbout_handle",
            "gui/btnAbout_idle",
            "gui/btnBackToMenu_handle",
            "gui/btnBackToMenu_idle",
            "gui/btnContinue_handle",
            "gui/btnContinue_idle",
            "gui/btnEasy_handle",
            "gui/btnEasy_idle",
            "gui/btnExit_handle",
            "gui/btnExit_idle",
            "gui/btnHard_handle",
            "gui/btnHard_idle",
            "gui/btnHome_handle",
            "gui/btnHome_idle",
            "gui/btnMenu_handle",
            "gui/btnMenu_idle",
            "gui/btnNormal_handle",
            "gui/btnNormal_idle",
            "gui/btnPlay_handle",
            "gui/btnPlay_idle",
            "gui/btnSound_disable",
            "gui/btnSound_enable",
            "gui/shopBoard",
        ]
        for texture in texture_list:
            if not self.has_texture(texture):
                self.add_texture(texture)

        # PRELOADED
        self.is_preloaded = True
