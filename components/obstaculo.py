import pygame
import random
import time
import threading
from components.jogador import jogador

class obstaculo():

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen, dific) -> None:
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen
        self.color = "blue"

        self.WIDTH = 50
        self.HEIGHT = 80

        self.x = random.randrange(0, self.SW)
        self.y = -20

        # setar velocidade de acordo com a velocidade
        if dific <= 5:
            self.velocidade_range_min = 1
            self.velocidade_range_max = 6
            self.speed = random.randrange(1,6)
        elif 5 < dific <= 10:
                self.velocidade_range_min = 5
                self.velocidade_range_max = 9
                self.speed = random.randrange(5,9)
        elif 10 < dific <= 15:
            self.velocidade_range_min = 8
            self.velocidade_range_max = 12
            self.speed = random.randrange(8, 12)


    @staticmethod
    def desenhar_obstaculo(self, jogador):
        # TODO impedir os obstáculos de spawnarem em cima uns dos outros
        # TODO timer randomico para o primeiro spawn

        # esperar para respawnar o obstáculo
        def esperar():
            self.y = -100
            self.speed = 0
            time.sleep(random.randrange(1, 4))
            self.x = random.randrange(0, self.SW)
            self.speed = random.randrange(self.velocidade_range_min, self.velocidade_range_max)
        t1 = threading.Thread(target=esperar)

        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 40)
        self.y += self.speed


        rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        rectJogador = pygame.Rect(jogador.x, jogador.y, jogador.JOGADOR_WIDTH, jogador.JOGADOR_HEIGHT)

        if rect.colliderect(rectJogador):
            # TODO game over.
            self.color = "green"
            jogador.tira_pontos()
            print(jogador.pontos)

        if self.y > self.SH + 50:
            t1.start()

            

    
    