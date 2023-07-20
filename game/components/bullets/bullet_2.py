import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_PLAYER, PLAYER_TYPE, SCREEN_HEIGHT


class Bullet_2(Bullet):
    SPEED = 15
    BULLETS = {PLAYER_TYPE : BULLET_PLAYER}

    def __init__(self, spaceship):
        super().__init__(spaceship)
        self.image = pygame.transform.scale(self.BULLETS[self.owner], (30, 10))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
