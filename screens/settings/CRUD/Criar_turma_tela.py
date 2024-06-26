
import pygame
import sys
from components.Inputbox import InputBox
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen, Screen_manager
from backend.connector import connector

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()
cnx = connector()

class Cria_turma():
    def __init__(self):
        self.input_nome_turma = InputBox("Coloque o nome da turma:", screen, x=100, y=200, width=825, height=100, font_size=30)

        # FONTE
        CAMINHO_FONTE = "./m6x11plus.ttf"
        self.base_font = pygame.font.Font(CAMINHO_FONTE, 32)

    def run(self):
        running = True

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        # IMAGEM PAINEL
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH-100)

        while running:
            pygame.display.set_caption("Cria turma")
            screen.blit(fundo_painel, (50, 20))

            selecao_mouse = pygame.mouse.get_pos()

            botao_criar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 150, 650), text_input="CRIAR")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 - 150, 650), text_input="VOLTAR")

            for button in [botao_criar, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.input_nome_turma.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_criar.checkForInput(selecao_mouse):
                        cnx.adicionar_turma(turma=self.input_nome_turma.get_input())
                        screen_manager.pop_screen()
                        running = False
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False

            self.input_nome_turma.run_inputbox()
            pygame.display.update()
