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
    # IMAGEM DO BOTÃO
    button = pygame.image.load("assets/button.png")
    aspect_ratio_button = button.get_width() / button.get_height()
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = int(BUTTON_WIDTH / aspect_ratio_button)
    fundo_button = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))

    pygame.display.set_caption("selecao_fase")

    # FUNDO DA TELA
    fundo = pygame.image.load("assets/mapa.png").convert_alpha()
    FUNDO_WIDTH = SCREEN_WIDTH
    aspect_ratio = fundo.get_width() / fundo.get_height()
    FUNDO_HEIGHT = int(FUNDO_WIDTH / aspect_ratio)
    fundo_image = pygame.transform.scale(fundo, (FUNDO_WIDTH, FUNDO_HEIGHT))
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

        # Fazer diplay da seleção de carro
        # hamburguer = pygame.image.load("assets/hamburguer_normal.png")
        # botao_hamburguer = Button(image=jogador.mostra_imagem(hamburguer), pos=(SCREEN_WIDTH*2 / 3, 400), text_input="")
        # hotdog = pygame.image.load("assets/hotdog_normal.png")
        # botao_hotdog = Button(image=jogador.mostra_imagem(hotdog), pos=(SCREEN_WIDTH*2 / 3, 525), text_input="")

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
    # IMAGEM DO BOTÃO
    button = pygame.image.load("assets/button.png")
    aspect_ratio_button = button.get_width() / button.get_height()
    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = int(BUTTON_WIDTH / aspect_ratio_button)
    fundo_button = pygame.transform.scale(button, (BUTTON_WIDTH, BUTTON_HEIGHT))

    pygame.display.set_caption("SELECAO DE CARRO")
    running = True

    # IMAGEM DO FUNDO
    fundo = pygame.image.load("assets/mapa.png").convert_alpha()
    FUNDO_WIDTH = SCREEN_WIDTH
    aspect_ratio = fundo.get_width() / fundo.get_height()
    FUNDO_HEIGHT = int(FUNDO_WIDTH / aspect_ratio)
    fundo_image = pygame.transform.scale(fundo, (FUNDO_WIDTH, FUNDO_HEIGHT))

    painel = pygame.image.load("assets/painel.png").convert_alpha()
    PAINEL_WIDTH = SCREEN_WIDTH + 50
    aspect_ratio = painel.get_width() / painel.get_height()
    PAINEL_HEIGHT = int(PAINEL_WIDTH / aspect_ratio)
    painel_image = pygame.transform.scale(painel, (PAINEL_WIDTH, PAINEL_HEIGHT))

    while running:
        screen.fill("white")
        screen.blit(fundo_image, (0,0))
        screen.blit(painel_image, (-25,-150))

        selecao_carro_mouse = pygame.mouse.get_pos()

        hamburguer = pygame.image.load("assets/hamburguer_normal.png")
        botao_hamburguer = Button(image=jogador.mostra_imagem(hamburguer), pos=(SCREEN_WIDTH*2 / 3 + 100, 450), text_input="")
        hotdog = pygame.image.load("assets/hotdog_normal.png")
        botao_hotdog = Button(image=jogador.mostra_imagem(hotdog), pos=(SCREEN_WIDTH / 2, 450), text_input="") 
        donut = pygame.image.load("assets/donut_normal.png")
        botao_donut = Button(image=jogador.mostra_imagem(donut), pos=(SCREEN_WIDTH / 3 - 100, 450), text_input="") 
        abacate = pygame.image.load("assets/abacate_normal.png")
        botao_abacate = Button(image=jogador.mostra_imagem(abacate), pos=(SCREEN_WIDTH / 2, 200), text_input="") 
        ovo = pygame.image.load("assets/ovo_normal.png")
        botao_ovo = Button(image=jogador.mostra_imagem(ovo), pos=(SCREEN_WIDTH / 3 - 100, 200), text_input="") 

        botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH / 2, 650), text_input="VOLTAR")

        for button in [botao_hamburguer, botao_hotdog, botao_donut, botao_abacate, botao_ovo, botao_voltar]:
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
                    return model
                if botao_hotdog.checkForInput(selecao_carro_mouse):
                    model = "hotdog"
                    return model
                if botao_donut.checkForInput(selecao_carro_mouse):
                    model = "donut"
                    return model
                if botao_abacate.checkForInput(selecao_carro_mouse):
                    model = "abacate"
                    return model
                if botao_ovo.checkForInput(selecao_carro_mouse):
                    model = "ovo"
                    return model
                if botao_voltar.checkForInput(selecao_carro_mouse):
                    running = False
                    screen_manager.pop_screen()  # Volta para a tela anterior
                    model = None
                    return model
