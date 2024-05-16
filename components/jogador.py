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
        self.is_moving = False
        self.pontos = 10
        self.vida = 10
        self.image = pygame.image.load("assets/hotdog_normal.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.image, (200, 200))

        # Criando retangulo
        self.rect = self.player_image.get_rect(topleft=(self.x, self.y))

    def desenhar_jogador(self):
        # TODO adicionar sprite do jogador :3
        self.screen.blit(self.player_image, (self.x, self.y))

    def mover_jogador(self, keys):
        #Posição antiga do jogador:
        pos_antiga = (self.x, self.y)

        # input do usuario
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        #Posição atual do jogador
        pos_atual = (self.x, self.y)

        # pos
        if pos_antiga!=pos_atual:
            self.is_moving = True
        else:
            self.is_moving = False

        #mudando de cor se estiver movendo
        if self.is_moving:
            self.image = pygame.image.load("assets/hotdog_boost.png").convert_alpha()
            self.screen.blit(self.player_image, (self.x, self.y))
        else:
            self.image = pygame.image.load("assets/hotdog_normal.png").convert_alpha()
            self.screen.blit(self.player_image, (self.x, self.y))

        # garantir que o jogador não saia da tela e não passe da metade de sua altura
        if self.x < 0:
            self.x = 0
        elif self.x > self.SW - self.JOGADOR_WIDTH:
            self.x = self.SW - self.JOGADOR_WIDTH
        if self.y < self.SH / 2:
            self.y = self.SH / 2
        elif self.y > self.SH - self.JOGADOR_HEIGHT:
            self.y = self.SH - self.JOGADOR_HEIGHT

    def tira_vida(self):
        self.vida -= 1
        self.pontos -=1

    def colisao():
        '''

        foi feita no objeto obstaculo pois um obstaculo pode colidir apenas com um jogador,
        mas um jogador pode colidir com varios obstaculos.
        manterei a função aqui para caso eu queira lidar com outros tipos de colisão.

        '''
        pass
