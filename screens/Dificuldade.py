import pygame
import sys
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Dificuldade:
    def mostra_niveis():
        pygame.display.set_caption("ajustes")
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        while running:
            selecao_mouse = pygame.mouse.get_pos()

            botao_1 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 100 , 200), text_input="1")
            botao_2 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 200), text_input="2")
            botao_3 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 100, 200), text_input="3")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_1, botao_2, botao_3, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_1.checkForInput(selecao_mouse):
                        print("dific 1")
                    if botao_2.checkForInput(selecao_mouse):
                        print("dific 2")
                    if botao_3.checkForInput(selecao_mouse):
                        print("dific 3")
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False
