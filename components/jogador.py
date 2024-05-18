import pygame

class jogador:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, screen, model):
        # Carregar imagem normal
        modelo = self.carro_modelo(model)
        self.image_normal = pygame.image.load(modelo[0]).convert_alpha()

        self.SW = SCREEN_WIDTH
        self.SH = SCREEN_HEIGHT
        self.screen = screen
        
        # Carregar e redimensionar imagem original
        self.JOGADOR_WIDTH = 80
        aspect_ratio = self.image_normal.get_width() / self.image_normal.get_height()
        self.JOGADOR_HEIGHT = int(self.JOGADOR_WIDTH / aspect_ratio)
        self.player_image = pygame.transform.scale(self.image_normal, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))

        self.x = (self.SW - self.JOGADOR_WIDTH) // 2
        self.y = self.SH - self.JOGADOR_HEIGHT - 20

        self.speed = 6
        self.pontos = 10
        self.vida = 10

        # Imagem para indicar movimento
        self.image_boost = pygame.image.load(modelo[1]).convert_alpha()

        # Criando retângulo
        self.image_rect = self.image_normal.get_rect()
        self.image_rect = pygame.Rect(self.x, self.y, self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT)
        # self.rect = pygame.Rect(self.image_rect.x, self.image_rect.y, self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT)

    def desenhar_jogador(self):
        # pygame.draw.rect(self.screen, (255, 0, 255), self.image_rect)
        # Desenhar jogador
        self.screen.blit(self.player_image, self.image_rect)

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

        # Atualizando o retangulo:
        self.image_rect.x = self.x
        self.image_rect.y = self.y


        # Alternar entre imagem normal e imagem de movimento
        if self.is_moving:
            self.player_image = pygame.transform.scale(self.image_boost, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))
        else:
            self.player_image = pygame.transform.scale(self.image_normal, (self.JOGADOR_WIDTH, self.JOGADOR_HEIGHT))

        # Garantir que o jogador não saia da tela
        self.x = max(0, min(self.x, self.SW - self.JOGADOR_WIDTH))
        self.y = max(0, min(self.y, self.SH - self.JOGADOR_HEIGHT))

    def tira_vida(self):
        self.vida -= 1

    def colisao(self):
        # Tratar colisões (se necessário)
        pass

    def mostra_imagem(imagem):
        IMAGE_WIDTH = 80
        aspect_ratio = imagem.get_width() / imagem.get_height()
        IMAGE_HEIGHT = int(IMAGE_WIDTH / aspect_ratio)
        image = pygame.transform.scale(imagem, (IMAGE_WIDTH, IMAGE_HEIGHT))
        return image

    @staticmethod
    def carro_modelo(modelo):
        if modelo == "hamburguer":
            return("assets/hamburguer_normal.png", "assets/hamburguer_boost.png")
        if modelo == "hotdog":
            return("assets/hotdog_normal.png", "assets/hotdog_boost.png")