import pygame
import sys
import pygame.mixer
from backend.connector import connector
from components.Music import Music
from screens.screen import Screen, Screen_manager
from screens.Cria_cadastro import Cria_cadastro
from screens.menu_principal import Main_menu
from components.Button import Button
from components.Inputbox import InputBox
from components.SpriteSheet import SpriteSheet

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()
cnx = connector()

# FONTE
CAMINHO_FONTE = "./m6x11plus.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 32)


class Validar():
    def __init__(self):
        self.fundo_image = Screen.cria_fundo(SCREEN_WIDTH)
        self.fundo_button = SpriteSheet().cria_fundo_botao(200)
        self.painel_image = SpriteSheet().cria_painel(SCREEN_WIDTH-100)
        self.running = True
        self.input_usuario = InputBox("E-MAIL:", screen, 200, 196, 600, 40, 32)
        self.input_senha = InputBox("SENHA:", screen, 200, 296, 600, 40, 32)
        self.valida = 0

    def entrar(self, usuario, senha):
        print(f"Usuario: {usuario} \nSenha: {senha}")
        if usuario.endswith("@jpiaget.pro.br"):
            result = cnx.verificar_professor(usuario, senha)
            return result
        elif usuario.endswith("@jpiaget.g12.br"):
            result = cnx.verificar_aluno(usuario, senha)
            return result
        else:
            # TODO avisar que o email tem que ser da escola
            # "E-MAIL INVÁLIDO"
            return None
            

    def run(self):
        mensagem_erro = None
        while self.running:
            musica = Music()
            musica.play()

            pygame.display.set_caption("Login")

            screen.blit(self.fundo_image, (0, 0))
            screen.blit(self.painel_image, (50, 20))

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
                        usuario = self.input_usuario.get_input()
                        senha = self.input_senha.get_input()
                        print(f"Tentou logar com usuário: {usuario} e senha: {senha}")
                        
                        # Verifique se os campos estão preenchidos
                        if not usuario or not senha:
                            mensagem_erro = "TODOS OS CAMPOS DEVEM SER PREENCHIDOS!"
                        else:
                            mensagem_erro = None
                            resultado = self.entrar(usuario, senha)
                            print(resultado)
                            try: 
                                if resultado:
                                    screen_manager.push_screen(Main_menu().abre_menu_principal(usuario))
                                else:
                                    mensagem_erro = "USUÁRIO OU SENHA INVÁLIDOS!"
                            except:
                                mensagem_erro = "Email inválido"
                    if botao_criar_conta.checkForInput(logar_mouse):
                        print("Tentou criar conta")
                        screen_manager.push_screen(Cria_cadastro().run())
                    if botao_sair.checkForInput(logar_mouse):
                        pygame.quit()
                        sys.exit()

            if mensagem_erro:
                erro = base_font.render(mensagem_erro, True, ('white'))
                screen.blit(erro, (SCREEN_WIDTH/2 - erro.get_width() / 2, 50))

            self.input_usuario.run_inputbox()
            self.input_senha.run_inputbox()
            pygame.display.update()
    