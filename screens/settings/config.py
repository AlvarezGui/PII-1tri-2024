import sys
import pygame
from components.Button import Button
from components.SpriteSheet import SpriteSheet
from screens.settings.CRUD.Manter import Manter
from screens.screen import Screen_manager, Screen
from screens.settings.Dificuldade import Dificuldade
from screens.settings.Volume import Volume

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()

class config():
    def __init__(self):
        self.dificuldade = None

    def mostra_config(self):
        running = True

        # IMAGEM PAINEL
        painel_image = SpriteSheet().cria_painel(SCREEN_WIDTH-100)

        # IMAGEM DO BOTÃO
        fundo_button = SpriteSheet().cria_fundo_botao(250)

        dific = Dificuldade()

        while running:
            pygame.display.set_caption("Ajustes")

            screen.blit(painel_image, (50,20))

            selecao_mouse = pygame.mouse.get_pos()

            botao_muda_dificuldade = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 150), text_input="DIFICULDADE")
            botao_muda_volume = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 400), text_input="VOLUME")
            botao_manter = Button(image=fundo_button, pos=(SCREEN_WIDTH/2 + 300, 650), text_input="MANTER")
            botao_voltar = Button(image=fundo_button, pos=(SCREEN_WIDTH/2, 650), text_input="VOLTAR")

            for button in [botao_muda_dificuldade, botao_muda_volume, botao_manter, botao_voltar]:
                button.changeColor(selecao_mouse)
                button.update(screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_muda_dificuldade.checkForInput(selecao_mouse):
                        screen_manager.push_screen(dific.mostra_niveis())
                        self.dificuldade = dific.get_dific()
                        print(self.dificuldade)
                    if botao_muda_volume.checkForInput(selecao_mouse):
                        screen_manager.push_screen(Volume().mostra_Volume())
                    if botao_manter.checkForInput(selecao_mouse):
                        screen_manager.push_screen(Manter().mostra_Manter())
                    if botao_voltar.checkForInput(selecao_mouse):
                        screen_manager.pop_screen()
                        running = False
    
    def get_dific(self):
        return self.dificuldade
