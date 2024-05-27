import pygame
import sys
from components.button import Button
from screens.settings.CRUD.Manter_enitdades import Manter_entidades
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Manter:
    def mostra_Manter(self):
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)

        #IMAGEM DO PAINEL
        fundo_painel = Screen.cria_painel(SCREEN_WIDTH+250)

        while running:
            screen.blit(fundo_painel, (-125, -230))
            
            selecao_mouse = pygame.mouse.get_pos()

            botao_turma = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="TURMAS")
            botao_conta = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 250 , 400), text_input="CONTAS")
            botao_pergunta = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 250, 400), text_input="PERGUNTAS")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_pergunta, botao_conta, botao_turma, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_turma.checkForInput(selecao_mouse):
                        print("Tentou manter turmas")
                        screen_manager.push_screen(Manter_entidades('turmas').mostra_entidades())
                    if botao_conta.checkForInput(selecao_mouse):
                        screen_manager.push_screen(Manter_entidades('contas').mostra_entidades())
                    if botao_pergunta.checkForInput(selecao_mouse):
                        screen_manager.push_screen(Manter_entidades('perguntas').mostra_entidades())
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False