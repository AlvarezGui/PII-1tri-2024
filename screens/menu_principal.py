import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
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


class Main_menu():
    dific: int

    def __init__(self):
        self.dific = 1

    def abre_menu_principal(self):
        running = True
        configu = config()

        # FUNDO DA TELA
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)

        while running:
            pygame.display.set_caption("Menu")

            #Sobreposição de telas
            screen.blit(fundo_image, (0,0))

            menu_mouse = pygame.mouse.get_pos()

            #Criando os botões
            botao_jogar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 400), text_input="JOGAR")
            botao_config = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 525), text_input="AJUSTES")
            botao_sair = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="SAIR")
            botao_deslogar = Button(image=fundo_button, pos=(100, 70), text_input="DESLOGAR")
            for button in [botao_jogar, botao_config, botao_sair, botao_deslogar]:
                button.changeColor(menu_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                #Manejando os botões
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogar.checkForInput(menu_mouse):
                        screen_manager.push_screen(Selecao_fase.seleciona_fase(self.dific))
                    if botao_config.checkForInput(menu_mouse):
                        screen_manager.push_screen(configu.mostra_config())
                        self.dific = configu.get_dific()
                    if botao_deslogar.checkForInput(menu_mouse):
                        screen_manager.pop_screen()
                        running = False
                    if botao_sair.checkForInput(menu_mouse):
                        pygame.quit()
                        sys.exit()