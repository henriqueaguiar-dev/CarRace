import pygame
from pygame import Surface

from code.paths import resource_path

_CRASH_SOUND = None


def play_crash_sound():
    global _CRASH_SOUND
    if _CRASH_SOUND is None:
        try:
            _CRASH_SOUND = pygame.mixer.Sound(resource_path('asset/crash.wav'))
            _CRASH_SOUND.set_volume(0.45)
        except Exception:
            _CRASH_SOUND = False
    if _CRASH_SOUND:
        _CRASH_SOUND.play()


class Explosion:
    def __init__(self, position: tuple[int, int]):
        self.name = "Explosion"
        self.max_life = 12
        self.life = self.max_life
        self.health = 1
        self.colliding_with = set()
        self.size = 64
        self.surf: Surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center=position)
        self._redraw()

    def _redraw(self):
        self.surf.fill((0, 0, 0, 0))
        progress = 1.0 - (self.life / self.max_life)
        radius = int(8 + progress * 24)
        alpha = int(220 * (1.0 - progress))
        center = (self.size // 2, self.size // 2)
        pygame.draw.circle(self.surf, (255, 200, 0, alpha), center, radius)
        ring_alpha = int(180 * (1.0 - progress))
        pygame.draw.circle(
            self.surf,
            (255, 80, 0, ring_alpha),
            center,
            min(self.size // 2 - 2, radius + 8),
            2,
        )

    def move(self):
        self.life -= 1
        if self.life <= 0:
            self.health = 0
            return
        self._redraw()
