import pygame
import sys
from components.button import Button
from components.jogador import jogador
from components.obstaculo import obstaculo
from screens.screen import Screen_manager
from screens.selecao_fase import selecao_fase
from screens.config import config

''''
PARA OS BOTÕES DE VOLTAR, SEGUNDO O VIDEO, FOI COLOCADO TODAS AS SCREENS NO MSM ARQUIVO, PARA VOLTAR BASTAVA-SE COLOCAR O ONCLICK RODAR A TELA ANTERIOR, NÃO PODEMOS FAZER ISSO AQUI
'''

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


class main_menu():
    fundo = pygame.image.load("assets/mapa.png").convert_alpha()
    FUNDO_WIDTH = SCREEN_WIDTH
    aspect_ratio = fundo.get_width() / fundo.get_height()
    FUNDO_HEIGHT = int(FUNDO_WIDTH / aspect_ratio)
    fundo_image = pygame.transform.scale(fundo, (FUNDO_WIDTH, FUNDO_HEIGHT))
    pygame.display.set_caption("Menu")
    running = True

    while running:
        #Sobreposição de telas
        screen.fill("white")
        screen.blit(fundo_image, (0,0))

        menu_mouse = pygame.mouse.get_pos()

        #Criando os botões
        botao_jogar = Button(image=None, pos=(SCREEN_WIDTH/2, 150), text_input="JOGAR")
        botao_config = Button(image=None, pos=(SCREEN_WIDTH/2, 400), text_input="AJUSTES")
        botao_sair = Button(image=None, pos=(SCREEN_WIDTH/2, 650), text_input="SAIR")
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
                    screen_manager.push_screen(selecao_fase())
                if botao_config.checkForInput(menu_mouse):
                    screen_manager.push_screen(config())
                if botao_sair.checkForInput(menu_mouse):
                    pygame.quit()
                    sys.exit()
    