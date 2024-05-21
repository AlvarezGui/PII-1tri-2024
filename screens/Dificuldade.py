import pygame
import sys
from components.button import Button
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Dificuldade:
    dific = 1

    def mostra_niveis(self):
        pygame.display.set_caption("ajustes")
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        while running:
            selecao_mouse = pygame.mouse.get_pos()

            botao_1 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 250 , 150), text_input="1")
            botao_2 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="2")
            botao_3 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 250, 150), text_input="3")
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
                        dificuldade_selecionada = 1 
                        screen_manager.pop_screen()
                        running = False
                    if botao_2.checkForInput(selecao_mouse):
                        print("dific 2")
                        dificuldade_selecionada = 2
                        screen_manager.pop_screen()
                        running = False
                    if botao_3.checkForInput(selecao_mouse):
                        print("dific 3")
                        dificuldade_selecionada = 3
                        screen_manager.pop_screen()
                        running = False
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False
    
    def get_dific(self):
        return self.dific
