import pygame
import sys
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.screen import Screen_manager, Screen
from components.levels.jogador import Jogador
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class Selecao_carro():
    def escolhe_modelo():
        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(200)

        running = True

        # IMAGEM DO FUNDO
        fundo_image = Screen.cria_fundo(SCREEN_WIDTH)

        # IMAGEM PAINEL
        painel_image = SpriteSheet().cria_painel(SCREEN_WIDTH-100)

        while running:
            pygame.display.set_caption("Selecionando skin")
            screen.fill("white")
            screen.blit(fundo_image, (0,0))
            screen.blit(painel_image, (50,20))

            selecao_carro_mouse = pygame.mouse.get_pos()

            image_normal = Jogador.carro_modelo("hamburguer")[0]
            aspect_ratio = image_normal.get_width() / image_normal.get_height()
            JOGADOR_HEIGHT = int(80/ aspect_ratio)
            imagem_hamburger = pygame.transform.scale(image_normal, (80, JOGADOR_HEIGHT))
            botao_hamburguer = Button(image=imagem_hamburger, pos=(SCREEN_WIDTH*2 / 3 + 100, 450), text_input="")

            image_normal = Jogador.carro_modelo("hotdog")[0]
            aspect_ratio = image_normal.get_width() / image_normal.get_height()
            JOGADOR_HEIGHT = int(80/ aspect_ratio)
            imagem_hotdog = pygame.transform.scale(image_normal, (80, JOGADOR_HEIGHT))
            botao_hotdog = Button(image=imagem_hotdog, pos=(SCREEN_WIDTH / 2, 450), text_input="") 

            image_normal = Jogador.carro_modelo("donut")[0]
            aspect_ratio = image_normal.get_width() / image_normal.get_height()
            JOGADOR_HEIGHT = int(80/ aspect_ratio)
            imagem_donut = pygame.transform.scale(image_normal, (80, JOGADOR_HEIGHT))
            botao_donut = Button(image=imagem_donut, pos=(SCREEN_WIDTH / 3 - 100, 450), text_input="") 

            image_normal = Jogador.carro_modelo("abacate")[0]
            aspect_ratio = image_normal.get_width() / image_normal.get_height()
            JOGADOR_HEIGHT = int(80/ aspect_ratio)
            imagem_abacate = pygame.transform.scale(image_normal, (80, JOGADOR_HEIGHT))
            botao_abacate = Button(image=imagem_abacate, pos=(SCREEN_WIDTH / 2, 200), text_input="")
            
            image_normal = Jogador.carro_modelo("ovo")[0]
            aspect_ratio = image_normal.get_width() / image_normal.get_height()
            JOGADOR_HEIGHT = int(80/ aspect_ratio)
            imagem_ovo = pygame.transform.scale(image_normal, (80, JOGADOR_HEIGHT))
            botao_ovo = Button(image=imagem_ovo, pos=(SCREEN_WIDTH / 3 - 100, 200), text_input="") 

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
