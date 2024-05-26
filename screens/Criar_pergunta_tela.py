
import pygame
import sys
from components.Inputbox import InputBox
from components.button import Button
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Cria_pergunta():
    def __init__(self):
        self.input_enunciado = InputBox("Enunciado:", screen, 100, 100, 825, 250, 20)

    def run(self):
        pygame.display.set_caption("Cria pergunta")
        running = True


        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(250)
        fundo_button_alternativas = Screen.cria_fundo_botao(100)

        # IMAGEM PAINEL
        fundo_painel = Screen.cria_painel(SCREEN_WIDTH+250)

        while running:
            screen.blit(fundo_painel, (-125, -230))

            selecao_mouse = pygame.mouse.get_pos()

            botao_numero_alternativas4 = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 100, 400), text_input="4")
            botao_numero_alternativas5 = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 100, 400), text_input="5")
            botao_a = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 250, 525), text_input="A")
            botao_b = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 125, 525), text_input="B")
            botao_c = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2, 525), text_input="C")
            botao_d = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 125, 525), text_input="D")
            botao_e = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 250, 525), text_input="E")
            botao_criar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 650), text_input="CRIAR")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150, 650), text_input="VOLTAR")

            for button in [botao_numero_alternativas5, botao_numero_alternativas4, botao_a, botao_b, botao_c, botao_d, botao_e, botao_criar, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.input_enunciado.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_numero_alternativas4.checkForInput(selecao_mouse):
                        print("A questão terá 4 alternativas")
                    if botao_numero_alternativas5.checkForInput(selecao_mouse):
                        print("A questão terá 5 alternativas")
                    if botao_criar.checkForInput(selecao_mouse):
                        print("Pergunta criada")
                        screen_manager.pop_screen()
                        pygame.display.set_caption("Perguntas")
                        running = False
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        pygame.display.set_caption("Perguntas")
                        running = False

            self.input_enunciado.run_inputbox()
            pygame.display.update()
