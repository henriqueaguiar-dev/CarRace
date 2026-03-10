#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for name in ('Level1Bg4',):
                    list_bg.append(Background(name, (0, 0)))
                    list_bg.append(Background(name, (0, -WIN_HEIGHT)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for name in ('Level2Bg3',):
                    list_bg.append(Background(name, (0, 0)))
                    list_bg.append(Background(name, (0, -WIN_HEIGHT)))
                return list_bg
            case 'Player1':
                road_left = int(WIN_WIDTH * 0.22)
                return Player('Player1', (road_left + 10, WIN_HEIGHT - 90))
            case 'Enemy1':
                road_left = int(WIN_WIDTH * 0.22)
                road_right = int(WIN_WIDTH * 0.78)
                return Enemy('Enemy1', (random.randint(road_left + 10, road_right - 60), random.randint(-200, -60)))
            case 'Enemy2':
                road_left = int(WIN_WIDTH * 0.22)
                road_right = int(WIN_WIDTH * 0.78)
                return Enemy('Enemy2', (random.randint(road_left + 10, road_right - 60), random.randint(-220, -80)))
