from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
import random


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        if not self.enemies:
            self.enemies.append(random.choice([Enemy(), Enemy_2()]))

        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
        self.enemies = []