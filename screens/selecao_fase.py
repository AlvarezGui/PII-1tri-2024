import pygame
import sys
from components.button import Button
from screens.fase import fase
from screens.screen import Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


def selecao_fase():
    pygame.display.set_caption("selecao_fase")
    running = True

    while running:
        screen.fill("black")

        selecao_mouse = pygame.mouse.get_pos()

        botao_fase1 = Button(image=None, pos=(SCREEN_WIDTH / 2, 150), text_input="FASE 1")
        botao_fase2 = Button(image=None, pos=(SCREEN_WIDTH / 2, 400), text_input="FASE 2")
        botao_fase3 = Button(image=None, pos=(SCREEN_WIDTH / 2, 650), text_input="FASE 3")
        botao_voltar = Button(image=None, pos=(SCREEN_WIDTH/3, 400), text_input="VOLTAR")

        for button in [botao_fase1, botao_fase2, botao_fase3, botao_voltar]:
            button.changeColor(selecao_mouse)
            button.update(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_fase1.checkForInput(selecao_mouse):
                    fs = fase(3)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_fase2.checkForInput(selecao_mouse):
                    fs = fase(6)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_fase3.checkForInput(selecao_mouse):
                    fs = fase(12)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_voltar.checkForInput(selecao_mouse):
                    screen_manager.pop_screen()  # Volta para a tela anterior
                    return
                