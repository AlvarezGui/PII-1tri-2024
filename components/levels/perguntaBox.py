import pygame
import random
from components.SpriteSheet import SpriteSheet

class PerguntaBox(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        super().__init__()
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.WIDTH = 50
        self.HEIGHT = 80

        self.x = random.randrange(0, self.SW)
        self.y = -20
        self.speed = random.randrange(1, 6)
        self.is_active = False

        self.image = SpriteSheet().image_at((1597, 22, 313, 248), -1).convert_alpha()
        aspect_ratio = self.image.get_width() / self.image.get_height()
        new_height = int(self.WIDTH / aspect_ratio)
        self.image = pygame.transform.scale(self.image, (self.WIDTH, new_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, jogador):
        self.y += self.speed
        self.rect.y = self.y

        rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        jogador_rect = pygame.Rect(jogador.x, jogador.y, jogador.JOGADOR_WIDTH, jogador.JOGADOR_HEIGHT)

        if rect.colliderect(jogador_rect):
            self.is_active = True

        if self.y > self.SH + 50:
            self.respawn()

    def respawn(self):
        self.x = random.randrange(0, self.SW)
        self.y = -20
        self.rect.topleft = (self.x, self.y)
        self.speed = random.randrange(2, 6)
