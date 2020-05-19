import pygame
from pygame.sprite import Sprite

'''
Sprite精灵 可将游戏中相关的元素编组 进而同时操作编组中的所有元素
'''


class Bullet(Sprite):

    def __init__(self, setting, screen, ship):

        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
