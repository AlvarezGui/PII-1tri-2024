import sys
import pygame
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Ranking:
    def __init__(self):
        self.ranking = None
    
    def mostra_ranking(self):
        running = True

        # IMAGEM PAINEL
        painel_image = SpriteSheet().cria_painel(SCREEN_WIDTH-50)

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)


        while running:
            ranking_mouse = pygame.mouse.get_pos()

            screen.blit(painel_image, (25, 5))

            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 700), text_input="VOLTAR")

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
