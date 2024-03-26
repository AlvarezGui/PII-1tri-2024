import pygame
import random
from main import SCREEN_WIDTH, screen, SCREEN_HEIGHT

class obstaculo():

    def __init__(self, x, y, vel):
        self.coordenadas_obstaculo_y = y
        self.coordenadas_obstaculo_x = x
        self.velocidade_obstaculo = vel

    def draw_obstacle(self):
        while self.coordenadas_obstaculo_y <= SCREEN_HEIGHT + 10:
            pygame.time.delay(pygame.time.get_ticks())
            self.coordenadas_obstaculo_y += self.velocidade_obstaculo
            print(self.coordenadas_obstaculo_y)

        if self.coordenadas_obstaculo_y > SCREEN_HEIGHT + 10:
            self.coordenadas_obstaculo_x = random.randrange(0, SCREEN_WIDTH)
            self.coordenadas_obstaculo_y = -20
        
        pygame.draw.circle(screen, "blue", (self.coordenadas_obstaculo_x, self.coordenadas_obstaculo_y), 40)
       