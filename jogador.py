import pygame

class jogador():

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen) -> None:
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.JOGADOR_WIDTH = 50
        self.JOGADOR_HEIGHT = 80

        self.x = (self.SW - self.JOGADOR_WIDTH) // 2
        self.y = self.SH - self.JOGADOR_HEIGHT - 20
        self.speed = 6

        self.rect = pygame.Rect(self.x, self.y, self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT)

    @staticmethod
    def desenhar_jogador(self):
        # TODO adicionar sprite do jogador :3
        pygame.draw.circle(self.screen, "red", (self.x, self.y), 40)

    @staticmethod
    def mover_jogador(self, keys):
        # input do usuario
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # garantir que o jogador não saia da tela e não passe da metade de sua altura
        if self.x < 0:
            self.x = 0
        elif self.x > self.SW - self.JOGADOR_WIDTH:
            self.x = self.SW - self.JOGADOR_WIDTH
        if self.y < self.SH / 2:
            self.y = self.SH / 2
        elif self.y > self.SH - self.JOGADOR_HEIGHT:
            self.y = self.SH - self.JOGADOR_HEIGHT

    def colisao():
        # TODO adicionar colisão ao jogador
        pass
