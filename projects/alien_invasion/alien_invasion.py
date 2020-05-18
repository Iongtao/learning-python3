# !/usr/bin/env python3
# coding=utf-8

import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()

    setting = Settings()

    screen = pygame.display.set_mode(
        (setting.screen_width, setting.screent_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(setting.bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()
