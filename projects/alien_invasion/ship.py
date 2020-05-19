# !/usr/bin/env python3
# coding=utf-8

import pygame

class Ship():

    def __init__(self, setting, screen):
        '''初始化飞船并设置初始位置'''
        self.screen = screen
        self.setting = setting

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting.ship_speed_factor
        self.rect.centerx = self.center
        