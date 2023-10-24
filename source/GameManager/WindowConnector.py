import pygame.surface

from source.GameManager.Singleton import Singleton


class WindowConnector(metaclass=Singleton):
    def __init__(self):
        self.window = None

    def set_window(self, window: pygame.surface.Surface):
        self.window = window

    def get_window(self) -> pygame.surface.Surface:
        return self.window
