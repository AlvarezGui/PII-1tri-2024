import sys
import pygame
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen_manager
from backend.connector import connector

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()
cnx = connector()

class Ranking:
    def __init__(self):
        self.ranking = None
    
    def mostra_ranking(self):
        running = True
        rankings = cnx.solicitar_ranking(tipo="aluno")

        # IMAGEM PAINEL
        painel_image = SpriteSheet().cria_painel(SCREEN_WIDTH-50)

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)

        while running:
            ranking_mouse = pygame.mouse.get_pos()

            screen.blit(painel_image, (25, 5))

            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 700), text_input="VOLTAR")

            if len(rankings) == 5:
                num1 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input=rankings[0][0])
                num2 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150, 300), text_input=rankings[1][0])
                num3 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 300), text_input=rankings[2][0])
                num4 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150, 450), text_input=rankings[3][0])
                num5 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 450), text_input=rankings[4][0])

                for button in [botao_voltar, num1, num2, num3, num4, num5]:
                    button.changeColor(ranking_mouse)
                    button.update(screen)

            else:
                for button in [botao_voltar]:
                    button.changeColor(ranking_mouse)
                    button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.checkForInput(ranking_mouse):
                        screen_manager.pop_screen()
                        running = False
