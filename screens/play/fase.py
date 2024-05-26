from time import sleep
import pygame
from components.button import Button
from components.levels.jogador import jogador
from components.levels.obstaculo import obstaculo
from components.levels.perguntaBox import PerguntaBox
from screens.screen import Screen_manager, Screen


# setar relógio
clock = pygame.time.Clock()

class Fase():

    def __init__(self, dific, model):
        self.dific = dific
        self.SCREEN_WIDTH = 1020
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen_manager = Screen_manager()
        self.model = model

    def desenhar_fase(self):
        running = True

        # FUNDO IMAGEM 
        fundo_image = Screen.cria_fundo(self.SCREEN_WIDTH)
        
        jgdr = Jogador(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, self.model)
        obs = []
        quest = []


        # TODO adicionar dificuldade dinâmica √
        dificuldade = self.dific

        print(dificuldade)

        while running:
            self.screen.blit(fundo_image, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            jogar_mouse = pygame.mouse.get_pos()
            botao_sair = Button(image=None, pos=(self.SCREEN_WIDTH*2/3, 750), text_input="VOLTAR")

            for button in [botao_sair]:
                button.changeColor(jogar_mouse)
                button.update(self.screen)
            
            # métodos e variaveis do objeto jogador
            keys = pygame.key.get_pressed()
            jgdr.desenhar_jogador()
            jgdr.mover_jogador(keys)

            # obstáculos
            for i in range(dificuldade):
                # TODO adicionar tipos diferentes de obstáculos ?? 
                obs.append(Obstaculo(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, dificuldade))
                obs[i].desenhar_obstaculo(jgdr)

            #Perguntas
            for c in range(dificuldade//5):
                quest.append(PerguntaBox(self.SCREEN_HEIGHT, self.SCREEN_WIDTH, self.screen))
                quest[c].desenhar_perguntas(jgdr)

            # Update display
            pygame.display.update()
            if jgdr.vida <= 0:
                running = False
                self.screen_manager.pop_screen()


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_sair.checkForInput(jogar_mouse):
                        self.screen_manager.pop_screen()
                        running = False


            # setar taxa de quadros pra 60 fps
            clock.tick(60)

