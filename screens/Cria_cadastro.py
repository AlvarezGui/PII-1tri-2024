import pygame
import sys
# from components.connector import connector
from components.Inputbox import InputBox
from screens.screen import Screen, Screen_manager
from components.button import Button

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

# FONTE
CAMINHO_FONTE = "./m6x11plus.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 32)

class Cria_cadastro():
    def __init__(self):
        self.fundo_button = Screen.cria_fundo_botao(250)
        self.painel_image = Screen.cria_painel(SCREEN_WIDTH + 150)
        self.running = True
        self.input_nome = InputBox("NOME:", screen, 200, 146, 600, 40, 32)
        self.input_email = InputBox("E-MAIL:", screen, 200, 246, 600, 40, 32)
        self.input_senha = InputBox("SENHA:", screen, 200, 346, 600, 40, 32)
        self.input_turma = InputBox("TURMA:", screen, 200, 446, 600, 40, 32)

    def run(self):
        pygame.display.set_caption("Login")
        
        while self.running:
            screen.blit(self.painel_image, (-80, -190))

            logar_mouse = pygame.mouse.get_pos()
        
            botao_cadastrar = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2 + 150, 650), text_input="CADASTRAR")
            botao_sair = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2 - 150, 650), text_input="CANCELAR")
            for button in [botao_cadastrar, botao_sair]:
                button.changeColor(logar_mouse)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.input_nome.handle_event(event)
                self.input_email.handle_event(event)
                self.input_senha.handle_event(event)
                self.input_turma.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_cadastrar.checkForInput(logar_mouse):
                        print("Tentou criar conta")
                    if botao_sair.checkForInput(logar_mouse):
                        screen_manager.pop_screen()
                        self.running = False
            
            self.input_nome.run_inputbox()
            self.input_email.run_inputbox()
            self.input_senha.run_inputbox()
            self.input_turma.run_inputbox()
            pygame.display.update()