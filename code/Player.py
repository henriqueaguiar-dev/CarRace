#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame.key

from code.Const import WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_ACCEL, PLAYER_KEY_BRAKE, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_ACCEL, PLAYER_BRAKE, PLAYER_FRICTION, PLAYER_MAX_SPEED, PLAYER_MAX_REVERSE, PLAYER_TURN_SPEED
from code.Entity import Entity
from code.paths import resource_path


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        sprite_name = name
        if name == 'Player1':
            preferred = f'{name}_0'
            if os.path.exists(resource_path(f'asset/{preferred}.png')):
                sprite_name = preferred
        super().__init__(name, position, sprite_name=sprite_name)
        self.damage_stage = 0
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.centery)
        self.speed = 0.0

    def on_hit(self, damage: int, other):
        if self.name != 'Player1':
            return
        if self.damage_stage >= 3:
            return
        self.damage_stage += 1
        self.set_sprite(f'{self.name}_{self.damage_stage}')

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_ACCEL[self.name]]:
            self.speed = min(self.speed + PLAYER_ACCEL, PLAYER_MAX_SPEED)
        elif pressed_key[PLAYER_KEY_BRAKE[self.name]]:
            self.speed = max(self.speed - PLAYER_BRAKE, -PLAYER_MAX_REVERSE)
        else:
            if self.speed > 0:
                self.speed = max(0.0, self.speed - PLAYER_FRICTION)
            elif self.speed < 0:
                self.speed = min(0.0, self.speed + PLAYER_FRICTION)

        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.pos_x -= PLAYER_TURN_SPEED
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.pos_x += PLAYER_TURN_SPEED

        self.pos_y -= self.speed

        half_w = self.rect.width / 2
        half_h = self.rect.height / 2
        self.pos_x = max(half_w, min(WIN_WIDTH - half_w, self.pos_x))
        self.pos_y = max(half_h, min(WIN_HEIGHT - half_h, self.pos_y))

        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)
