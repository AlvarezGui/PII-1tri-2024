import pygame


class Screen():
    SCREEN_WIDTH = 1020
    SCREEN_HEIGHT = 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ''''
    Colocar essa classe como PAI para todas as screens
    '''


    def cria_fundo(width):
        # FUNDO DA TELA
        fundo = pygame.image.load("assets/mapa.png").convert_alpha()
        FUNDO_WIDTH = width
        aspect_ratio = fundo.get_width() / fundo.get_height()
        FUNDO_HEIGHT = int(FUNDO_WIDTH / aspect_ratio)
        fundo_image = pygame.transform.scale(fundo, (FUNDO_WIDTH, FUNDO_HEIGHT))
        return fundo_image
    
    def cria_painel(width):
        # IMAGEM PAINEL
        painel = pygame.image.load("assets/painel.png").convert_alpha()
        PAINEL_WIDTH = width
        aspect_ratio = painel.get_width() / painel.get_height()
        PAINEL_HEIGHT = int(PAINEL_WIDTH / aspect_ratio)
        painel_image = pygame.transform.scale(painel, (PAINEL_WIDTH, PAINEL_HEIGHT))
        return painel_image
    
    def cria_fundo_botao(width):
        # IMAGEM DO BOTÃO
        button = pygame.image.load("assets/button.png")
        aspect_ratio_button = button.get_width() / button.get_height()
        BUTTON_WIDTH = width
        BUTTON_HEIGHT = int(BUTTON_WIDTH / aspect_ratio_button)
        fundo_button = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))
        return fundo_button


class Screen_manager:
    def __init__(self):
        self.screen_stack = []

    def push_screen(self, screen):
        self.screen_stack.append(screen)

    def pop_screen(self):
        if self.screen_stack:
            self.screen_stack.pop()

    def current_screen(self):
        if self.screen_stack:
            return self.screen_stack[-1]
        return None
        