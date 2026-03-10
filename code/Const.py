# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg4': 4,
    'Level2Bg3': 3,
    'Enemy1': 3,
    'Enemy2': 3,
}

ENTITY_HEALTH = {
    'Level1Bg4': 999,
    'Level2Bg3': 999,
    'Player1': 4,
    'Enemy1': 60,
    'Enemy2': 80,
}

ENTITY_DAMAGE = {
    'Level1Bg4': 0,
    'Level2Bg3': 0,
    'Player1': 10,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_SCORE = {
    'Level1Bg4': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Enemy1': 50,
    'Enemy2': 75,
}

# M
MENU_OPTION = ('NEW RACE',
               'SCORE',
               'EXIT',)

# P
PLAYER_KEY_ACCEL = {'Player1': pygame.K_UP}
PLAYER_KEY_BRAKE = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}

# S
SPAWN_TIME = 1500

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 30000  # 30s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# P
PLAYER_ACCEL = 0.18
PLAYER_BRAKE = 0.22
PLAYER_FRICTION = 0.06
PLAYER_MAX_SPEED = 4.8
PLAYER_MAX_REVERSE = 2.2
PLAYER_TURN_SPEED = 3.2

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
