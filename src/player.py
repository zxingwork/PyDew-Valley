import pygame
from setting import *
from typing import *
from math import sqrt
from support import *
from timer import Timer


class PlayerStatus:
    up = 'up'
    down = 'down'
    right = 'right'
    left = 'left'
    up_idle = 'up_idle'
    down_idle = 'down_idle'
    left_idle = 'left_idle'
    right_idle = 'right_idle'
    up_axe = 'up_axe'
    down_axe = 'down_axe'
    left_axe = 'left_axe'
    right_axe = 'right_axe'
    up_water = 'up_water'
    down_water = 'down_water'
    right_water = 'right_water'
    left_water = 'left_water'


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.animations = {}
        self.import_assets()
        self.status = PlayerStatus.up
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement attribute
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # tools
        self.selected_tool = 'axe'

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'right': [], 'left': [],
                           'up_idle': [], 'down_idle': [], 'right_idle': [], 'left_idle': [],
                           'up_hoe': [], 'down_hoe': [], 'right_hoe': [], 'left_hoe': [],
                           'up_axe': [], 'down_axe': [], 'right_axe': [], 'left_axe': [],
                           'up_water': [], 'down_water': [], 'right_water': [], 'left_water': []}
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

        print(self.animations)

    def animate(self, dt):
        self.frame_index += len(self.animations[self.status]) * dt
        if self.frame_index > len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = PlayerStatus.up
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = PlayerStatus.down
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = PlayerStatus.left
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = PlayerStatus.right
        else:
            self.direction.x = 0

        # tool use
        if keys[pygame.K_SPACE]:
            # timer for the tool use

            pass

    def get_status(self):
        # if the player is not moving
        # add _idle to the status
        if self.direction.magnitude() == 0:
            if self.status + "_idle" in self.animations:
                self.status += '_idle'

    def move(self, dt):
        if self.direction.x or self.direction.y:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt) -> None:
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
