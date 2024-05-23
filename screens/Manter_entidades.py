
import pygame
import sys
from components.button import Button
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Manter_coisas():
    tipo : str
    def __init__(self, tipo):
        self.tipo = tipo
        if self.tipo == 'turmas':
                print('tela de mudar turmas')
        if self.tipo == 'perguntas':
            print('tela de mudar perguntas')
        if self.tipo == 'contas':
            print('tela de mudar contas')

    def mostra_manter(self):
        pygame.display.set_caption("ajustes")
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        # IMAGEM PAINEL
        fundo_painel = Screen.cria_painel(SCREEN_WIDTH+250)

        while running:
            screen.blit(fundo_painel, (-125, -230))

            selecao_mouse = pygame.mouse.get_pos()

            botao_criar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 250, 150), text_input="CRIAR")
            botao_atualizar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="ATUALIZAR")
            botao_deletar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 250 , 150), text_input="DELETAR")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_criar, botao_atualizar, botao_deletar, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_criar.checkForInput(selecao_mouse):
                        print("")
                    if botao_atualizar.checkForInput(selecao_mouse):
                        print("")
                    if botao_deletar.checkForInput(selecao_mouse):
                        print("")
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False