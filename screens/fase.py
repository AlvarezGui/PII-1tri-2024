from time import sleep
import pygame
from components.button import Button
from components.jogador import jogador
from components.obstaculo import obstaculo
from screens.screen import Screen_manager
# from Componentes_fase.PerguntaBox import PerguntaBox 


# setar relógio
clock = pygame.time.Clock()

class fase():


    def __init__(self, dific):
        self.dific = dific
        self.SCREEN_WIDTH = 1020
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen_manager = Screen_manager()

    
    def desenhar_fase(self):
        running = True
        
        jgdr = jogador(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)
        obs = []
        # quest = []


        # TODO adicionar dificuldade dinâmica √
        dificuldade = self.dific

        while running:
            self.screen.fill("black")
            
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
                obs.append(obstaculo(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, dificuldade))
                obs[i].desenhar_obstaculo(obs[i], jgdr)

            #Perguntas
            # for c in range(dificuldade//5):
            #     quest.append(PerguntaBox(self.SCREEN_HEIGHT, SCREEN_WIDTH, screen))
            #     quest[c].desenhar_perguntas(quest[c], jgdr)

            # Update display
            pygame.display.update()
            if jgdr.vida <= 0:
                running = False
                self.screen_manager.pop_screen()


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_sair.checkForInput(jogar_mouse):
                        running = False
                        self.screen_manager.pop_screen()



            # setar taxa de quadros pra 60 fps
            clock.tick(60)

