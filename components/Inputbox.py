import pygame

class InputBox():

    def __init__(self, label, screen, x, y, width, height):
        self.login_label = label
        self.user_text = ""
        self.input_rect = pygame.Rect(x, y, width, height)
        self.label_rect = pygame.Rect(x, y-34, 110, 36)
        self.color = pygame.Color('black')
        self.screen = screen
        self.active = False

        # FONTE
        CAMINHO_FONTE = "./m6x11plus.ttf"
        self.base_font = pygame.font.Font(CAMINHO_FONTE, 32)

    def checkForInput(self, position):
        if self.input_rect.collidepoint(position):
            self.active = True
        else:
            self.active = False
    
    def get_input(self):
        return self.user_text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.checkForInput(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(self.user_text)
                self.user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                self.user_text += event.unicode
    

    def run_inputbox(self):
        # LABEL 
        pygame.draw.rect(self.screen, self.color, self.label_rect, 2)
        label_user = self.base_font.render(self.login_label, True, ('white'))
        self.screen.blit(label_user, (self.label_rect.x + 5, self.label_rect.y + 3))
        self.label_rect.w = max(0, label_user.get_width()+10)

        # INPUT BOX Rectangle
        pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
        user_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        self.screen.blit(user_surface, (self.input_rect.x + 5, self.input_rect.y + 5))


