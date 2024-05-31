import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.ranking import Ranking
from screens.screen import Screen_manager, Screen
from screens.play.selecao_fase import Selecao_fase
from screens.settings.config import config

''''
PARA OS BOTÕES DE VOLTAR, SEGUNDO O VIDEO, FOI COLOCADO TODAS AS SCREENS NO MSM ARQUIVO, PARA VOLTAR BASTAVA-SE COLOCAR O ONCLICK RODAR A TELA ANTERIOR, NÃO PODEMOS FAZER ISSO AQUI
'''

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

CAMINHO_FONTE = "./m6x11plus.ttf"
base_font = pygame.font.Font(CAMINHO_FONTE, 50)


class Main_menu():
    dific: int

    def __init__(self):
        self.dific = 1

    def abre_menu_principal(self, usuario):
        running = True
        configu = config()

        # FUNDO DA TELA
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)

        # LOGO
        logo_image = SpriteSheet().cria_logo(SCREEN_WIDTH - 500)

        selecao = Selecao_fase()

        while running:
            pygame.display.set_caption("Menu")

            #Sobreposição de telas
            screen.blit(fundo_image, (0,0))
            screen.blit(logo_image, (SCREEN_WIDTH/2 - logo_image.get_width()/2, 30))

            menu_mouse = pygame.mouse.get_pos()

            #Criando os botões
            botao_jogar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 400), text_input="JOGAR")
            botao_config = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 525), text_input="AJUSTES")
            botao_sair = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="SAIR")
            botao_deslogar = Button(image=fundo_button, pos=(120, 70), text_input="DESLOGAR")
            botao_ranking = Button(image=fundo_button, pos=(120, 720), text_input="RANKING")
            for button in [botao_jogar, botao_config, botao_ranking, botao_sair, botao_deslogar]:
                button.changeColor(menu_mouse)
                button.update(screen)

            label_pontos = pygame.font.Font(CAMINHO_FONTE, 20).render("PONTOS", True, ("white"))
            screen.blit(label_pontos, (20, 590))
            pontos = base_font.render(str(selecao.get_pontos()), True, ("white"))
            screen.blit(pontos, (20, 600))

            label_usuario = pygame.font.Font(CAMINHO_FONTE, 20).render("PONTOS", True, ("white"))
            screen.blit(label_usuario, (20, 520))
            user = base_font.render(str(usuario), True, ("white"))
            screen.blit(user, (20, 530))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                #Manejando os botões
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogar.checkForInput(menu_mouse):
                        screen_manager.push_screen(selecao.seleciona_fase(self.dific))
                    if botao_config.checkForInput(menu_mouse):
                        screen_manager.push_screen(configu.mostra_config())
                        self.dific = configu.get_dific()
                    if botao_deslogar.checkForInput(menu_mouse):
                        screen_manager.pop_screen()
                        running = False
                    if botao_ranking.checkForInput(menu_mouse):
                        screen_manager.push_screen(Ranking().mostra_ranking())
                    if botao_sair.checkForInput(menu_mouse):
                        pygame.quit()
                        sys.exit()