import random
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2


class Enemy_2(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.speed_x = 7
        self.speed_y = 4
        self.move_x = random.randint(50, 150)
        self.shooting_time = random.randint(20, 40)

