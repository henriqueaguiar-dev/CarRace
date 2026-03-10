#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE
from code.paths import resource_path


class Entity(ABC):
    def __init__(self, name: str, position: tuple, sprite_name=None):
        self.name = name
        self.sprite_name = sprite_name or name
        self.surf = pygame.image.load(resource_path('asset/' + self.sprite_name + '.png')).convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'
        self.colliding_with = set()

    def set_sprite(self, sprite_name: str):
        if self.sprite_name == sprite_name:
            return
        self.sprite_name = sprite_name
        center = self.rect.center
        self.surf = pygame.image.load(resource_path('asset/' + self.sprite_name + '.png')).convert_alpha()
        self.rect = self.surf.get_rect(center=center)

    def on_hit(self, damage: int, other):
        pass

    @abstractmethod
    def move(self):
        pass
