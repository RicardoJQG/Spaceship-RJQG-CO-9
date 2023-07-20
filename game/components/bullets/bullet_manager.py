import pygame
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_2 import Bullet_2
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE, SHIELD_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.bullets = []

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score += 1

        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    print(game.death_count)
                    pygame.time.delay(1000)
                    break

    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
        if spaceship.type == PLAYER_TYPE and not self.bullets:
            self.enemy_bullets.append(Bullet_2(spaceship)) 