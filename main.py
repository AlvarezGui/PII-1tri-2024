import pygame
from jogador import *
from obstaculo import *

pygame.init()

# setar tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fast Food")

# setar relógio
clock = pygame.time.Clock()


def game():
    running = True
    
    jgdr = jogador(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    obs = obstaculo(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    obs2 = obstaculo(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # métodos do objeto jogador
        keys = keys = pygame.key.get_pressed()
        jgdr.desenhar_jogador(jgdr)
        jgdr.mover_jogador(jgdr, keys)

        # obstáculos
        obs.desenhar_obstaculo(obs)
        obs2.desenhar_obstaculo(obs2)

        # Update display
        pygame.display.flip()

        # setar taxa de quadros pra 60 fps
        clock.tick(60)

        screen.fill('white')

if __name__ == "__main__":
    game()