
import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.Cria_cadastro import Cria_cadastro
from screens.screen import Screen, Screen_manager
from screens.settings.CRUD.Atualiza_tela import Atualiza
from screens.settings.CRUD.Criar_pergunta_tela import Cria_pergunta
from screens.settings.CRUD.Criar_turma_tela import Cria_turma
from screens.settings.CRUD.Delete_tela import Delete

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
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        # IMAGEM PAINEL
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH-100)

        while running:
            if self.tipo == 'perguntas':
                pygame.display.set_caption("Perguntas")
            if self.tipo == 'turmas':
                pygame.display.set_caption("Turmas")
            if self.tipo == 'contas':
                pygame.display.set_caption("Contas")

            screen.blit(fundo_painel, (50, 20))

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
                        screen_manager.push_screen(Atualiza(self.tipo).select_atualiza())
                    if botao_deletar.checkForInput(selecao_mouse):
                        screen_manager.push_screen(Delete(self.tipo).select_delete())
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False