import pygame
import random
import time
import threading
from components.SpriteSheet import SpriteSheet

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen, dific):
        super().__init__()
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        # SPAWNANDO
        self.x = random.randrange(0, self.SW)
        self.y = -20

        # SE FOR A PIMEIRA
        self.e_primeira = True

        # setar velocidade de acordo com a velocidade
        if dific <= 5:
            self.velocidade_range_min = 1
            self.velocidade_range_max = 6
        elif 5 < dific <= 10:
            self.velocidade_range_min = 5
            self.velocidade_range_max = 9
        elif 10 < dific <= 15:
            self.velocidade_range_min = 8
            self.velocidade_range_max = 12

        self.speed = random.randrange(self.velocidade_range_min, self.velocidade_range_max)
        self.image, self.rect = SpriteSheet().cria_enzima()
        self.rect.topleft = (self.x, self.y)

    def update(self, jogador):
        self.y += self.speed
        self.rect.y = self.y

        # Colisão
        rectJogador = pygame.Rect(jogador.x, jogador.y, jogador.JOGADOR_WIDTH, jogador.JOGADOR_HEIGHT)
        if self.rect.colliderect(rectJogador):
            jogador.tira_vida()
            self.respawn()

        # Checar se o objeto está fora da tela
        if self.y > self.SH + 50:
            self.respawn()

    def respawn(self):
        self.y = -100
        self.rect.y = self.y
        self.x = random.randrange(0, self.SW)
        self.rect.x = self.x
        self.speed = random.randrange(self.velocidade_range_min, self.velocidade_range_max)
