import pygame
import sys
from components.button import Button
from screens.screen import Screen_manager, Screen
from screens.selecao_fase import Selecao_fase
from screens.config import config

''''
PARA OS BOTÕES DE VOLTAR, SEGUNDO O VIDEO, FOI COLOCADO TODAS AS SCREENS NO MSM ARQUIVO, PARA VOLTAR BASTAVA-SE COLOCAR O ONCLICK RODAR A TELA ANTERIOR, NÃO PODEMOS FAZER ISSO AQUI
'''

# SCREEN PARAMETERS
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


class main_menu():

    # FUNDO DA TELA
    fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

    pygame.display.set_caption("Menu")
    running = True

    # IMAGEM DO BOTÃO
    fundo_button = Screen.cria_fundo_botao(200)

    while running:
        #Sobreposição de telas
        screen.fill("white")
        screen.blit(fundo_image, (0,0))

        menu_mouse = pygame.mouse.get_pos()

        #Criando os botões
        botao_jogar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 350), text_input="JOGAR")
        botao_config = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 500), text_input="AJUSTES")
        botao_sair = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="SAIR")
        for button in [botao_jogar, botao_config, botao_sair]:
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
                    screen_manager.push_screen(Selecao_fase.seleciona_fase())
                if botao_config.checkForInput(menu_mouse):
                    screen_manager.push_screen(config.mostra_config())
                if botao_sair.checkForInput(menu_mouse):
                    pygame.quit()
                    sys.exit()
    