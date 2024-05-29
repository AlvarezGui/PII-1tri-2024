
import pygame
import sys
from components.Button import Button
from components.Music import Music
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Volume:
    def mostra_Volume(self):
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        while running:
            selecao_mouse = pygame.mouse.get_pos()

            botao_muda_dificuldade = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="DIFICULDADE")
            botao_menor = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 250, 400), text_input="-")
            botao_maior = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 250 , 400), text_input="+")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_muda_dificuldade, botao_menor, botao_maior, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_menor.checkForInput(selecao_mouse):
                        Music.diminui_volume()
                    if botao_maior.checkForInput(selecao_mouse):
                        Music.aumenta_volume()
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False