import os.path

import pygame
from setting import *


class Overlay:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.play = player

        # import
        overlay_path = "../graphics/overlay/"
        self.tools_surf = {tool: pygame.image.load(os.path.join(overlay_path, tool)).convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(os.path.join(overlay_path, seed)).convert_alpha() for seed in player.seeds}

