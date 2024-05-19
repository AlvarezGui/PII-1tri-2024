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

        # Carregando imagem 
        self.image = pygame.image.load("assets/enzima.png").convert_alpha()
        self.image.convert()


        self.WIDTH = 80
        aspect_ratio = self.image.get_width() / self.image.get_height()
        self.HEIGHT = int(self.WIDTH / aspect_ratio)

        self.x = random.randrange(0, self.SW)
        self.y = -20

        self.e_primeira = True

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

    def desenhar_obstaculo(self, jogador):
        # TODO impedir os obstáculos de spawnarem em cima uns dos outros

        # Fazendo o retângulo
        # rect = pygame.draw.circle(self.screen, self.color, (self.x, self.y), 40)
        self.image_rect = self.image.get_rect()
        self.image_obstacle = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.image_rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

        # pygame.draw.rect(self.screen, (0, 255, 255), self.image_rect)
        self.screen.blit(self.image_obstacle, self.image_rect)
        # TODO timer randomico para o primeiro spawn

        # esperar para respawnar o obstáculo
        def esperar():
            self.y = -100
            self.speed = 0
            time.sleep(random.randrange(1, 4))
            self.x = random.randrange(0, self.SW)
            self.speed = random.randrange(self.velocidade_range_min, self.velocidade_range_max)
            self.color = "blue"
        t1 = threading.Thread(target=esperar)

        if self.e_primeira:
            t1.start()
            self.e_primeira = False

        self.y += self.speed
       

        # coll
        rectJogador = pygame.Rect(jogador.x, jogador.y, jogador.JOGADOR_WIDTH, jogador.JOGADOR_HEIGHT)

        if self.image_rect.colliderect(rectJogador):
            # TODO game over.
            jogador.tira_vida()
            print(jogador.vida)

        # checar se o objeto está fora da tela
        if self.y > self.SH + 50:
            t1.start()

            '''
            achar um equilibrio entre a 1 e 3 fase no que se trata de velocidade e quantidade
            e decidir se terá ou não um timer para esperar o spawn dos obstáculos
            '''
            
            # self.y = -100
            # self.x = random.randrange(0, self.SW)
            # self.speed = random.randrange(self.velocidade_range_min, self.velocidade_range_max)

            

    
    