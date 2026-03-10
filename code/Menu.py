#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame.image
from pygame import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW
from code.paths import resource_path


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(resource_path('asset/MenuBg.png')).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.title_pos = (WIN_WIDTH / 2, 125)
        self.menu_y = WIN_HEIGHT - 20
        self.menu_spacing = 120
        center_x = WIN_WIDTH / 2
        offset = (len(MENU_OPTION) - 1) / 2
        self.menu_positions = [
            (center_x + (i - offset) * self.menu_spacing, self.menu_y)
            for i in range(len(MENU_OPTION))
        ]
        self.control_surf = pygame.image.load(resource_path('asset/control.png')).convert_alpha()
        max_w = WIN_WIDTH - 40
        control_area_top = 140
        control_area_bottom = self.menu_y - 10
        max_h = max(10, control_area_bottom - control_area_top)
        w, h = self.control_surf.get_size()
        scale = min(max_w / w, max_h / h)
        if scale != 1.0:
            new_size = (max(1, int(w * scale)), max(1, int(h * scale)))
            self.control_surf = pygame.transform.smoothscale(self.control_surf, new_size)
        self.control_rect = self.control_surf.get_rect(midbottom=(WIN_WIDTH / 2, control_area_bottom))

    def run(self):
        menu_option = 0
        pygame.mixer_music.load(resource_path('asset/Menu.mp3'))
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Car Race", C_ORANGE, self.title_pos)
            self.window.blit(source=self.control_surf, dest=self.control_rect)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_YELLOW, self.menu_positions[i])
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, self.menu_positions[i])
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:  # RIGHT KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_LEFT:  # LEFT KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
