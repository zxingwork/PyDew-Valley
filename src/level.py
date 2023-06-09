import pygame
from settings import *
from player import Player
from overlay import Overlay
from typing import *


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CamaraGroup()
        self.player: Optional[Player] = None

        self.setup()

        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((100, 100), self.all_sprites)
        pass

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        self.overlay.display()


class CamaraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
