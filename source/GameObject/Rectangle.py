import pygame

from source import WConnect


class Rectangle:
    def __init__(self, position, size, color=(255, 255, 255), border_color=(0, 0, 0)):
        from pygame import Rect
        x, y = position
        width, height = size
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.border_color = border_color
        self.__origin_x = 0
        self.__origin_y = 0

    @property
    def origin(self):
        return self.__origin_x, self.__origin_y

    @origin.setter
    def origin(self, value):
        self.__origin_x, self.__origin_y = value

    @property
    def position(self):
        return self.rect.x, self.rect.y

    @position.setter
    def position(self, value):
        self.rect.x, self.rect.y = value

    @property
    def absolute_position(self):
        return self.rect.x - self.__origin_x, self.rect.y - self.__origin_y

    def render(self):
        from pygame.draw import rect
        x, y = self.absolute_position
        absolute_rect = pygame.Rect(x, y, self.rect.w, self.rect.h)
        rect(WConnect.window, self.color, absolute_rect)
        rect(WConnect.window, self.border_color, absolute_rect, 1)

    def contain(self, position):
        return self.rect.collidepoint(position)
