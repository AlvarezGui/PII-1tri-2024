import time
import pygame
from components.SpriteSheet import SpriteSheet

class Jogador(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen, model):
        super().__init__()
        modelo = self.carro_modelo(model)
        self.image_normal = modelo[0]
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.JOGADOR_WIDTH = 80
        aspect_ratio = self.image_normal.get_width() / self.image_normal.get_height()
        self.JOGADOR_HEIGHT = int(self.JOGADOR_WIDTH / aspect_ratio)
        self.image = pygame.transform.scale(self.image_normal, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))

        self.x = (self.SW - self.JOGADOR_WIDTH) // 2
        self.y = self.SH - self.JOGADOR_HEIGHT - 20
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

        self.speed = 6
        self.vida = 10
        self.image_boost = modelo[1]
        self.invencivel = False
        self.tempo_invencivel = 0.8  # Tempo de invencibilidade em segundos
        self.ultimo_hit = 0

    def update(self, keys):
        pos_antiga = (self.x, self.y)

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        pos_atual = (self.x, self.y)
        self.is_moving = pos_antiga != pos_atual

        if self.invencivel and time.time() - self.ultimo_hit > self.tempo_invencivel:
            self.invencivel = False

        self.rect.topleft = (self.x, self.y)
        if self.is_moving:
            self.image = pygame.transform.scale(self.image_boost, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))
        else:
            self.image = pygame.transform.scale(self.image_normal, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))

        self.x = max(0, min(self.x, self.SW - self.JOGADOR_WIDTH))
        self.y = max(0, min(self.y, self.SH - self.JOGADOR_HEIGHT))

    def tira_vida(self):
        if not self.invencivel:
            self.vida -= 1
            self.invencivel = True
            self.ultimo_hit = time.time()

    @staticmethod
    def carro_modelo(modelo):
        if modelo == "hamburguer":
            return (SpriteSheet().image_at((1611, 625, 309, 331), -1).convert_alpha(),
                    SpriteSheet().image_at((1292, 643, 309, 331), -1).convert_alpha())
        if modelo == "hotdog":
            return (SpriteSheet().image_at((968, 0, 309, 645), -1).convert_alpha(),
                    SpriteSheet().image_at((1279, 0, 309, 645), -1).convert_alpha())
        if modelo == "donut":
            return (SpriteSheet().image_at((327, 314, 309, 331), -1).convert_alpha(),
                    SpriteSheet().image_at((0, 320, 320, 331), -1).convert_alpha())
        if modelo == "abacate":
            return (SpriteSheet().image_at((320, 660, 319, 624), -1).convert_alpha(),
                    SpriteSheet().image_at((0, 663, 320, 624), -1).convert_alpha())
        if modelo == "ovo":
            return (SpriteSheet().image_at((960, 650, 324, 331), -1).convert_alpha(),
                    SpriteSheet().image_at((640, 656, 320, 331), -1).convert_alpha())
        return (SpriteSheet().image_at((1611, 625, 309, 331), -1).convert_alpha(),
                SpriteSheet().image_at((1292, 643, 309, 331), -1).convert_alpha())
