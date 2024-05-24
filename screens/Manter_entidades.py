
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
        if tipo == 'turmas':
            print('tela de mudar turmas')
            self.tipo = 'T'
        if tipo == 'perguntas':
            print('tela de mudar perguntas')
            self.tipo = 'P'
        if tipo == 'contas':
            print('tela de mudar contas')
            self.tipo = 'C'

    def mostra_manter(self):
        pygame.display.set_caption("ajustes")
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)
        fundo_button_alternatvas = Screen.cria_fundo_botao(150)

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

            # SEPARAÇÃO TURMAS/PERGUNTAS/CONTAS
            if self.tipo == 'T':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botao_criar.checkForInput(selecao_mouse):
                            print("tentou criar turma")
                        if botao_atualizar.checkForInput(selecao_mouse):
                            print("tentou atualizar turma")
                        if botao_deletar.checkForInput(selecao_mouse):
                            print("tentou deletar turma")
                        if botao_voltar.checkForInput(selecao_mouse):
                            screen_manager.pop_screen()
                            running = False

            if self.tipo == 'P':
                botao_alternativas4 = Button(image=fundo_button_alternatvas, pos=(SCREEN_WIDTH/2 - 150, 400), text_input="4")
                botao_alternativas5 = Button(image=fundo_button_alternatvas, pos=(SCREEN_WIDTH/2 + 150, 400), text_input="5")

                for button in [botao_alternativas4, botao_alternativas5]:
                    button.changeColor(selecao_mouse)
                    button.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botao_criar.checkForInput(selecao_mouse):
                            print("tentou criar pergunta")
                        if botao_atualizar.checkForInput(selecao_mouse):
                            print("tentou atualizar pergunta")
                        if botao_deletar.checkForInput(selecao_mouse):
                            print("tentou deletar pergunta")
                        if botao_voltar.checkForInput(selecao_mouse):
                            screen_manager.pop_screen()
                            running = False
            
            if self.tipo == 'C':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if botao_criar.checkForInput(selecao_mouse):
                            print("tentou criar conta")
                        if botao_atualizar.checkForInput(selecao_mouse):
                            print("tentou atualizar conta")
                        if botao_deletar.checkForInput(selecao_mouse):
                            print("tentou deletar conta")
                        if botao_voltar.checkForInput(selecao_mouse):
                            screen_manager.pop_screen()
                            running = False