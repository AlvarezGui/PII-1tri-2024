import pygame

class InputBox:
    def __init__(self, label, screen, x, y, width, height, font_size):
        self.login_label = label
        self.user_text = ""
        self.input_rect = pygame.Rect(x, y, width, height)
        self.label_rect = pygame.Rect(x, y - 34, 110, 36)
        self.color = pygame.Color('black')
        self.screen = screen
        self.active = False

        # FONTE
        CAMINHO_FONTE = "./m6x11plus.ttf"
        self.base_font = pygame.font.Font(CAMINHO_FONTE, 50)
        self.input_font = pygame.font.Font(CAMINHO_FONTE, font_size)

    def checkForInput(self, position):
        if self.input_rect.collidepoint(position):
            self.active = True
        else:
            self.active = False
    
    def get_input(self):
        return self.user_text
    
    def blit_text(self, surface, text, pos):
        words = text.split(' ')
        space_width, space_height = self.input_font.size(' ')
        max_width = self.input_rect.width - 10  # Considera um pequeno padding dentro da caixa
        x, y = pos
        line_height = self.input_font.get_linesize()
        
        for word in words:
            word_surface = self.input_font.render(word, True, pygame.Color("white"))
            word_width, word_height = word_surface.get_size()

            # Verifica se a palavra cabe na linha atual, senão, vai para a próxima linha
            if x + word_width >= self.input_rect.right - 5:
                x = pos[0]  # Reseta x.
                y += line_height  # Move para a próxima linha.

            surface.blit(word_surface, (x, y))
            x += word_width + space_width  # Adiciona espaço entre as palavras

        return
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.checkForInput(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.user_text += " "
            elif event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                self.user_text += event.unicode
    
    def run_inputbox(self):
        # LABEL 
        label_user = self.base_font.render(self.login_label, True, ('white'))
        self.screen.blit(label_user, (self.label_rect.x + 5, self.label_rect.y - 15))
        self.label_rect.w = max(0, label_user.get_width() + 10)

        # INPUT BOX Rectangle
        pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
        self.blit_text(self.screen, self.user_text, (self.input_rect.x + 5, self.input_rect.y + 5))
