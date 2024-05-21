import pygame
import sys
# from components.connector import connector
from screens.screen import Screen, Screen_manager
from components.button import Button
from screens.menu_principal import main_menu

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

# FONTE
CAMINHO_FONTE = "./ComicsCarToon.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 32)

class Cria_cadastro():
    def __init__(self):
        self.fundo_image = Screen.cria_fundo(Screen.SCREEN_WIDTH)
        self.fundo_button = Screen.cria_fundo_botao(250)
        self.painel_image = Screen.cria_painel(SCREEN_WIDTH + 150)
        self.running = True

        self.login_label = 'e-mail:'
        self.pass_label = 'senha:'
        self.turma_label = 'turma:'
        self.pass_text = self.user_text = self.turma_text = ''
        self.active_input = None

        # Criação do retangulos para inputs
        self.input_rect_user = pygame.Rect(200, 190, 220, 32)
        self.input_rect_pass = pygame.Rect(200, 300, 220, 32)
        self.input_rect_turma = pygame.Rect(200, 490, 220, 32)

        self.label_rect_user = pygame.Rect(200, 156, 110, 36)
        self.label_rect_pass = pygame.Rect(200, 266, 110, 36)
        self.label_rect_turma = pygame.Rect(100, 376, 110, 36)
        self.color = pygame.Color('black')

    # def validar_usuario(self, user, pas):
    #     # 1 checar a estrutura do email
    #     if user.endswith("@jpiaget.g12.br"):
    #         print("Estrutura de email correta")
    #         con.verificar_aluno(user, pas)
    #     elif user.endswith("@jpiaget.pro.br"):
    #         print("Você é um professor")
    #     else:
    #         print("Email inválido")

    def run(self):
        pygame.display.set_caption("Cadastrar")
        
        while self.running:
            screen.fill("white")
            screen.blit(self.fundo_image, (0, 0))
            screen.blit(self.painel_image, (-80, -190))

            cadastrar_mouse = pygame.mouse.get_pos()

            botao_cadastrar = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2 - 125, 500), text_input="CADASTRAR")
            botao_sair = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="CANCELAR")
            for button in [botao_cadastrar, botao_sair]:
                button.changeColor(cadastrar_mouse)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect_user.collidepoint(event.pos):
                        self.active_input = 'user'
                    elif self.input_rect_pass.collidepoint(event.pos):
                        self.active_input = 'pass'
                    elif self.input_rect_turma.collidepoint(event.pos):
                        self.active_input = 'turma'
                    else:
                        self.active_input = None

                    if botao_cadastrar.checkForInput(cadastrar_mouse):
                        print(f"Tentou cadastrar com usuário: {self.user_text} e senha: {self.pass_text}")
                        screen_manager.push_screen(main_menu.abre_menu_principal())
                    if botao_cadastrar.checkForInput(cadastrar_mouse):
                        print("Tentou criar conta")
                    if botao_sair.checkForInput(cadastrar_mouse):
                        pygame.quit()
                        sys.exit()

                # FUNCIONALIDADE DE ESCREVER
                if event.type == pygame.KEYDOWN:
                    if self.active_input == 'user':
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text += event.unicode
                    elif self.active_input == 'pass':
                        if event.key == pygame.K_BACKSPACE:
                            self.pass_text = self.pass_text[:-1]
                        else:
                            self.pass_text += event.unicode

            # LABEL USUARIO
            pygame.draw.rect(screen, self.color, self.label_rect_user, 2)
            label_user = base_font.render(self.login_label, True, ('white'))
            screen.blit(label_user, (self.label_rect_user.x + 5, self.label_rect_user.y + 3))
            self.label_rect_user.w = max(0, label_user.get_width()+10)

            # INPUT BOX USUARIO
            pygame.draw.rect(screen, self.color, self.input_rect_user, 2)
            user_surface = base_font.render(self.user_text, True, (255, 255, 255))
            screen.blit(user_surface, (self.input_rect_user.x + 5, self.input_rect_user.y + 5))
            self.input_rect_user.w = max(600, user_surface.get_width())
            self.input_rect_user.h = 70
            
            # LABEL SENHA
            pygame.draw.rect(screen, self.color, self.label_rect_pass, 2)
            label_pass = base_font.render(self.pass_label, True, ('white'))
            screen.blit(label_pass, (self.label_rect_pass.x + 5, self.label_rect_pass.y + 3))
            self.label_rect_pass.w = max(0, label_pass.get_width()+10)

            # INPUT BOX SENHA
            pygame.draw.rect(screen, self.color, self.input_rect_pass, 2)
            pass_surface = base_font.render('*' * len(self.pass_text), True, (255, 255, 255))
            screen.blit(pass_surface, (self.input_rect_pass.x + 5, self.input_rect_pass.y + 5))
            self.input_rect_pass.w = max(600, pass_surface.get_width() + 10)
            self.input_rect_pass.h = 70

            # LABEL TURMA
            pygame.draw.rect(screen, self.color, self.label_rect_turma, 2)
            label_turma = base_font.render(self.turma_label, True, ('white'))
            screen.blit(label_turma, (self.label_rect_turma.x + 5, self.label_rect_turma.y + 3))
            self.label_rect_turma.w = max(0, label_turma.get_width()+10)

            pygame.display.update()

            # self.validar_usuario(self.user_text, self.pass_text)

            

    