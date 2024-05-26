import pygame
import sys
from components.button import Button
from screens.fase import fase
from screens.screen import Screen_manager, Screen
from components.levels.jogador import jogador
from screens.Selecao_carro import Selecao_carro

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


class Selecao_fase():
    def seleciona_fase(dific):
        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(200)

        pygame.display.set_caption("selecao_fase")

        # FUNDO DA TELA
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        running = True
        model = None

        while running:
            screen.fill("white")
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
                        fs = fase(3*dific, model)
                        screen_manager.push_screen(fs.desenhar_fase())
                    if botao_fase2.checkForInput(selecao_mouse):
                        fs = fase(6*dific, model)
                        screen_manager.push_screen(fs.desenhar_fase())
                    if botao_fase3.checkForInput(selecao_mouse):
                        fs = fase(12*dific, model)
                        screen_manager.push_screen(fs.desenhar_fase())
                    if botao_selecionar_veiculo.checkForInput(selecao_mouse):
                        model = Selecao_carro.escolhe_modelo()
                        screen_manager.push_screen(Selecao_carro.escolhe_modelo())
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False  # Volta para a tela anterior
                    

