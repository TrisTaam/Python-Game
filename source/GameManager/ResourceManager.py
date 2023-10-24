import pygame
import os

from source.GameManager.Singleton import Singleton


class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self.isPreloaded = None
        self.isSoundEnable = None
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
        pass

    def remove_font(self, name: str):
        pass

    def get_font(self, name: str):
        pass

    def has_font(self, name: str) -> bool:
        pass

    def add_sound(self, name: str):
        pass

    def remove_sound(self, name: str):
        pass

    def get_sound(self, name: str):
        pass

    def has_sound(self, name: str) -> bool:
        pass

    def play_sound(self, name: str):
        pass

    def is_enable_sound(self) -> bool:
        return self.isSoundEnable

    def enable_sound(self):
        self.isSoundEnable = True

    def disable_sound(self):
        self.isSoundEnable = False

    def preload(self):
        pass
