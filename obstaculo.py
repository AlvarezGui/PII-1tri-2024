import pygame
import random

class obstaculo():

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen) -> None:
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.WIDTH = 50
        self.HEIGHT = 80

        self.x = random.randrange(0, self.SW)
        self.y = -20
        self.speed = random.randrange(1,6)

    @staticmethod
    def desenhar_obstaculo(self, jogador):
        # TODO impedir os obstáculos de spawnarem em cima uns dos outros
        pygame.draw.circle(self.screen, "blue", (self.x, self.y), 40)
        self.y += self.speed

        rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

        if rect.colliderect(jogador.rect):
            # TODO game over.
            print("Colidiu")

        if self.y > self.SH + 50:
            self.x = random.randrange(0, self.SW)
            self.y = -20
            self.speed = random.randrange(2,6)