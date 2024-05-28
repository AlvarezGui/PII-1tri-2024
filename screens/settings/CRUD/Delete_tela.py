
import pygame
import sys
from components.Button import Button
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Delete:
    tipo: str
    def __init__(self, tipo):
        self.tipo = tipo

    def select_delete(self):

        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        # IMAGEM PAINEL
        fundo_painel = Screen.cria_painel(SCREEN_WIDTH+250)

        while running:
            if self.tipo == 'perguntas':
                pygame.display.set_caption("Perguntas")
            if self.tipo == 'turmas':
                pygame.display.set_caption("Turmas")
            if self.tipo == 'contas':
                pygame.display.set_caption("Contas")

            screen.blit(fundo_painel, (-125, -230))

            selecao_mouse = pygame.mouse.get_pos()

            botao_delete = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 650), text_input="DELETAR")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150, 650), text_input="VOLTAR")

            for button in [botao_delete, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_delete.checkForInput(selecao_mouse):
                        print("Tentou deletar")
                        if self.tipo == 'turmas':
                            print("tentou deletar uma turma")
                        if self.tipo == 'perguntas':
                            print("tentou deletar perguntas")
                        if self.tipo == 'contas':
                            print("tentou deletar contas")
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False