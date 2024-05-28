import pygame
import sys
from components.button import Button
from screens.screen import Screen_manager, Screen
from components.levels.jogador import Jogador
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Selecao_carro():
    def escolhe_modelo():
        # IMAGEM DO BOTÃO
        fundo_button = Screen.cria_fundo_botao(200)

        running = True

        # IMAGEM DO FUNDO
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        # IMAGEM PAINEL
        painel_image = Screen.cria_painel(SCREEN_WIDTH+100)

        while running:
            pygame.display.set_caption("Selecionando skin")
            screen.fill("white")
            screen.blit(fundo_image, (0,0))
            screen.blit(painel_image, (-25,-150))

            selecao_carro_mouse = pygame.mouse.get_pos()

            hamburguer = pygame.image.load("assets/hamburguer_normal.png")
            botao_hamburguer = Button(image=Jogador.mostra_imagem(hamburguer), pos=(SCREEN_WIDTH*2 / 3 + 100, 450), text_input="")
            hotdog = pygame.image.load("assets/hotdog_normal.png")
            botao_hotdog = Button(image=Jogador.mostra_imagem(hotdog), pos=(SCREEN_WIDTH / 2, 450), text_input="") 
            donut = pygame.image.load("assets/donut_normal.png")
            botao_donut = Button(image=Jogador.mostra_imagem(donut), pos=(SCREEN_WIDTH / 3 - 100, 450), text_input="") 
            abacate = pygame.image.load("assets/abacate_normal.png")
            botao_abacate = Button(image=Jogador.mostra_imagem(abacate), pos=(SCREEN_WIDTH / 2, 200), text_input="") 
            ovo = pygame.image.load("assets/ovo_normal.png")
            botao_ovo = Button(image=Jogador.mostra_imagem(ovo), pos=(SCREEN_WIDTH / 3 - 100, 200), text_input="") 

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