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

    # FUNDO DA TELA
    fundo = pygame.image.load("assets/mapa.png").convert_alpha()
    FUNDO_WIDTH = SCREEN_WIDTH
    aspect_ratio = fundo.get_width() / fundo.get_height()
    FUNDO_HEIGHT = int(FUNDO_WIDTH / aspect_ratio)
    fundo_image = pygame.transform.scale(fundo, (FUNDO_WIDTH, FUNDO_HEIGHT))

    # IMAGEM DO BOTÃO
    button = pygame.image.load("assets/button.png")
    aspect_ratio_button = button.get_width() / button.get_height()
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = int(BUTTON_WIDTH / aspect_ratio_button)
    fundo_button = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))

    while running:
        screen.fill("white")
        screen.blit(fundo_image, (0,0))

        selecao_mouse = pygame.mouse.get_pos()

        botao_muda_dificuldade = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="DIFICULDADE")
        botao_muda_volume = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 400), text_input="VOLUME")
        botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

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
