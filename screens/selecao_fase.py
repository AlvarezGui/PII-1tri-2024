import pygame
import sys
from components.button import Button
from screens.fase import fase
from screens.screen import Screen_manager
from components.jogador import jogador

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


def selecao_fase():
    pygame.display.set_caption("selecao_fase")
    running = True

    while running:
        screen.fill("white")

        selecao_mouse = pygame.mouse.get_pos()

        botao_fase1 = Button(image=None, pos=(SCREEN_WIDTH / 2, 150), text_input="FASE 1")
        botao_fase2 = Button(image=None, pos=(SCREEN_WIDTH / 2, 400), text_input="FASE 2")
        botao_fase3 = Button(image=None, pos=(SCREEN_WIDTH / 2, 650), text_input="FASE 3")
        botao_voltar = Button(image=None, pos=(SCREEN_WIDTH / 3, 400), text_input="VOLTAR")
        botao_selecionar_veiculo = Button(image=None, pos=(SCREEN_WIDTH - 200, 100), text_input="CARROS")

        # Fazer diplay da seleção de carro
        # hamburguer = pygame.image.load("assets/hamburguer_normal.png")
        # botao_hamburguer = Button(image=jogador.mostra_imagem(hamburguer), pos=(SCREEN_WIDTH*2 / 3, 400), text_input="")
        # hotdog = pygame.image.load("assets/hotdog_normal.png")
        # botao_hotdog = Button(image=jogador.mostra_imagem(hotdog), pos=(SCREEN_WIDTH*2 / 3, 525), text_input="")

        for button in [botao_fase1, botao_fase2, botao_fase3, botao_voltar, botao_selecionar_veiculo]:
            # button.changeColor(selecao_mouse)
            button.update(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_fase1.checkForInput(selecao_mouse):
                    fs = fase(3, model)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_fase2.checkForInput(selecao_mouse):
                    fs = fase(6, model)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_fase3.checkForInput(selecao_mouse):
                    fs = fase(12, model)
                    screen_manager.push_screen(fs.desenhar_fase())
                if botao_selecionar_veiculo.checkForInput(selecao_mouse):
                    model = selecao_carro()
                    screen_manager.push_screen(selecao_carro())
                if botao_voltar.checkForInput(selecao_mouse):
                    screen_manager.pop_screen()  # Volta para a tela anterior
                    return 
                

def selecao_carro():
    pygame.display.set_caption("SELECAO DE CARRO")
    running = True
    while running:
        screen.fill("white")

        selecao_carro_mouse = pygame.mouse.get_pos()

        hamburguer = pygame.image.load("assets/hamburguer_normal.png")
        botao_hamburguer = Button(image=jogador.mostra_imagem(hamburguer), pos=(SCREEN_WIDTH*2 / 3, 400), text_input="")
        hotdog = pygame.image.load("assets/hotdog_normal.png")
        botao_hotdog = Button(image=jogador.mostra_imagem(hotdog), pos=(SCREEN_WIDTH / 2, 400), text_input="") 

        botao_voltar = Button(image=None, pos=(SCREEN_WIDTH / 3, 400), text_input="VOLTAR")

        for button in [botao_hamburguer, botao_hotdog, botao_voltar]:
            button.changeColor(selecao_carro_mouse)
            button.update(screen)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_hamburguer.checkForInput(selecao_carro_mouse):
                    model = "hamburguer"
                if botao_hotdog.checkForInput(selecao_carro_mouse):
                    model = "hotdog"
                if botao_voltar.checkForInput(selecao_carro_mouse):
                    screen_manager.pop_screen()  # Volta para a tela anterior
                    running = False
                return model
