from __future__ import annotations
import os.path

import pygame
from settings import *
from player import Player


class Overlay:
    def __init__(self, player: Player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.play = player

        # import
        overlay_path = "../graphics/overlay/"
        self.tools_surf = {tool: pygame.image.load(os.path.join(overlay_path, tool + '.png')).convert_alpha() for tool
                           in player.tools}
        self.seeds_surf = {seed: pygame.image.load(os.path.join(overlay_path, seed + '.png')).convert_alpha() for seed
                           in player.seeds}

    def display(self):
        # tools
        tool_surf: pygame.Surface = self.tools_surf[self.play.selected_tool]
        tool_rectangle = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rectangle)

        # seed
        seed_surf: pygame.Surface = self.seeds_surf[self.play.selected_seed]
        seed_rectangle = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rectangle)
