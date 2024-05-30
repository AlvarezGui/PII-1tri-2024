import pygame


# SPRITESHEET
CAMINHO_PARA_SPRITESHEET = "assets/Sprite-0002.png"

class SpriteSheet():
    def __init__(self):
        try:
            self.sheet = pygame.image.load(CAMINHO_PARA_SPRITESHEET).convert_alpha()
        except pygame.error.message:
            print('Unable to load spritesheet image:', CAMINHO_PARA_SPRITESHEET)
            raise SystemExit.message
        
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    def cria_fundo_botao(self, width):
        # IMAGEM DO BOTÃO
        button = self.image_at((340,0,590,313), -1).convert_alpha()
        aspect_ratio_button = button.get_width() / button.get_height()
        BUTTON_WIDTH = width
        BUTTON_HEIGHT = int(BUTTON_WIDTH / aspect_ratio_button)
        fundo_button = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))
        return fundo_button
    
    def cria_painel(self, width):
        # IMAGEM PAINEL
        painel = self.image_at((652, 2016, 1265, 1043), -1).convert_alpha()
        PAINEL_WIDTH = width
        aspect_ratio = painel.get_width() / painel.get_height()
        PAINEL_HEIGHT = int(PAINEL_WIDTH / aspect_ratio)
        painel_image = pygame.transform.scale(painel, (PAINEL_WIDTH, PAINEL_HEIGHT))
        return painel_image
    
    def cria_enzima(self):
        # Carregando imagem 
        image = self.image_at(rectangle=(0, 0, 326, 308), colorkey=-1).convert_alpha()
        WIDTH = 80
        aspect_ratio = image.get_width() / image.get_height()
        HEIGHT = int(WIDTH / aspect_ratio) 

        # Fazendo o retângulo
        image_rect = image.get_rect()
        image_obstacle = pygame.transform.scale(image, (WIDTH, HEIGHT))
        image_rect = pygame.Rect(image_rect.x, image_rect.y, WIDTH, HEIGHT)
        return image_obstacle, image_rect