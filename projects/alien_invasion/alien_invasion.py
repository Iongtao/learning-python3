# !/usr/bin/env python3
# coding=utf-8

import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    # 初始化设置信息
    setting = Settings()

    # 创建游戏窗口
    screen = pygame.display.set_mode(
        (setting.screen_width, setting.screen_height))

    # 设置窗口标题
    pygame.display.set_caption('Alien Invasion')

    # 创建一个飞船
    ship = Ship(setting, screen)

    # 创建一个用于存储子弹的编组 
    # 这里可能和Bullet类中的sprite相关联了
    bullets = Group()

    # 开始游戏的主循环
    while True:

        # 监听键鼠时间
        check_events(setting, screen, ship, bullets)
        # 更新飞船信息
        ship.update()
        # 更新子弹信息
        bullets.update()
        # 更新屏幕信息
        update_screen(setting, screen, ship, bullets)


run_game()
