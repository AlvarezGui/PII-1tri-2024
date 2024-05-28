
import pygame
import sys
from components.Button import Button
from screens.Cria_cadastro import Cria_cadastro
from screens.screen import Screen, Screen_manager
from screens.settings.CRUD.Criar_pergunta_tela import Cria_pergunta
from screens.settings.CRUD.Criar_turma_tela import Cria_turma

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Manter_entidades:
    tipo: str
    def __init__(self, tipo):
        self.tipo = tipo

    def mostra_entidades(self):

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

            botao_criar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="CRIAR")
            botao_atualizar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 400), text_input="ATUALIZAR")
            botao_deletar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150 , 400), text_input="DELETAR")
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
                        if self.tipo == 'perguntas':
                            screen_manager.push_screen(Cria_pergunta().run())
                        if self.tipo == 'turmas':
                            screen_manager.push_screen(Cria_turma().run())
                        if self.tipo == 'contas':
                            screen_manager.push_screen(Cria_cadastro().run())
                    if botao_atualizar.checkForInput(selecao_mouse):
                        print("atualizar pergunta")
                    if botao_deletar.checkForInput(selecao_mouse):
                        print("deletar pergunta")
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False