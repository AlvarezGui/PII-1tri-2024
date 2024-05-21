import pygame

class InputBox():


    def __init__(self, label, screen):
        self.login_label = label
        self.user_text = ""
        self.input_rect = pygame.Rect(200, 190, 220, 32)
        self.label_rect = pygame.Rect(200, 156, 110, 36)
        self.color = pygame.Color('black')

        # FONTE
        CAMINHO_FONTE = "./ComicsCarToon.ttf"
        self.base_font = pygame.font.Font(CAMINHO_FONTE, 32)
        
        # LABEL 
        pygame.draw.rect(screen, self.color, self.label_rect, 2)
        label_user = self.base_font.render(self.login_label, True, ('white'))
        screen.blit(label_user, (self.label_rect.x + 5, self.label_rect.y + 3))
        self.label_rect.w = max(0, label_user.get_width()+10)

        # INPUT BOX Rectangle
        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        user_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        screen.blit(user_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(600, user_surface.get_width())
        self.input_rect.h = 70
         

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def get_input(self):
        return self.user_text