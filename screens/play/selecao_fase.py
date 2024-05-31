import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.play.fase import Fase
from screens.screen import Screen_manager, Screen
from .Selecao_carro import Selecao_carro

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


class Selecao_fase():
    def __init__(self):
        self.pontos = 0
    def seleciona_fase(self, dific):
        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)

        # FUNDO DA TELA
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        running = True
        model = None

        if type(dific) == None:
            dific = 1

        while running:
            pygame.display.set_caption("Seleção de level")

            screen.blit(fundo_image, (0,0))

            selecao_mouse = pygame.mouse.get_pos()

            botao_fase1 = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2, 150), text_input="FASE 1")
            botao_fase2 = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2, 400), text_input="FASE 2")
            botao_fase3 = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2, 650), text_input="FASE 3")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH / 3 - 200, 400), text_input="VOLTAR")
            botao_selecionar_veiculo = Button(image=fundo_button, pos=(SCREEN_WIDTH - 200, 100), text_input="CARROS")

            for button in [botao_fase1, botao_fase2, botao_fase3, botao_voltar, botao_selecionar_veiculo]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_fase1.checkForInput(selecao_mouse):
                        try:
                            fs = Fase(3*dific, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                        except:
                            fs = Fase(3, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                    if botao_fase2.checkForInput(selecao_mouse):
                        try:
                            fs = Fase(6*dific, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                        except:
                            fs = Fase(6, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                    if botao_fase3.checkForInput(selecao_mouse):
                        try:
                            fs = Fase(12*dific, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                        except:
                            fs = Fase(12, model)
                            result = fs.desenhar_fase()
                            screen_manager.push_screen(result)
                            self.pontos += result
                    if botao_selecionar_veiculo.checkForInput(selecao_mouse):
                        model = Selecao_carro.escolhe_modelo()
                        screen_manager.push_screen(Selecao_carro.escolhe_modelo())
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False  # Volta para a tela anterior
                    
    def get_pontos(self):
        return self.pontos

