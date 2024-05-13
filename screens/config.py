import sys
import pygame
from components.button import Button
from screens.screen import Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

def config():
    pygame.display.set_caption("ajustes")
    running = True

    while running:
        screen.fill("black")

        selecao_mouse = pygame.mouse.get_pos()

        botao_muda_dificuldade = Button(image=None, pos=(SCREEN_WIDTH/2, 150), text_input="DIFICULDADE")
        botao_muda_volume = Button(image=None, pos=(SCREEN_WIDTH/2, 400), text_input="VOLUME")
        botao_voltar = Button(image=None, pos=(SCREEN_WIDTH/3, 400), text_input="VOLTAR")

        for button in [botao_muda_dificuldade, botao_muda_volume, botao_voltar]:
            button.changeColor(selecao_mouse)
            button.update(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_muda_dificuldade.checkForInput(selecao_mouse):
                    print("Tela de mudar dificuldade")
                if botao_muda_volume.checkForInput(selecao_mouse):
                    print("Tela de mudar volume")
                if botao_voltar.checkForInput(selecao_mouse):
                    running = False
                    screen_manager.pop_screen()
