import pygame

class jogador:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen

        self.JOGADOR_WIDTH = 50
        self.JOGADOR_HEIGHT = 80

        self.x = (self.SW - self.JOGADOR_WIDTH) // 2
        self.y = self.SH - self.JOGADOR_HEIGHT - 20

        self.speed = 6
        self.pontos = 10
        self.vida = 10

        # Carregar imagem normal
        self.image_normal = pygame.image.load("assets/hotdog_normal.png").convert_alpha()

        # Carregar e redimensionar imagem original
        aspect_ratio = self.image_normal.get_width() / self.image_normal.get_height()
        new_height = 4*int(self.JOGADOR_WIDTH / aspect_ratio)
        self.player_image = pygame.transform.scale(self.image_normal, (4*self.JOGADOR_WIDTH, new_height))

        # Imagem para indicar movimento
        self.image_boost = pygame.image.load("assets/hotdog_boost.png").convert_alpha()

        # Criando retângulo
        self.rect = self.player_image.get_rect(topleft=(self.x, self.y))

    def desenhar_jogador(self):
        # Desenhar jogador
        self.screen.blit(self.player_image, (self.x, self.y))

    def mover_jogador(self, keys):
        # Posição antiga do jogador
        pos_antiga = (self.x, self.y)

        # Input do usuário
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Posição atual do jogador
        pos_atual = (self.x, self.y)

        # Verificar se está se movendo
        self.is_moving = pos_antiga != pos_atual

        # Alternar entre imagem normal e imagem de movimento
        if self.is_moving:
            self.player_image = pygame.transform.scale(self.image_boost, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))
        else:
            self.player_image = pygame.transform.scale(self.image_normal, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))

        # Garantir que o jogador não saia da tela
        self.x = max(0, min(self.x, self.SW - self.JOGADOR_WIDTH))
        self.y = max(self.SH // 2, min(self.y, self.SH - self.JOGADOR_HEIGHT))

    def tira_vida(self):
        self.vida -= 1
        self.pontos -= 1

    def colisao(self):
        # Tratar colisões (se necessário)
        pass