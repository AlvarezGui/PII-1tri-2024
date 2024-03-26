import pygame
import sys
import random
from obstaculo import *

# Initialize Pygame
pygame.init()

# setqar tela 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fast Food")

# cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# variaveis do carro
CAR_WIDTH = 50
CAR_HEIGHT = 80

# sprites do carro
# car_img = pygame.image.load('car.png')  # You need to have an image named 'car.png' in your directory

# setar relógio
clock = pygame.time.Clock()

def draw_car(x, y):
    # screen.blit(car_img, (x, y))
    pygame.draw.circle(screen, "red", (x, y), 40)

# def draw_obstacle(cordenadas_obstaculo_x, cordenadas_obstaculo_y):
#     pygame.draw.circle(screen, "blue", (cordenadas_obstaculo_x, cordenadas_obstaculo_y), 40)
    


def game():
    # poss inicial do carro
    car_x = (SCREEN_WIDTH - CAR_WIDTH) // 2
    car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20
    car_speed = 6

    coordenadas_obstaculo_y = -20
    coordenadas_obstaculo_x = random.randrange(0, SCREEN_WIDTH)
    velocidade_obstaculo = 4


    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed
        if keys[pygame.K_UP]:
            car_y -= car_speed
        if keys[pygame.K_DOWN]:
            car_y += car_speed

        # checar se o carro está dentro da tela
        if car_x < 0:
            car_x = 0
        elif car_x > SCREEN_WIDTH - CAR_WIDTH:
            car_x = SCREEN_WIDTH - CAR_WIDTH
        if car_y < SCREEN_HEIGHT / 2:
            car_y = SCREEN_HEIGHT / 2
        elif car_y > SCREEN_HEIGHT - CAR_HEIGHT:
            car_y = SCREEN_HEIGHT - CAR_HEIGHT

        # Clear the screen
        screen.fill(WHITE)

        # desenhar carro
        draw_car(car_x, car_y)

        # desenhar obstáculos
        # 2
        obs1 = obstaculo(coordenadas_obstaculo_x, coordenadas_obstaculo_y, velocidade_obstaculo)
        obs1.draw_obstacle()
        obs1.coordenadas_obstaculo_y += velocidade_obstaculo
        

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    game()
