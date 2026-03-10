import sys
from datetime import datetime

import pygame
from pygame import Surface, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, C_WHITE
from code.DBProxy import DBProxy
from code.paths import resource_path


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load(resource_path('asset/ScoreBg.png')).convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, player_score: list[int]):
        pygame.mixer_music.load(resource_path('asset/Score.mp3'))
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'FINISH!', C_YELLOW, SCORE_POS['Title'])
            text = 'Enter Driver name (4 characters):'
            score = player_score[0]
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': int(score), 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load(resource_path('asset/Score.mp3'))
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 DISTANCE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     DISTANCE        DATE      ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for idx, player_score in enumerate(list_score):
            if idx not in SCORE_POS:
                break
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_YELLOW, SCORE_POS[idx])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
