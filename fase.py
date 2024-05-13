from time import sleep
import pygame
from components.button import Button
from components.jogador import jogador
from components.obstaculo import obstaculo
from screens.screen import Screen_manager
# from Componentes_fase.PerguntaBox import PerguntaBox 

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = Screen_manager()


# setar relógio
clock = pygame.time.Clock()

def fase(dific):
    running = True
    
    jgdr = jogador(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    obs = []
    # quest = []


    # TODO adicionar dificuldade dinâmica √
    dificuldade = dific

    while running:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        jogar_mouse = pygame.mouse.get_pos()
        botao_sair = Button(image=None, pos=(SCREEN_WIDTH*2/3, 750), text_input="VOLTAR")

        for button in [botao_sair]:
            button.changeColor(jogar_mouse)
            button.update(screen)
        
        # métodos e variaveis do objeto jogador
        keys = pygame.key.get_pressed()
        jgdr.desenhar_jogador()
        jgdr.mover_jogador(keys)

        # obstáculos
        for i in range(dificuldade):
            # TODO adicionar tipos diferentes de obstáculos ?? 
            obs.append(obstaculo(SCREEN_WIDTH, SCREEN_HEIGHT, screen, dificuldade))
            obs[i].desenhar_obstaculo(obs[i], jgdr)

        #Perguntas
        # for c in range(dificuldade//5):
        #     quest.append(PerguntaBox(SCREEN_HEIGHT, SCREEN_WIDTH, screen))
        #     quest[c].desenhar_perguntas(quest[c], jgdr)

        # Update display
        pygame.display.update()
        if jgdr.pontos <= 0:
            running = False
            screen_manager.pop_screen()


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_sair.checkForInput(jogar_mouse):
                    running = False
                    screen_manager.pop_screen()



        # setar taxa de quadros pra 60 fps
        clock.tick(60)

