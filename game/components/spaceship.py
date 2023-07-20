import pygame
from pygame.sprite import Sprite
from game.components.bullets import bullet_manager
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_2 import Bullet_2

from game.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP


class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    SPACESHIP_HEIGHT = 60
    SPACESHIP_WIDTH = 50


    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0


    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_SPACE]:
            game.bullet_manager.add_bullet(self)

    def shoot(self, bullet_manager):
        bullet = Bullet_2(self.rect.centerx, self.rect.top)
        bullet_manager.add(bullet)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        else:
            self.rect.x = 0

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale (image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.power_up_time_up = time_up
        self.power_up_type = type

    def draw_power_up(self, game):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)  
            if time_left >= 0:
                game.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enabled for {time_left} seconds", y=50, color=(255, 255, 255))
            else:
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))