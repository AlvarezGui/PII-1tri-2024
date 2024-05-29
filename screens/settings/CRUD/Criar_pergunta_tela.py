
import pygame
import sys
from components.Inputbox import InputBox
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen, Screen_manager

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Cria_pergunta():
    def __init__(self):
        self.input_enunciado = InputBox("Enunciado:", screen, 100, 100, 825, 250, 20)

        # FONTE
        CAMINHO_FONTE = "./m6x11plus.ttf"
        self.base_font = pygame.font.Font(CAMINHO_FONTE, 32)

    def run(self):
        running = True


        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)
        fundo_button_alternativas = Screen.cria_fundo_botao(100)

        # IMAGEM PAINEL
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH-100)

        while running:
            pygame.display.set_caption("Cria pergunta")

            screen.blit(fundo_painel, (50, 20))

            selecao_mouse = pygame.mouse.get_pos()

            label_qnt = self.base_font.render("Quantidade de alternativas:", True, ('white'))
            screen.blit(label_qnt, (SCREEN_WIDTH/2 - 145 , 350))

            botao_numero_alternativas4 = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 80, 415), text_input="4")
            botao_numero_alternativas5 = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 80, 415), text_input="5")

            label_alternativa = self.base_font.render("Alternativa correta:", True, ('white'))
            screen.blit(label_alternativa, (SCREEN_WIDTH/2 - 108 , 460))

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
                        running = False
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False

            self.input_enunciado.run_inputbox()
            pygame.display.update()
