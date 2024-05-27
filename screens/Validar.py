import pygame
import sys
# from components.connector import connector
from screens.screen import Screen, Screen_manager
from screens.Cria_cadastro import Cria_cadastro
from screens.menu_principal import Main_menu
from components.button import Button
from components.Inputbox import InputBox

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

# FONTE
CAMINHO_FONTE = "./m6x11plus.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 32)

class Validar():
    def __init__(self):
        self.fundo_image = Screen.cria_fundo(Screen.SCREEN_WIDTH)
        self.fundo_button = Screen.cria_fundo_botao(250)
        self.painel_image = Screen.cria_painel(SCREEN_WIDTH + 150)
        self.running = True
        self.input_usuario = InputBox("E-MAIL:", screen, 200, 196, 600, 40, 32)
        self.input_senha = InputBox("SENHA:", screen, 200, 296, 600, 40, 32)

    def run(self):
        while self.running:
            pygame.display.set_caption("Login")

            screen.blit(self.fundo_image, (0, 0))
            screen.blit(self.painel_image, (-80, -190))

            logar_mouse = pygame.mouse.get_pos()

            botao_logar = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2 - 125, 500), text_input="ENTRAR")
            botao_criar_conta = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2 + 125, 500), text_input="CADASTRAR")
            botao_sair = Button(image=self.fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="CANCELAR")
            for button in [botao_logar, botao_criar_conta, botao_sair]:
                button.changeColor(logar_mouse)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.input_usuario.handle_event(event)
                self.input_senha.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_logar.checkForInput(logar_mouse):
                        print(f"Tentou logar com usuário: {self.input_usuario.get_input()} e senha: {self.input_senha.get_input()}")
                        screen_manager.push_screen(Main_menu().abre_menu_principal())
                    if botao_criar_conta.checkForInput(logar_mouse):
                        print("Tentou criar conta")
                        screen_manager.push_screen(Cria_cadastro().run())
                    if botao_sair.checkForInput(logar_mouse):
                        pygame.quit()
                        sys.exit()

            self.input_usuario.run_inputbox()
            self.input_senha.run_inputbox()
            pygame.display.update()
    