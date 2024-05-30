import pygame
from components.Button import Button
from components.levels.jogador import Jogador
from components.levels.obstaculo import Obstaculo
from components.levels.perguntaBox import PerguntaBox
from screens.screen import Screen_manager, Screen
from pygame.sprite import Group

clock = pygame.time.Clock()

class Fase():
    def __init__(self, dific, model):
        self.dific = dific
        self.SCREEN_WIDTH = 1020
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen_manager = Screen_manager()
        self.model = model
        self.all_sprites = Group()
        self.obstacles = Group()
        self.questions = Group()

    def desenhar_fase(self):
        running = True
        fundo_image = Screen.cria_fundo(self.SCREEN_WIDTH)
        jgdr = Jogador(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, self.model)
        self.all_sprites.add(jgdr)

        for i in range(self.dific):
            obs = Obstaculo(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen, self.dific)
            self.obstacles.add(obs)
            self.all_sprites.add(obs)

        for c in range(self.dific // 5):
            quest = PerguntaBox(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)
            self.questions.add(quest)
            self.all_sprites.add(quest)

        botao_sair = Button(image=None, pos=(self.SCREEN_WIDTH * 2/3, 750), text_input="VOLTAR")

        while running:
            self.screen.blit(fundo_image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogar_mouse = pygame.mouse.get_pos()
                    if botao_sair.checkForInput(jogar_mouse):
                        self.screen_manager.pop_screen()
                        running = False

            keys = pygame.key.get_pressed()
            jgdr.update(keys)
            
            for obs in self.obstacles:
                obs.update(jgdr)
            
            for quest in self.questions:
                quest.update(jgdr)

            self.all_sprites.draw(self.screen)

            jogar_mouse = pygame.mouse.get_pos()
            botao_sair.changeColor(jogar_mouse)
            botao_sair.update(self.screen)

            pygame.display.flip()
            if jgdr.vida <= 0:
                running = False
                self.screen_manager.pop_screen()
            clock.tick(60)
