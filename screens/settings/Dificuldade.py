import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Dificuldade:
    def __init__(self):
        self.dificuldade_selecionada = None

    def mostra_niveis(self):
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        while running:
            selecao_mouse = pygame.mouse.get_pos()

            botao_1 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 250 , 150), text_input="Fácil")
            botao_2 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="Normal")
            botao_3 = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 250, 150), text_input="Difícil")
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
                        self.dificuldade_selecionada = 1 
                        screen_manager.pop_screen()
                        running = False
                    if botao_2.checkForInput(selecao_mouse):
                        print("dific 2")
                        self.dificuldade_selecionada = 2
                        screen_manager.pop_screen()
                        running = False
                    if botao_3.checkForInput(selecao_mouse):
                        print("dific 3")
                        self.dificuldade_selecionada = 3
                        screen_manager.pop_screen()
                        running = False
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False
    
    def get_dific(self):
        return self.dificuldade_selecionada
