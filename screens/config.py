import sys
import pygame
from components.button import Button
from screens.screen import Screen_manager, Screen

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class config():
    def mostra_config():
        pygame.display.set_caption("ajustes")
        running = True

        # IMAGEM PAINEL
        painel_image = Screen.cria_painel(SCREEN_WIDTH+250)

        # FUNDO DA TELA
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        while running:
            screen.fill("white")
            screen.blit(fundo_image, (0,0))
            screen.blit(painel_image, (-125,-230))

            selecao_mouse = pygame.mouse.get_pos()

            botao_muda_dificuldade = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="DIFICULDADE")
            botao_muda_volume = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 400), text_input="VOLUME")
            botao_manter = Button(image=fundo_button, pos=(SCREEN_WIDTH - 100, 400), text_input="MANTER")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_muda_dificuldade, botao_muda_volume,botao_manter, botao_voltar]:
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
                    if botao_manter.checkForInput(selecao_mouse):
                        print("Tentou manter")
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False
