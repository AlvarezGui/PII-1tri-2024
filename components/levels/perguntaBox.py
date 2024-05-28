import pygame
import random

class PerguntaBox():

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen) -> None:
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.WIDTH = 50
        self.HEIGHT = 80

        self.x = random.randrange(0, self.SW)
        self.y = -20
        self.speed = random.randrange(1,6)
        self.is_active = False

    def desenhar_perguntas(self, jogador):
        # Carregar imagem
        image_normal = pygame.image.load("assets/question.png").convert_alpha()

        # Calcular altura proporcional
        aspect_ratio = image_normal.get_width() / image_normal.get_height()
        new_height = int(self.WIDTH / aspect_ratio)

        # Redimensionar imagem
        question_image = pygame.transform.scale(image_normal, (self.WIDTH, new_height))

        # Desenhar imagem
        self.screen.blit(question_image, (self.x, self.y))

        # Movimentar pergunta
        self.y += self.speed

        # Checar colisão com jogador
        rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        jogador.rect_jogador = pygame.Rect(jogador.x, jogador.y, jogador.JOGADOR_WIDTH, jogador.JOGADOR_HEIGHT)


        if rect.colliderect(jogador.rect_jogador):
            # TODO acessar pergunta.
            self.is_active = True

        if self.y > self.SH + 50:
            self.x = random.randrange(0, self.SW)
            self.y = -20
            self.speed = random.randrange(2,6)
