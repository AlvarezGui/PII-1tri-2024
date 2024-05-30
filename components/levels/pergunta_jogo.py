import pygame
import sys
from components.Button import Button
from screens.screen import Screen_manager
from components.SpriteSheet import SpriteSheet

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class PerguntaJogo:
    def __init__(self, enunciado, alternativas, resposta_correta):
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta

    def run(self):
        running = True
        fundo_painel = SpriteSheet().cria_painel(SCREEN_WIDTH-100)
        fundo_button_alternativas = SpriteSheet().cria_fundo_botao_pequeno(70)

        while running:
            pygame.display.set_caption("PERGUNTA!")

            screen.blit(fundo_painel, (50, 20))

            selecao_mouse = pygame.mouse.get_pos()
            if self.alternativas == 5:
                botao_a = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 250, 525), text_input="A")
                botao_b = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 - 125, 525), text_input="B")
                botao_c = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2, 525), text_input="C")
                botao_d = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 125, 525), text_input="D")
                botao_e = Button(image=fundo_button_alternativas, pos=(SCREEN_WIDTH/2 + 250, 525), text_input="E")

            for button in [botao_a, botao_b, botao_c, botao_d, botao_e]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_a.checkForInput(selecao_mouse):
                        print("Alternativa A")
                        screen_manager.pop_screen()
                        return True
                    if botao_b.checkForInput(selecao_mouse):
                        print("Alternativa B")
                    if botao_c.checkForInput(selecao_mouse):
                        print("Alternativa C")
                    if botao_d.checkForInput(selecao_mouse):
                        print("Alternativa D")
                    if botao_e.checkForInput(selecao_mouse):
                        print("Alternativa E")

            pygame.display.update()

